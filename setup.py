#!/usr/bin/env python

import os

from setuptools import find_packages, setup

setup(
    name="clcache",
    description="MSVC compiler cache",
    author="Frerich Raabe <raabe@froglogic.com>, Kay Hayen <kay.hayen@gmail.com>",
    url="https://github.com/Nuitka/clcache",
    packages=find_packages(),
    platforms="any",
    keywords=[],
    install_requires=[
        'typing; python_version < "3.5"',
        'subprocess.run; python_version < "3.5"',
        "atomicwrites",
        "pymemcache",
        "pyuv",
    ],
    entry_points={
        "console_scripts": [
            "clcache = clcache.__main__:main",
            "clcache-server = clcache.server.__main__:main",
        ]
    },
    setup_requires=[
        "setuptools_scm",
    ],
    data_files=[
        ("", ("clcache.pth",)),
    ],
    use_scm_version=True,
)
