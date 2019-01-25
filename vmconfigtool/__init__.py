"""
Allows ways to get some default values for data as well as to get some
commonly-needed values.
"""

import os


_DEFAULT_GIT_REMOTE = "https://github.com/jmunixusers/cs-vm-build"
_DEFAULT_CONFIG_PATH = os.path.join(
    os.environ['HOME'], ".config", "vm_config", "config.json"
)
_COURSES = {
    'CS 101': 'cs101',
    'CS 149': 'cs149',
    'CS 159': 'cs159',
    'CS 261': 'cs261',
    'CS 354': 'cs354',
    'CS 361': 'cs361',
    'CS 430': 'cs430',
}
_NAME = "JMU CS VM Configuration Tool"
__version__ = "2.0.0"

def default_git_remote():
    """
    Provides the URL for the default remote of the Ansible playbook git repo.
    """

    return _DEFAULT_GIT_REMOTE


def default_config_path():
    """
    Provides the default path for the user's configuration
    """

    return _DEFAULT_CONFIG_PATH


def courses():
    """
    Gives a list of all supported courses.
    """

    return dict(_COURSES)


def name():
    """
    Provides the name of the tool.
    """

    return _NAME

def version():
    """
    Provides the version of the tool.
    """

    return __version__
