import sys
from PyQt5 import QtWidgets, uic, QtCore
import sqlite3
import functions as f

# creates a database from excel file
database = sqlite3.connect('flightdata.db')
f.import_excel_to_database(database)

# this imports the designs from QT Designer
gui1 = uic.loadUiType('pyqt_design.ui')[0]
gui2 = uic.loadUiType('instructions_menu.ui')[0]
gui3 = uic.loadUiType('variables_menu.ui')[0]
gui4 = uic.loadUiType('amendflights_menu.ui')[0]
gui5 = uic.loadUiType('filterflights_menu.ui')[0]
gui6 = uic.loadUiType('addflights_menu.ui')[0]
gui7 = uic.loadUiType('deleteflights_menu.ui')[0]
gui8 = uic.loadUiType('editflights_menu.ui')[0]
gui9 = uic.loadUiType('delay_menu.ui')[0]
gui10 = uic.loadUiType('gateclosure_menu.ui')[0]
gui11 = uic.loadUiType('cancelledflight_menu.ui')[0]
gui12 = uic.loadUiType('extendedturnaround_menu.ui')[0]
gui13 = uic.loadUiType('exturnover2_menu.ui')[0]
gui14 = uic.loadUiType('rescheduleflight_menu.ui')[0]

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
        self.clearflights_menu = FilterWindow(self)

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
        '''
        this loads the data from the database into the main GUI table
        :return: GUI which displays data from database
        '''
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

# this class creates the instructions window !!NOT DONE!!
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
        self.extendedturnaround_menu = ExtendedTurnaroundWindow(self)

        self.delay_button.clicked.connect(self.delay_connect)
        self.gateclosure_button.clicked.connect(self.gateclosure_connect)
        self.cancelled_button.clicked.connect(self.cancelledflight_connect)
        self.maintenance_button.clicked.connect(self.extendedturnaround_connect)

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

    def extendedturnaround_connect(self):
        '''
        connects the maintenance button click with opening the maintenance menu
        :return: showing the maintenance menu
        '''
        self.extendedturnaround_menu.show()

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

# this class creates the filter flights window
class FilterWindow(QtWidgets.QMainWindow, gui5):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)
        self.resetbutton.clicked.connect(self.reset_connect)

    def clear_connect(self):
        '''
        clears the buttons in the GUI
        '''
        self.arrivaltime_input.clear()
        self.departuretime_input.clear()
        self.prevdest_input.clear()
        self.nextdest_input.clear()
        self.gatenum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then adds the information into the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        #arrival = self.arrivaltime_input.text()
        #departure = self.departuretime_input.text()
        #prevdest = self.prevdest_input.text()
        #nextdest = self.nextdest_input.text()
        #gatenum = self.gatenum_input.text()

        arrival = '09:30'
        departure = 'None'
        prevdest = 'None'
        nextdest = 'None'
        gatenum = 'None'

        filter_list = []
        filter_names = []
        filter_data = []

        if arrival != 'None':
            filter_list.clear()
            filter_list.append(arrival)
            filter_data.append(arrival)
            filter_names.append('arrival')
            filter_data = tuple(filter_list)

            filterarrival_query = '''
            SELECT *
            FROM flightdata
            WHERE "Arrival Time" LIKE (?) '''

            cursor.execute(filterarrival_query, filter_data)

        if departure != 'None':
            filter_list.clear()
            filter_list.append(departure)
            filter_data.append(departure)
            filter_data.append('departure')
            filter_data = tuple(filter_list)

            filterdeparture_query = '''
            SELECT *
            FROM flightdata
            WHERE "Departure Time" LIKE (?) '''

            cursor.execute(filterdeparture_query, filter_data)

        if prevdest != 'None':
            filter_list.clear()
            filter_list.append(prevdest)
            filter_data.append(prevdest)
            filter_names.append('prevdest')
            filter_data = tuple(filter_list)

            filterprevdest_query = '''
            SELECT *
            FROM flightdata
            WHERE "Previous Destination" LIKE (?) '''

            cursor.execute(filterprevdest_query, filter_data)

        if nextdest != 'None':
            filter_list.clear()
            filter_list.append(nextdest)
            filter_data.append(nextdest)
            filter_names.append('nextdest')
            filter_data = tuple(filter_list)

            filternextdest_query = '''
            SELECT *
            FROM flightdata
            WHERE "Nest Destination" LIKE (?) '''

            cursor.execute(filternextdest_query, filter_data)

        if gatenum != 'None':
            filter_list.clear()
            filter_list.append(gatenum)
            filter_data.append(gatenum)
            filter_names.append('gatenum')
            filter_data = tuple(filter_list)

            filtergatenum_query = '''
            SELECT *
            FROM flightdata
            WHERE "Gate Number" LIKE (?) '''

            cursor.execute(filtergatenum_query, filter_data)

        print(len(filter_names))
        print(filter_data)

        f.filter_deleterows(filter_names, filter_data)

        database_connect.commit()

        self.parent.load_data()

        cursor.close()

        if database_connect:
            database_connect.close()

    def reset_connect(self):
        database = sqlite3.connect('flightdata.db')
        f.import_excel_to_database(database)
        self.parent.load_data()

