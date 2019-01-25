"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import codecs
import re
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# These two functions are used to provide a single source for the package
# version as described in option 1 at:
# https://packaging.python.org/guides/single-sourcing-package-version/
def read(*parts):
    with codecs.open(path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vmconfigtool',

    version=find_version("vmconfigtool", "__init__.py"),

    description='JMU CS VM Configuration Tool',

    long_description=long_description,

    long_description_content_type='text/markdown',

    #url='https://github.com/jmunixusers/vmconfigtool',

    author='JMU Unix Users Group',

    classifiers=[
        'Development Status :: 4 - Beta',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'pyyaml',
        'pygobject',
    ],

    entry_points={
        'console_scripts': [
            'vmconfigtool=vmconfigtool.main:main',
        ],
    },
)
