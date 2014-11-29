#!/usr/bin/env python3

import sys
from PySide import QtGui
import pyTalkManager as tm
from congregation import Congregation

# Importation of GUIs
import gui.MainWindow
import gui.DatabaseWindow
import gui.BrotherWindow
import gui.AddBrotherWindow
import gui.CongregationWindow
import gui.AddCongregationWindow


class MainWindow(QtGui.QMainWindow, gui.MainWindow.Ui_MainWindow):
    """The main window of pyTalkManager.

    From MainWindow all functions of pyTalkManager is accessed by the end user.

    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        tm.first_run_check()

        # Tool bar actions
        self.actionDatabase.triggered.connect(self.show_database_window)
        self.actionBrothers.triggered.connect(self.show_brother_window)
        self.actionCongregation.triggered.connect(self.show_congregation_window)

    def show_database_window(self):
        """Method that calls the Database Window"""

        self.db_window = DatabaseWindow()
        self.db_window.show()

    def show_brother_window(self):
        """Method that calls the Brother Window"""

        self.bro_window = BrotherWindow()
        self.bro_window.show()

    def show_congregation_window(self):
        """Method that calls the Congregation Window"""

        self.congregation_window = CongregationWindow()
        self.congregation_window.show()


class DatabaseWindow(QtGui.QDialog, gui.DatabaseWindow.Ui_DatabaseWindow):
    """
    Window for end user to manage pyTalkManager's database.

    Supported actions for the user:

      Create a new database
      Backup existing database to a new location
      Load an existing database

    At the moment non of the functionality are implemented.

    """


    def __init__(self, parent=None):
        super(DatabaseWindow, self).__init__(parent)
        self.setupUi(self)


class BrotherWindow(QtGui.QDialog, gui.BrotherWindow.Ui_BrotherWindow):
    """Window for the end user to manage the list of brothers in the database."""

    def __init__(self, parent=None):
        super(BrotherWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_add.clicked.connect(self.show_add_brother_window)


    def show_add_brother_window(self):
        self.add_bro_window = AddBrotherWindow()
        self.add_bro_window.show()


class AddBrotherWindow(QtGui.QDialog, gui.AddBrotherWindow.Ui_AddBrotherWindow):
    """

    Window for the end user to add brothers to the database.

    The window that opens when the user clicks on the 'Add'
    button in BrotherWindow()

    Methods:

      add_item() - Takes all widget information and stores it in a variable.
                   Currently the combo boxes and check boxes are not supported.

    """

    def __init__(self, parent=None):
        super(AddBrotherWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_add.clicked.connect(self.add_item)

    def add_item(self):
        first_name = self.line_f_name.displayText()
        middle_name = self.line_m_name.displayText()
        last_name = self.line_l_name.displayText()
        phone = self.line_phone.displayText()
        email = self.line_email.displayText()
        congregation = 'Congregation combo box'
        responsibility = 'Responsibility combo box'
        chairman = 'Chairman check box'
        speaker = 'Speaker check box'
        coordinator = 'Coordinator check box'
        note = self.text_note.toPlainText()

        columns = ['first_name', 'middle_name', 'last_name', 'phone', 'email',
                   'congregation', 'responsibility', 'chairman', 'speaker',
                   'coordinator', 'note']
        values = [first_name, middle_name, last_name, phone, email,
                  congregation, responsibility, chairman, speaker,
                  coordinator, note]


class CongregationWindow(QtGui.QDialog, gui.CongregationWindow.Ui_CongregationWindow):
    """
    Window that allows the user to add, edit, and delete congregations to the database.

    Methods:

      populate_table - Get's all the congregations entered in the database and returns
                       only their names. Then it populates the list_congregation QListWidget
                       with the retrieved names.

      edit_congregation_window - Repurpose the AddCongregationWindow for editing congregation
                                 information.

      load_congregation_data - Submits user edits back to the database

      show_add_congregation_window - Opens the AddCongregationWindow

    """

    def __init__(self, parent=None):
        super(CongregationWindow, self).__init__(parent)
        self.setupUi(self)
        self.populate_table()

        self.button_add.clicked.connect(self.show_add_congregation_window)
        self.button_edit.clicked.connect(self.edit_congregation_window)

    # Populate the congregation table
    def populate_table(self):
        list = Congregation.get_list(None)

        for item in list:
            self.list_congregation.addItem("{}".format(item[0]))


    def edit_congregation_window(self):
        """
        Opens the AddCongregationWindow, changes the title to
        'Edit Congregation', and populates the fields with data from
        the database. The user can edit any field and save it to the
        database.

        """

        all_congregations = Congregation.get_entries(None)
        selection = self.list_congregation.currentRow()

        self.show_edit = AddCongregationWindow()
        self.show_edit.show()
        self.show_edit.setWindowTitle("Edit Congregation")
        self.show_edit.button_add.setText('Save')  # Renamed 'Add' button to 'Save'
        self.show_edit.button_add.clicked.connect(lambda: self.load_congregation_data(all_congregations[selection][0]))

        # Fill all of the fields with the values from the database.
        # All the fields must be converted to string otherwise an error is raised.
        # Look more into the error.
        self.show_edit.line_name.setText(str(all_congregations[selection][1]))
        self.show_edit.line_phone.setText(str(all_congregations[selection][2]))
        self.show_edit.line_email.setText(str(all_congregations[selection][3]))
        self.show_edit.line_address.setText(str(all_congregations[selection][4]))
        self.show_edit.line_city.setText(str(all_congregations[selection][5]))
        self.show_edit.line_state.setText(str(all_congregations[selection][6]))
        self.show_edit.line_zipcode.setText(str(all_congregations[selection][7]))
        self.show_edit.line_longitude.setText(str(all_congregations[selection][8]))
        self.show_edit.line_latitude.setText(str(all_congregations[selection][9]))
        self.show_edit.text_note.setText(str(all_congregations[selection][10]))


    def load_congregation_data(self, row):
        """
        Method that submits user made edits to be committed to the database.

        All the fields are submitted to the
        Congregation.edit_congregation method which will do various
        checks such as make sure all required fields are entered. Then
        from there it is passed off to the db module that will cause
        the database to be modified.

        Variables:
          values - a list of all the values that can be edited by the user in
                   order.

        """


        name = self.show_edit.line_name.displayText()
        phone = self.show_edit.line_phone.displayText()
        email = self.show_edit.line_email.displayText()
        address = self.show_edit.line_address.displayText()
        city = self.show_edit.line_city.displayText()
        state = self.show_edit.line_state.displayText()
        zipcode = self.show_edit.line_zipcode.displayText()
        latitude = self.show_edit.line_latitude.displayText()
        longitude = self.show_edit.line_longitude.displayText()
        notes = self.show_edit.text_note.toPlainText()

        values = [name, phone, email, address, city,
                  state, zipcode, longitude, latitude, notes]

        Congregation.edit_congregation(None, values, row)
        self.show_edit.close()


    def show_add_congregation_window(self):
        """Window that allows the user enter a new congregation into the database"""

        self.add_cong_window = AddCongregationWindow()
        self.add_cong_window.show()


class AddCongregationWindow(QtGui.QDialog, gui.AddCongregationWindow.Ui_AddCongregationWindow):
    """
    Window to allow the user to enter a new congregation into the database.

    Methods:
      add_item - Takes care of collecting user entered information and submitting
                 it to Congregation.add_congregation where it will be checked for
                 various things before being sent to the db module for inserting
                 into the database.

    """


    def __init__(self, parent=None):
        self.edit_mode = False
        super(AddCongregationWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_add.clicked.connect(self.add_item)


    def add_item(self):
        """
        Method to add information of a new congregation to
        the database.

        """

        name = self.line_name.displayText()
        phone = self.line_phone.displayText()
        email = self.line_email.displayText()
        address = self.line_address.displayText()
        city = self.line_city.displayText()
        state = self.line_state.displayText()
        zipcode = self.line_zipcode.displayText()
        latitude = self.line_latitude.displayText()
        longitude = self.line_longitude.displayText()
        notes = self.text_note.toPlainText()

        values = [name, phone, email, address, city,
                  state, zipcode, longitude, latitude, notes]

        # Passes the columns and values needed for adding a new
        # congregation to add_congregation. The add_congregation method
        # takes care of checking if all required fields have been
        # entered. If not, then it returns False with the error
        # otherwise it returns True.

        submission = Congregation.add_congregation(None, values)

        if submission is True:
            pass
        else:
            if submission[1] == "Error: duplicate":
                print(submission[2])  # debugging - Will replace with GUI
            elif submission[1] == "Error: Fields":
                print(submission[2])  # debugging - Will replace with GUI


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())
