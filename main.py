import sys
from PyQt5 import QtWidgets, uic, QtCore
import sqlite3
import pandas as pd
import functions as f

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
gui9 = uic.loadUiType('delay_menu.ui')[0]
gui10 = uic.loadUiType('gateclosure_menu.ui')[0]
gui11 = uic.loadUiType('cancelledflight_menu.ui')[0]
gui12 = uic.loadUiType('maintenance_menu.ui')[0]

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

        self.instructions_menu = InstructionsWindow(self)
        self.variables_menu = VariablesWindow(self)
        self.amendflights_menu = AmendWindow(self)
        self.clearflights_menu = ClearWindow(self)

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

        self.schedule_table.clearContents()
        self.schedule_table.setRowCount(100)
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
        self.parent = parent

        self.delay_menu = DelayFlightsWindow(self)
        self.gateclosure_menu = GateClosureWindow(self)
        self.cancelledflight_menu = CancelledFlightsWindow(self)
        self.maintenance_menu = MaintenanceWindow(self)

        self.delay_button.clicked.connect(self.delay_connect)
        self.gateclosure_button.clicked.connect(self.gateclosure_connect)
        self.cancelled_button.clicked.connect(self.cancelledflight_connect)
        self.maintenance_button.clicked.connect(self.maintenance_connect)

    def delay_connect(self):
        '''
        connects the delay flights button click with opening the delay flights menu
        :return: showing the delay flights menu
        '''
        self.delay_menu.show()

    def gateclosure_connect(self):
        '''
        connects the gate closure button click with opening the gate closure  menu
        :return: showing the gate closure menu
        '''
        self.gateclosure_menu.show()

    def cancelledflight_connect(self):
        '''
        connects the cancelled flight button click with opening the cancelled flight menu
        :return: showing the cancelled flight menu
        '''
        self.cancelledflight_menu.show()

    def maintenance_connect(self):
        '''
        connects the maintenance button click with opening the maintenance menu
        :return: showing the maintenance menu
        '''
        self.maintenance_menu.show()

# this class creates the amend flights window
class AmendWindow(QtWidgets.QMainWindow, gui4):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.addflights_menu = AddFlightsWindow(self)
        self.deleteflights_menu = DeleteFlightsWindow(self)
        self.editflights_menu = EditFlightsWindow(self)

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
        self.parent = parent

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
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        arrival = self.arrivaltime_input.text()
        departure = self.departuretime_input.text()
        prev_destination = self.prevdest_input.text()
        next_destination = self.nextdest_input.text()
        prev_flightnum = self.prevflightnum_input.text()
        next_flightnum = self.nextflightnum_input.text()
        gate_num = self.gatenum_input.text()

        data = (arrival, departure, prev_destination, next_destination, prev_flightnum, next_flightnum, gate_num)
        query = "INSERT INTO flightdata values(?,?,?,?,?,?,?)"
        cursor.execute(query, data)

        database_connect.commit()

        self.parent.parent.load_data()

        cursor.close()

        if database_connect:
            database_connect.close()

# this class creates the delete flights window
class DeleteFlightsWindow(QtWidgets.QMainWindow, gui7):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        self.flightnum_input.clear()

    def submit_connect(self):
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        arrival = self.arrivaltime_input.text()
        prev_flightnum = self.prevflightnum_input.text()

        data = (arrival, prev_flightnum)
        query = ''' 
        DELETE FROM flightdata 
        WHERE "Arrival Time" = (?) 
        AND "Previous Flight Number" = (?) '''
        cursor.execute(query, data)

        database_connect.commit()

        self.parent.parent.load_data()

        for row in cursor.execute('SELECT * FROM flightdata'):
            print(row)

        cursor.close()

        if database_connect:
            database_connect.close()

# this class creates the edit flights window
class EditFlightsWindow(QtWidgets.QMainWindow, gui8):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

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
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        arrival = self.arrivaltime_input.text()
        departure = self.departuretime_input.text()
        prev_destination = self.prevdest_input.text()
        next_destination = self.nextdest_input.text()
        prev_flightnum = self.prevflightnum_input.text()
        next_flightnum = self.nextflightnum_input.text()
        gate_num = self.gatenum_input.text()

        # !!!THIS NEEDS TO BE FOR EDIT FLIGHT - CURRENTLY COPIED FROM ADD FLIGHT!!!
        #data = (arrival, departure, prev_destination, next_destination, prev_flightnum, next_flightnum, gate_num)
        #query = "INSERT INTO flightdata values(?,?,?,?,?,?,?)"
        #cursor.execute(query, data)

        database_connect.commit()

        self.parent.parent.load_data()

        cursor.close()

        if database_connect:
            database_connect.close()

