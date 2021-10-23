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

import sys
import logging

from PySide6 import QtWidgets

from .view.view import MyView
from .presenter.presenter import MyPresenter
from .model.model import MyModel

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# logger.setLevel(logging.WARNING)
# consolehandler = logging.StreamHandler()
# consolehandler.setLevel(logging.WARNING)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# consolehandler.setFormatter(formatter)
# logger.addHandler(consolehandler)

"""
    We have now initialized a simple logger.
    To learn more of how it works, or when and how to use it, study the logging module docs 
    (https://docs.python.org/3/howto/logging.html). 
    
    Here are some examples of how we will use it:
    logger.debug('Log this string: %s. And also log this number: %d.' % (aString, aNumber))
    logger.info('Log this string: %s.' % (aString, ))
    logger.warning('Log this.')
    logger.error('Log this string: %s.' % aString)
    logger.critical('Log this string: %s. And also log this number: %d. And another string: %s.' % (aString, aNumber, anotherString))

"""

def main():
    """
        Here we create the application, and start the Qt event loop. Observe that the model and view are
        created first, and that they do not have a reference to either each other or the presenter. This
        is by design. If the model och the view wishes to communicate with the presenter (or in rare cases
        with each other), theh have to use signals.
    """
    
    app = QtWidgets.QApplication(sys.argv)
    model = MyModel()
    view = MyView() 
    presenter = MyPresenter(model, view, app)
    sys.exit(app.exec_())

