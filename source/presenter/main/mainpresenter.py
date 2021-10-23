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

from PySide6 import QtCore, QtGui, QtWidgets

logger = logging.getLogger(__name__)

class MainPresenter(QtCore.QObject):
    """
        The Presenter object contains the intelligence of the GUI. That is, here
        resides the interactions between the widgets in the View object. The Presenter
        acts upon signals sent from both the View and the Model.

        The Presenter object has access to both the View and Model objects, so its
        actions takes the form of method calls to these.
    """

    update_calendar = QtCore.Signal(list)

    def __init__(self, model, view, app):
        super(MainPresenter, self).__init__()

        # Store view, model and app.
        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()


    def connectSignals(self):
        """
            Here we connect the signals from both Model and View to methods in the
            Presenter object.
        """
        self.view.mainwindow.myQuitSignal.connect(self.quit)
        self.view.mainwindow.pushButton_Calculate.pressed.connect(self.calculate)
        self.view.mainwindow.spinBox_a.valueChanged.connect(self.eraseResult)
        self.view.mainwindow.spinBox_b.valueChanged.connect(self.eraseResult)


    def quit(self):
        """
            This method should always be called when exiting the app. If data needs
            to be saved, or the user needs to be asked for some action prior to exiting,
            here is where it should happen.
        """

        # Give the model a chance to make a clean exit.
        self.model.quit()

        # This line exits the application.
        QtWidgets.QApplication.quit()

    
    def calculate(self):
        a = self.view.mainwindow.spinBox_a.value()
        b = self.view.mainwindow.spinBox_b.value()
        result = self.model.add(a, b)

        self.view.mainwindow.label_Result.setText(str(result))

    
    def eraseResult(self):
        self.view.mainwindow.label_Result.setText('')