# this class creates the delay flights window
class DelayFlightsWindow(QtWidgets.QMainWindow, gui9):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        self.flightnum_input.clear()
        self.arrivaltime_input.clear()
        self.delaytime_input.clear()

    def submit_connect(self):
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        #delay = self.delaytime_input.text()
        #arrival_time = self.arrivaltime_input.text()
        #flight_num = self.flightnum_input.text()

        delay = '30'
        arrival_time = '09:30'
        flight_num = 'BA9669'

        # this gets the departure time from the table
        departure_query = '''
            SELECT "Departure Time"
            FROM flightdata
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''
        departure_data = (arrival_time, flight_num)
        cursor.execute(departure_query, departure_data)

        for row in cursor.execute(departure_query, departure_data):
            departure_time = (row[0])

        # updates database with new arrival time with the delay
        arrival_query = '''
            UPDATE flightdata
            SET "Arrival Time" = (?)
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''
        arrival_data = (f.delay_changetime(delay, arrival_time), arrival_time, flight_num)
        cursor.execute(arrival_query, arrival_data)

        # updates database with new departure time with the delay
        departure_update_query = '''
            UPDATE flightdata
            SET "Departure Time" = (?)
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''
        departure_update_data = (f.delay_changetime(delay, departure_time), f.delay_changetime(delay, arrival_time), flight_num)
        cursor.execute(departure_update_query, departure_update_data)

        # gets the gate number of any flights that arrive at the same time
        gatenum_delay = '''
            SELECT "Gate Number"
            FROM flightdata
            WHERE "Arrival Time" = (?)
            AND "Previous Flight Number" = (?)'''

        turnaround = (f.time_convertmin(f.delay_changetime(delay, departure_time)) -
                      f.time_convertmin(f.delay_changetime(delay, arrival_time)))

        #print(arrival_time)

        for i in range(0, turnaround):
            if len(str(i)) == 1:
                time_period = arrival_time[0] + arrival_time[1] + arrival_time[2] + arrival_time[3] + str(i)
                #print(time_period)
                print(f.delay_changetime(delay, time_period))
                print()
                data_gatenum = (f.delay_changetime(delay, time_period), flight_num)
                cursor.execute(gatenum_delay, data_gatenum)
                #for row in cursor.execute(gatenum_delay, data_gatenum):
                    #print(row)
            else:
                time_period = arrival_time[0] + arrival_time[1] + arrival_time[2] + str(i)[0] + str(i)[1]
                #print(time_period)
                print(f.delay_changetime(delay, time_period))
                print()
                data_gatenum = (f.delay_changetime(delay, time_period), flight_num)
                cursor.execute(gatenum_delay, data_gatenum)
               # for row in cursor.execute(gatenum_delay, data_gatenum):
                #    print(row)

        # !! NEED TO CHECK FUNCTION TO WHY IT IS SWAPPING HOURS WHICH IS ERROR AND WHY SECOND GATE HAS NOT BEEN FOUND!!

        # these are the gates available at the terminal
        gates = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

        # this compares and sees if a gate is available or not at the allocated time
        for row in cursor.execute(gatenum_delay, data_gatenum):
            #print(row)
            if row:
                for i in range(0, len(gates)):
                    for j in range(len(row)):
                        if gates[i] != row[0]:
                            # updates database with new gate number
                            updategates_query = '''
                                UPDATE flightdata
                                SET "Gate Number" = (?)
                                WHERE "Arrival Time" = (?)
                                AND "Previous Flight Number" = (?)'''
                            updategates_data = (gates[i], f.delay_changetime(delay, arrival_time), 'BA9669')
                            cursor.execute(updategates_query, updategates_data)

                            break
                        else:
                            None

        database_connect.commit()

        self.parent.parent.load_data()

        #for row in cursor.execute('SELECT * FROM flightdata'):
         #   print(row)

        cursor.close()

        if database_connect:
            database_connect.close()

# this class creates the gate closure flights window
class GateClosureWindow(QtWidgets.QMainWindow, gui10):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the cancelled flights window
class CancelledFlightsWindow(QtWidgets.QMainWindow, gui11):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the maintenance flights window
class MaintenanceWindow(QtWidgets.QMainWindow, gui12):
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