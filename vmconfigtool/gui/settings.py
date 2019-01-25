"""
Tools for displaying a settings dialog window.
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte
from gi.repository import GLib
from gi.repository import GdkPixbuf

class SettingsDialog(Gtk.Dialog):
    """
    Settings dialog window for the configuration tool.
    """

    def __init__(self, parent, config):
        Gtk.Dialog.__init__(
            self, "Settings", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self._settings = {}
        self.config = config
        self.set_default_size(400, 100)

        # Use a grid so that the labels and entries can be aligned correctly.
        grid = Gtk.Grid()
        grid.set_row_spacing(6)
        grid.set_column_spacing(6)
        grid.set_border_width(6)

        branch_label = _create_label("Release track:")
        url_label = _create_label("Source URL:")

        branch_entry = _create_entry(config.get_value("git-branch"))
        url_entry  = _create_entry(config.get_value("git-url"))

        self._register_setting("git-branch", branch_entry)
        self._register_setting("git-url", url_entry)

        grid.attach(branch_label, 0, 0, 1, 1)
        grid.attach(branch_entry, 1, 0, 1, 1)
        grid.attach(url_label, 0, 1, 1, 1)
        grid.attach(url_entry, 1, 1, 1, 1)

        self.get_content_area().pack_end(grid, False, False, 0)

        grid.show_all()

    def _register_setting(self, key, widget):
        """
        Registers a setting and its associated GTK widget. This allows it to
        be retrieved by the settings key later.
        """

        self._settings[key] = widget

    def get_setting(self, key):
        """
        Retrieves the value associated with a particular setting. This allows
        for the caller to get the value the user chose.
        """

        widget = self._settings.get(key, None)
        if widget is None:
            return None

        if isinstance(widget, Gtk.Entry):
            # The docs say that the string returned from get_text() should not
            # be freed, modified, nor stored. It is unclear if this is a
            # relic from C++, but to be safe, we'll make a copy of the string
            # and return that to the caller.
            return str(widget.get_text())
        if isinstance(widget, Gtk.Checkbox):
            return widget.is_active()

        # Add more widget types here as appropriate
        return None


def _create_label(text):
    """
    Helps with creating a GTK Label. Sets the text to the given text and then
    right-justifies the text.
    """

    label = Gtk.Label(text)
    label.set_justify(Gtk.Justification.RIGHT)
    label.set_halign(Gtk.Align.END)
    return label

def _create_entry(text, width=40):
    """
    Creates a GTK Entry widget with the given width and default text.
    """

    entry = Gtk.Entry()
    entry.set_text(text)
    entry.set_width_chars(width)
    return entry
