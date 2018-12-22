"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vmconfigtool',  # Required

    version='2.0.0',

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
        'pygobject',
    ],

    entry_points={
        'console_scripts': [
            'sample=vmconfigtool.main:main',
        ],
    },
)
