"""
Allows for create an About dialog window.
"""
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte
from gi.repository import GLib
from gi.repository import GdkPixbuf

from vmconfigtool import (
    name,
    version,
)

from vmconfigtool import gui

class ConfigToolAboutDialog(Gtk.AboutDialog):
    """
    An about dialog for the VM Configuration Tool
    """

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self, parent=parent)

        try:
            self.set_logo(
                GdkPixbug.new_from_file_at_size(
                    gui.get_icon_path(), 96, 96
                )
            )
        except Exception as err:
            # TODO: Log message
            pass

        self.set_transient_for(parent)
        self.set_program_name(name())
        self.set_copyright("Copyright \xa9 2019 JMU Unix Users Group")
        self.set_comments(
            "A tool for configuring virtual machines created by the JMU"
            " Unix Users Group within the JMU Department of Computer Science,"
            " maintained by the JMU Unix Users Group."
        )

        # Anyone making significant contributions to the configuration tool
        # should add themself as an author explicitly
        self.set_authors(["Kyle Laker", "Members of the JMU Unix Users Group"])
        self.set_website("https://github.com/jmunixusers/cs-vm-build")
        self.set_website_label("Project GitHub page")
        self.set_version(version())
        self.set_license_type(Gtk.License.MIT_X11)
        self.connect("response", _destroy_about_dialog)

def _destroy_about_dialog(dialog, _):
    dialog.destroy()
