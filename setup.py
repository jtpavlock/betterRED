#!/usr/bin/env python3
"""Define project and dependencies"""

from distutils.core import setup

setup(
    name='betterRED',
    version='0.1.2',
    description='Automatic helper for redacted better.php',
    url='https://github.com/jtpavlock/betterRED',
    packages=[],
    scripts=['bin/better_red'],
    install_requires=['mutagen'],
    python_requires='>=3.6',
    )
