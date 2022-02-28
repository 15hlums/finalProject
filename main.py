import sys
from PyQt5 import QtWidgets, uic, QtCore
import sqlite3
import pandas as pd

# creates a database from excel file
database = sqlite3.connect('flightdata.db')
def import_excel_to_database(database):
        excel_read = pd.read_excel('FlightData.xlsx', sheet_name='Sheet1', index_col=0)
        excel_read.to_sql(name='flightdata', con=database, if_exists='replace', index=0)
        database.commit()
import_excel_to_database(database)

# this imports the designs from QT Designer
gui1 = uic.loadUiType('pyqt_design.ui')[0]
gui2 = uic.loadUiType('instructions_menu.ui')[0]
gui3 = uic.loadUiType('variables_menu.ui')[0]
gui4 = uic.loadUiType('amendflights_menu.ui')[0]
gui5 = uic.loadUiType('clearflights_menu.ui')[0]
gui6 = uic.loadUiType('addflights_menu.ui')[0]
gui7 = uic.loadUiType('deleteflights_menu.ui')[0]
gui8 = uic.loadUiType('editflights_menu.ui')[0]

# this class creates the main schedule window
class ScheduleWindow(QtWidgets.QMainWindow, gui1):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # set column width for table
        self.schedule_table.setColumnWidth(0,90)
        self.schedule_table.setColumnWidth(1, 90)
        self.schedule_table.setColumnWidth(2, 125)
        self.schedule_table.setColumnWidth(3, 125)
        self.schedule_table.setColumnWidth(4, 125)
        self.schedule_table.setColumnWidth(5, 125)
        self.schedule_table.setColumnWidth(6, 80)
        self.load_data()

        self.instructions_menu = InstructionsWindow()
        self.variables_menu = VariablesWindow()
        self.amendflights_menu = AmendWindow()
        self.clearflights_menu = ClearWindow()

        self.instructions_button.clicked.connect(self.instructions_connect)
        self.variables_button.clicked.connect(self.variables_connect)
        self.amend_button.clicked.connect(self.amend_connect)
        self.clear_button.clicked.connect(self.clear_connect)

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

    def amend_connect(self):
        '''
        connects the amend flights button click with opening the amend flights menu
        :return: showing the amend flights menu
        '''
        self.amendflights_menu.show()

    def clear_connect(self):
        '''
        connects the clear flights button click with opening the clear flights menu
        :return: showing the clear flights menu
        '''
        self.clearflights_menu.show()

    def load_data(self):
        cur = database.cursor()
        sqlquery = 'SELECT * FROM flightdata LIMIT 100'

        self.schedule_table.setRowCount(5)
        tablerow = 0
        for row in cur.execute(sqlquery):
            self.schedule_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.schedule_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.schedule_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.schedule_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.schedule_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.schedule_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.schedule_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))

            tablerow += 1

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

# this class creates the amend flights window
class AmendWindow(QtWidgets.QMainWindow, gui4):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.addflights_menu = AddFlightsWindow()
        self.deleteflights_menu = DeleteFlightsWindow()
        self.editflights_menu = EditFlightsWindow()

        self.addflights_button.clicked.connect(self.addflights_connect)
        self.deleteflights_button.clicked.connect(self.deleteflights_connect)
        self.editflights_button.clicked.connect(self.editflights_connect)

    def addflights_connect(self):
        '''
        connects the add flights button click with opening the add flights menu
        :return: showing the add flights menu
        '''
        self.addflights_menu.show()

    def deleteflights_connect(self):
        '''
        connects the delete flights button click with opening the delete flights menu
        :return: showing the delete flights menu
        '''
        self.deleteflights_menu.show()

    def editflights_connect(self):
        '''
        connects the edit flights button click with opening the edit flights menu
        :return: showing the edit flights menu
        '''
        self.editflights_menu.show()

# this class creates the clear flights window
class ClearWindow(QtWidgets.QMainWindow, gui5):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the add flights window
class AddFlightsWindow(QtWidgets.QMainWindow, gui6):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        self.arrivaltime_input.clear()
        self.departuretime_input.clear()
        self.prevdest_input.clear()
        self.nextdest_input.clear()
        self.prevflightnum_input.clear()
        self.nextflightnum_input.clear()
        self.gatenum_input.clear()

    def submit_connect(self):

        try:
            database_connect = sqlite3.connect('flightdata.db')
            cursor = database_connect.cursor()
            print("connected to database")

            sqlite_insert_query = """INSERT INTO flightdata
                                  (Arrival Time, Departure Time, Previous Destination, Next Destination, 
                                  Previous Flight Number, Next Flight Number, Gate Number) 
                                   VALUES 
                                  ('09:00','09:40','New York','Bahamas','BA345', 'BA123', 'C4')"""

            count = cursor.execute(sqlite_insert_query)
            database_connect.commit()
            print("inserted into flightdata table ", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("did not insert data into table", error)
        finally:
            if database_connect:
                database_connect.close()
                print("The database connection is closed")

class DeleteFlightsWindow(QtWidgets.QMainWindow, gui7):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the edit flights window
class EditFlightsWindow(QtWidgets.QMainWindow, gui8):
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
