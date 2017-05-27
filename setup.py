#!/usr/bin/env python

"""The setup and build script for the optparse-modular-example."""

import os
import setuptools


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setuptools.setup(
    name='optparse-modular-example',
    version='0.0.1',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    license='MIT',
    url='https://github.com/strizhechenko/optparse-modular-example',
    keywords='example optparse modular utils',
    description='I tried to find a nice way for modular optparse'
        'that would provide opportunity to create meta-utils easily',
    long_description=(read('README.rst')),
    packages=setuptools.find_packages(exclude=['tests*']),
    scripts=[os.path.join('utils/', script) for script in os.listdir('utils/')],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
