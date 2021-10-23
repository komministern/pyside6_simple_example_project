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

import os
import sys
import logging

from PySide6 import QtCore, QtGui, QtWidgets
# from .ui_mainwindow import Ui_MainWindow
from .main.mainwindow import MyMainwindow

logger = logging.getLogger(__name__)

class MyView(QtCore.QObject):
    """
        The View object is just a subclassed QMainWindow which contains the all the
        applications widgets. The main window and its contents is created with the 
        Qt Designer application. The ui file is found in the resources directory. 
    """

    def __init__(self):
        super(MyView, self).__init__()

        self.mainwindow = MyMainwindow()
