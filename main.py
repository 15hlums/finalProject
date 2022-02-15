import sys
from PyQt5 import QtWidgets, uic, QtCore

# this imports the designs from QT Designer
gui1 = uic.loadUiType('pyqt_design.ui')[0]
gui2 = uic.loadUiType('instructions_menu.ui')[0]
gui3 = uic.loadUiType('variables_menu.ui')[0]

# this class creates the main schedule window
class ScheduleWindow(QtWidgets.QMainWindow, gui1):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.instructions_menu = InstructionsWindow()
        self.variables_menu = VariablesWindow()

        self.instructions_button.clicked.connect(self.instructions_connect)
        self.variables_button.clicked.connect(self.variables_connect)

    def instructions_connect(self):
        '''
        connects the instructions button click with opening the instructions menu
        :return: showing the instructions menu
        '''
        self.instructions_menu.show()

    def variables_connect(self):
        '''
        connects the variables button click with opening the variables menu
        :return: showing the variables menu
        '''
        self.variables_menu.show()

# this class creates the instructions window
class InstructionsWindow(QtWidgets.QMainWindow, gui2):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the variables window
class VariablesWindow(QtWidgets.QMainWindow, gui3):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this function creates objects from the class that opens the main window
def main():
    # this resizes the window to fit with it's contents
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    main_window = ScheduleWindow()
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
