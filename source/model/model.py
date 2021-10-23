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

import logging
import pickle

from PySide6 import QtCore

logger = logging.getLogger(__name__)

class MyModel(QtCore.QObject):
    """
        This is where the abstract model lives. This could be a database with some added
        functionality, or a physics engine which continually calculates the positions of the
        bodies in a planetary system. This is the core of the app if you will, what the app
        is about. Making visual sense of the abstract data in the Model is the job of
        the View and Presenter. 
    """

    def __init__(self):
        super(MyModel, self).__init__()


    def quit(self):
        """
            This method gets called before the app exits, to give us a chance to exit cleanly
            if this is deemed necessary.
        """
        pass


    def add(self, a, b):
        return a + b
