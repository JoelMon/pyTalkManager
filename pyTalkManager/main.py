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
    # TODO Implement DatabaseWindow features

    def __init__(self, parent=None):
        super(DatabaseWindow, self).__init__(parent)
        self.setupUi(self)


class BrotherWindow(QtGui.QDialog, gui.BrotherWindow.Ui_BrotherWindow):
    """
    Window for the end user to manage the list of brothers in the database.
    """

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


class CongregationWindow(QtGui.QDialog,
                         gui.CongregationWindow.Ui_CongregationWindow):
    """
    Window that allows the user to add, edit, and delete congregations to the
    database.

    Methods:

      populate_table - Get's all the congregations entered in the database and
      returns only their names. Then it populates the list_congregation
      QListWidget with the retrieved names.

      edit_congregation_window - Repurpose the AddCongregationWindow for
      editing congregation information.

      load_congregation_data - Submits user edits back to the database

      show_add_congregation_window - Opens the AddCongregationWindow

    """

    def __init__(self, parent=None):
        super(CongregationWindow, self).__init__(parent)
        self.setupUi(self)
        self.populate_table()

        self.button_add.clicked.connect(self.show_add_congregation_window)
        self.button_edit.clicked.connect(self.edit_congregation_window)


    def populate_table(self):
        """
        Populates the congregation table so the user may select a congregation already entered into the database.
        """
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

        self.show_edit = EditCongregationDialog(selection)  # Pass the index of the user selection.
        self.show_edit.show()


    def show_add_congregation_window(self):
        """Window that allows the user enter a new congregation into the database"""

        self.add_cong_window = AddCongregationWindow()
        self.add_cong_window.show()


class AddCongregationWindow(QtGui.QDialog,
                            gui.AddCongregationWindow.Ui_AddCongregationWindow):
    """
    Window to allow the user to enter a new congregation into the database.

    Methods:
      new_congregation - Takes care of collecting user entered information
      and submitting it to Congregation.add_congregation where it will be
      checked for various things before being sent to the db module for
      inserting into the database.
    """


    def __init__(self, parent=None):
        super(AddCongregationWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_add.clicked.connect(self.new_congregation)


    def new_congregation(self):
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
        week = "week"
        time = "time"
        latitude = self.line_latitude.displayText()
        longitude = self.line_longitude.displayText()
        notes = self.text_note.toPlainText()
        visibility = 'True'

        new_congregation = Congregation()
        new_congregation.set_attributes(name, phone, email, address, city,
                                        state, zipcode, week, time, longitude,
                                        latitude, notes, visibility)
        new_congregation.add_congregation()


class EditCongregationDialog(QtGui.QDialog,
                             gui.AddCongregationWindow.Ui_AddCongregationWindow):
    # TODO: implement this class fully.

    # index is the user selected congregation
    def __init__(self, index, parent=None):
        super(EditCongregationDialog, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Edit Congregation")
        self.button_add.setText("Save")

        all_congregations = Congregation.get_entries(None)

        self.button_add.clicked.connect(lambda: self.submit_edit(all_congregations[index][0]))

        # load information of selected congregation into the dialog
        self.line_name.setText(str(all_congregations[index][1]))
        self.line_phone.setText(str(all_congregations[index][2]))
        self.line_email.setText(str(all_congregations[index][3]))
        self.line_address.setText(str(all_congregations[index][4]))
        self.line_city.setText(str(all_congregations[index][5]))
        self.line_state.setText(str(all_congregations[index][6]))
        self.line_zipcode.setText(str(all_congregations[index][7]))
        # select the correct radio box
        # self.timeEdit
        self.line_longitude.setText(str(all_congregations[index][8]))
        self.line_latitude.setText(str(all_congregations[index][9]))
        self.text_note.setText(str(all_congregations[index][10]))


    def submit_edit(self, row):
        """
        Method that submits user made edits to be committed to the database.

        All the fields are submitted to the
        Congregation.edit_congregation method which will do various
        checks such as make sure all required fields are entered. Then
        from there it is passed off to the db module that will cause
        the database to be modified.

        :param row: The row being modified.
        """

        name = self.line_name.displayText()
        phone = self.line_phone.displayText()
        email = self.line_email.displayText()
        address = self.line_address.displayText()
        city = self.line_city.displayText()
        state = self.line_state.displayText()
        zipcode = self.line_zipcode.displayText()
        week = "week"
        time = "time"
        latitude = self.line_latitude.displayText()
        longitude = self.line_longitude.displayText()
        notes = self.text_note.toPlainText()
        visibility = "True"

        edit_congregation = Congregation()
        edit_congregation.set_attributes(name, phone, email, address, city,
                                         state, zipcode, week, time, longitude,
                                         latitude, notes, visibility)
        edit_congregation.edit_congregation(row)
        self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())
