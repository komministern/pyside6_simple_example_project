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

from .main.mainpresenter import MainPresenter

logger = logging.getLogger(__name__)

class MyPresenter(QtCore.QObject):
    """
        The Presenter object contains the intelligence of the GUI. That is, here
        resides the interactions between the widgets in the View object. The Presenter
        acts upon signals sent from both the View and the Model.

        The Presenter object has access to both the View and Model objects, so its
        actions takes the form of method calls to these.
    """

    def __init__(self, model, view, app):
        super(MyPresenter, self).__init__()

        # Store view, model and app.
        self.model = model
        self.view = view
        self.app = app
    
        self.mainpresenter = MainPresenter(model, view, app)

        self.connectSignals()

        self.view.mainwindow.show()

    def connectSignals(self):
        """
            Here we can possibly connect all signals that are emitted from the model. This
            way it would be easier to read the program. But this is only profitable if
            there are multiple presenters, not just the main one.
        """
        pass

    
    

        