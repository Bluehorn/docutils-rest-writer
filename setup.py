# coding: utf-8

from os import path
from codecs import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

def extract_version():
    about = {}
    execfile("docutils_rest_writer/about.py", about)
    return about["__version__"]


setup(
    name='docutils-rest-writer',
    version=extract_version(),
    description='reStructuredText writer for docutils',
    long_description=long_description,

    url='https://github.com/Bluehorn/docutils-rest-writer',

    author='Torsten Landschoff',
    author_email='torsten@landschoff.net',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Developers',
        'Topic :: Documentation',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='rest docutils',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['docutils'],

    extras_require = {
        'test': ['pytest'],         # $ pip install -e .[dev,test]
    },

    entry_points={
        'console_scripts': [
            'rst2rst=docutils_rest_writer.cmdline:rst2rst',
        ],
    },
)
