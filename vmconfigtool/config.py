"""
Tools for managing the user's configuration.
"""

import json


class Config(object):
    """
    A configuration object to preserve settings across runs of the script. This
    provides tools for setting and retrieving values as well as writing and
    loading a config.
    """

    def __init__(self, init=None):
        if init is None:
            self._config = {}
        else:
            self._config = dict(init)

    def set_value(self, entry, value):
        """
        Set a particular configuration parameter.
        """

        self._config[entry] = value

    def get_value(self, entry, value=None):
        """
        Get the value of a particular configuration parameter.
        """

        return self._config.get(entry, value)

    def write(self, path):
        """
        Write the configuration to disk in JSON.
        """

        pass

    @classmethod
    def load(cls, path):
        """
        Load the user configuration from JSON.
        """

        return cls()
