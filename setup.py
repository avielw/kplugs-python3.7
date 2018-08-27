#!/usr/bin/python3

from distutils.core import setup

VERSION = "3.3.3"

setup(
    name = 'kplugs',
    python_requires='==3.7.*',
    packages = ['kplugs'],
    version = VERSION,
    description = 'The KPlugs Python module',
    author = 'Aviel Warschawski',
    author_email = 'contact@kplugs.org',
    url = 'https://github.com/avielw/kplugs-python3.7',
    keywords = [
        'kplugs',
        'kernel',
        'linux',
        'debug',
    ],
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
    ],
)
