"""
Copyright (C) 2021 Oscar Franzén <oscarfranzen@protonmail.com>

This file is part of PySide6 Simple Example Project.

PySide6 Simple Example Project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PySide6 Simple Example Project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PySide6 Simple Example Project.  If not, see <https://www.gnu.org/licenses/>.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple PySide6 project structure.',
    'author': 'Some One',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'someone@email.com',
    'version': '0.1',
    'install_requires': ['PySide6', 'PyInstaller'],
    'packages': [],
    'scripts': [],
    'name': 'pyside6_example_project'
}

setup(**config)