# this class creates the add flights window
class AddFlightsWindow(QtWidgets.QMainWindow, gui6):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears the buttons in the GUI
        '''
        self.arrivaltime_input.clear()
        self.departuretime_input.clear()
        self.prevdest_input.clear()
        self.nextdest_input.clear()
        self.prevflightnum_input.clear()
        self.nextflightnum_input.clear()
        self.gatenum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then adds the information into the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
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
        '''
        clears the data in the gui buttons
        '''
        self.flightnum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then deletes the relevant row from the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
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

        cursor.close()

        if database_connect:
            database_connect.close()

# this class creates the edit flights window !!NOT DONE!!
class EditFlightsWindow(QtWidgets.QMainWindow, gui8):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears the data from the gui buttons
        '''
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

# this class creates the delay flights window !!GATE COLLISION AVOIDANCE NOT WORKING!!
class DelayFlightsWindow(QtWidgets.QMainWindow, gui9):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears data from the gui buttons
        '''
        self.flightnum_input.clear()
        self.arrivaltime_input.clear()
        self.delaytime_input.clear()

    def submit_connect(self):
        '''
        takes input from the gui buttons and changes the time from the relevant delay amount and updates database and
        gui with the new times and gate numbers
        :return: updated database and gui
        '''
        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        delay = self.delaytime_input.text()
        arrival_time = self.arrivaltime_input.text()
        flight_num = self.flightnum_input.text()

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

        data_gatenum = (f.delay_changetime(delay, arrival_time), flight_num)
        cursor.execute(gatenum_delay, data_gatenum)

        # these are the gates available at the terminal
        gates = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

        # this compares and sees if a gate is available or not at the allocated time
        for row in cursor.execute(gatenum_delay, data_gatenum):
            if row:
                for i in range(0, len(gates)):
                    if gates[i] != row[0]:
                        # updates database with new gate number
                        updategates_query = '''
                            UPDATE flightdata
                            SET "Gate Number" = (?)
                            WHERE "Arrival Time" = (?)
                            AND "Previous Flight Number" = (?)'''
                        updategates_data = (gates[i], f.delay_changetime(delay, arrival_time), flight_num)
                        cursor.execute(updategates_query, updategates_data)

                        break
                    else:
                        None

        database_connect.commit()

        self.parent.parent.load_data()

        cursor.close()

        if database_connect:
            database_connect.close()

# this class creates the gate closure flights window !!NOT DONE!!
class GateClosureWindow(QtWidgets.QMainWindow, gui10):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the cancelled flights window !!NOT DONE!!
class CancelledFlightsWindow(QtWidgets.QMainWindow, gui11):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

# this class creates the extended turnarounds window
class ExtendedTurnaroundWindow(QtWidgets.QMainWindow, gui12):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.submitbutton.clicked.connect(self.submit_connect)
        self.clearbutton.clicked.connect(self.clear_connect)

    def clear_connect(self):
        '''
        this clears the buttons on the gui
        '''
        self.flightnum_input.clear()
        self.arrivaltime_input.clear()
        self.esttime_input.clear()

    def submit_connect(self):
        #estimated_time = self.esttime_input.text()

        estimated_time = '02:00'

        if float(estimated_time[1]) < 2.00 and float(estimated_time[1]) >= 0.00:
            self.less_2hours()
        elif float(estimated_time[1]) >= 2.00:
            self.more_2hours()
        else:
            None

    def less_2hours(self):
        '''
        when the extended turnaround is less than 2 hours, it will just delay the flight by the specified time
        :return: new times and gate numbers in the gui table
        '''

        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        flight_num = self.flightnum_input.text()
        arrival_time = self.arrivaltime_input.text()
        estimated_time = self.esttime_input.text()

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
        arrival_data = (f.delay_changetime(estimated_time, arrival_time), arrival_time, flight_num)
        cursor.execute(arrival_query, arrival_data)

        # updates database with new departure time with the delay
        departure_update_query = '''
                    UPDATE flightdata
                    SET "Departure Time" = (?)
                    WHERE "Arrival Time" = (?)
                    AND "Previous Flight Number" = (?)'''
        departure_update_data = (
        f.delay_changetime(estimated_time, departure_time), f.delay_changetime(estimated_time, arrival_time), flight_num)
        cursor.execute(departure_update_query, departure_update_data)

        # gets the gate number of any flights that arrive at the same time
        gatenum_delay = '''
                    SELECT "Gate Number"
                    FROM flightdata
                    WHERE "Arrival Time" = (?)
                    AND "Previous Flight Number" = (?)'''

        data_gatenum = (f.delay_changetime(estimated_time, arrival_time), flight_num)
        cursor.execute(gatenum_delay, data_gatenum)

        # these are the gates available at the terminal
        gates = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

        # this compares and sees if a gate is available or not at the allocated time
        for row in cursor.execute(gatenum_delay, data_gatenum):
            if row:
                for i in range(0, len(gates)):
                    if gates[i] != row[0]:
                        # updates database with new gate number
                        updategates_query = '''
                                    UPDATE flightdata
                                    SET "Gate Number" = (?)
                                    WHERE "Arrival Time" = (?)
                                    AND "Previous Flight Number" = (?)'''
                        updategates_data = (gates[i], f.delay_changetime(estimated_time, arrival_time), flight_num)
                        cursor.execute(updategates_query, updategates_data)

                        break
                    else:
                        None

        database_connect.commit()

        self.parent.parent.load_data()

        cursor.close()

        if database_connect:
            database_connect.close()

    def more_2hours(self):
        '''
        opens a new window which gives the user two options to either cancel or reschedule the flight as the extended
        turnaround is too long
        :return: opens exturnover2 window
        '''

        self.exturnover2_menu = ExtendedTurnaroundOverTwoWindow(self)
        self.exturnover2_menu.show()

# this class creates a window when the extended turnarounds is equal to or greater than 2 hours
class ExtendedTurnaroundOverTwoWindow(QtWidgets.QMainWindow, gui13):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.submitbutton.clicked.connect(self.submit_connect)

    def submit_connect(self):
        if self.cancelbutton.isChecked() == True:
            self.cancel_connect()
        elif self.reschedulebutton.isChecked() == True:
            print('res')
            self.reschedule_connect()
        else:
            None

    def cancel_connect(self):
        '''
        this cancels the flight when the extended turnaround is over 2 hours
        :return: updated gui table
        '''

        database_connect = sqlite3.connect('flightdata.db')
        cursor = database_connect.cursor()

        flight_num = self.parent.flightnum_input.text()
        arrival_time = self.parent.arrivaltime_input.text()

        cancel_data = (arrival_time, flight_num)
        cancel_query = ''' 
        DELETE FROM flightdata 
        WHERE "Arrival Time" = (?) 
        AND "Previous Flight Number" = (?) '''
        cursor.execute(cancel_query, cancel_data)

        database_connect.commit()

        self.parent.parent.parent.load_data()

        cursor.close()

        if database_connect:
            database_connect.close()

    def reschedule_connect(self):
        self.rescheduleflight_menu = RescheduleFlightWindow(self)
        self.rescheduleflight_menu.show()

# this class creates a window when user wants to reschedule a flight when the ex. turnaround is greater/equal to 2 hours
class RescheduleFlightWindow(QtWidgets.QMainWindow, gui14):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent

        self.clearbutton.clicked.connect(self.clear_connect)
        self.submitbutton.clicked.connect(self.submit_connect)

    def clear_connect(self):
        '''
        clears the buttons in the GUI
        '''
        self.arrivaltime_input.clear()
        self.departuretime_input.clear()
        self.prevdest_input.clear()
        self.nextdest_input.clear()
        self.prevflightnum_input.clear()
        self.nextflightnum_input.clear()
        self.gatenum_input.clear()

    def submit_connect(self):
        '''
        takes in inputs from the gui buttons and then adds the information into the database and calls load_data()
        fucntion from parent class to upload to gui
        :return: updates data in database and uploads to gui
        '''
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