"""
Handles creating and managing the GUI.
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte
from gi.repository import GLib
from gi.repository import GdkPixbuf

from vmconfigtool import (
    config,
    courses,
    gui,
    name,
)

from vmconfigtool.gui.about import ConfigToolAboutDialog
from vmconfigtool.gui.settings import SettingsDialog

class AnsibleWrapperWindow(Gtk.Window):
    """
    The main window for the program. Includes a series of checkboxes for
    courses as well as a VTE to show the output of the Ansible command.
    """


    def __init__(self, config):
        Gtk.Window.__init__(self, title=name())
        self.config = config
        self.checkboxes = []

        icon_location = gui.get_icon_path()

        # Attempt setting the icon for the window to the UUG Tux
        try:
            self.set_icon_from_file(icon_location)
        except GLib.GError as err:
            pass

        # Create a box to contain all elements that will be added to the window
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(self.vbox)

        self.create_menu_bar()

        # Create a box to contain all the elements below the toolbar
        contents = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        contents.set_border_width(10)

        instructions = Gtk.Label(
            "Select the course configurations to add/update"
            "(courses cannot be removed)."
        )
        instructions.set_alignment(0.0, 0.0)

        contents.pack_start(instructions, False, False, 0)

        courses_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # This button doesn't do anything. Common is always run
        refresh = Gtk.CheckButton("Base configuration")
        refresh.set_tooltip_text("This option is required")
        refresh.set_active(True)
        refresh.set_sensitive(False)
        courses_box.pack_start(refresh, False, False, 0)

        # Add a checkbox for every course; sorting is necessary because
        # dictionaries do not guarantee that order is preserved
        for (course, tag) in sorted(courses().items()):
            checkbox = Gtk.CheckButton(course)
            checkbox.set_tooltip_text("Configure for %s" % course)
            courses_box.pack_start(checkbox, False, False, 0)
            if tag in self.config.get_value('roles-this-run'):
                checkbox.set_active(True)
            checkbox.connect("toggled", self.on_course_toggled, tag)
            self.checkboxes.append(checkbox)
        contents.pack_start(courses_box, False, False, 0)

        # Add run and cancel buttons
        button_box = Gtk.Box(spacing=6)
        self.run_button = Gtk.Button.new_with_label("Run")
        self.run_button.set_tooltip_text("Configure the VM")
        self.run_button.connect("clicked", self.on_run_clicked)
        button_box.pack_start(self.run_button, True, True, 0)
        self.cancel_button = Gtk.Button.new_with_mnemonic("_Quit")
        self.cancel_button.connect("clicked", Gtk.main_quit)
        button_box.pack_end(self.cancel_button, True, True, 0)
        contents.pack_end(button_box, False, True, 0)

        # Add the terminal to the window
        self.terminal = Vte.Terminal()
        # Prevent the user from entering text or ^C
        self.terminal.set_input_enabled(False)
        # Ensure that if text is written, the user sees it
        self.terminal.set_scroll_on_output(True)
        # Ensure that all lines can be seen (default is only 512)
        self.terminal.set_scrollback_lines(-1)
        self.terminal.connect("child-exited", self.sub_command_exited)
        contents.pack_end(self.terminal, True, True, 0)
        self.vbox.pack_end(contents, True, True, 0)

        self.connect("delete-event", Gtk.main_quit)

    def create_menu_bar(self):
        """
        Creates the menu bar at the top of the window.
        """

        menu_bar = Gtk.MenuBar()

        # Create the File menu
        file_menu = Gtk.Menu()
        file_item = Gtk.MenuItem("File")
        file_item.set_submenu(file_menu)

        # Add settings and quit items to the File menu
        settings = Gtk.MenuItem("Settings\u2026")
        settings.connect("activate", self.show_settings)
        file_menu.append(settings)
        quit_item = Gtk.MenuItem("Quit")
        quit_item.connect("activate", Gtk.main_quit)
        file_menu.append(quit_item)

        menu_bar.append(file_item)

        # Create the Help menu
        help_menu = Gtk.Menu()
        help_item = Gtk.MenuItem("Help")
        help_item.set_submenu(help_menu)

        # Add about item to the Help menu
        about = Gtk.MenuItem("About")
        about.connect("activate", self.show_about_dialog)
        help_menu.append(about)

        menu_bar.append(help_item)

        # Add the menu bar to the window
        self.vbox.pack_start(menu_bar, False, False, 0)

    def main(self):
        """
        A convenient way to have a caller enter the GTK main loop without
        requiring them to import the GTK libraries.
        """

        Gtk.main()

    def show_settings(self, _):
        """
        Display the settings dialog and save the user's settings if they
        choose 'OK'.
        """

        dialog = SettingsDialog(parent=self, config=self.config)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            config.set_value('git-branch', dialog.get_setting('git-branch'))
            config.set_value('git-url', dialog.get_setting('git-url'))
            config.write()
        dialog.destroy()

    def show_about_dialog(self, _):
        """
        Display the About dialog for the tool.
        """

        ConfigToolAboutDialog(parent=self).show()

    def sub_command_exited(self, _, exit_status):
        pass

    def on_run_clicked(self, _):
        pass

    @staticmethod
    def on_course_toggled(button, name):
        pass


