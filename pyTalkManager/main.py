#!/usr/bin/env python3

import sys
from PySide import QtGui, QtCore
import pyTalkManager as tm
from congregation import Congregation
from db import DB
from brother import Brother


# Importation of GUIs
import gui.MainWindow
import gui.DatabaseWindow
import gui.BrotherWindow
import gui.AddBrotherWindow
import gui.CongregationWindow
import gui.AddCongregationWindow


class MainWindow(QtGui.QMainWindow, gui.MainWindow.Ui_MainWindow):
    """
    The main window of pyTalkManager.

    From MainWindow all functions of pyTalkManager is accessed by the end user.

    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.center_on_screen()
        tm.first_run_check()

        # Tool bar actions
        self.actionDatabase.triggered.connect(self.show_database_window)
        self.actionBrothers.triggered.connect(self.show_brother_window)
        self.actionCongregation.triggered.connect(self.show_congregation_window)

    def center_on_screen(self):
        """
        Center the window on the user's screen.

        """

        screen_resolution = QtGui.QDesktopWidget().screenGeometry()

        center_horizontal = ((screen_resolution.width() / 2) -
                             (self.frameSize().width() / 2))

        center_vertical = ((screen_resolution.height() / 2) -
                           (self.frameSize().height() / 2))

        self.move(center_horizontal, center_vertical)


    def show_database_window(self):
        """
        Method that calls the Database Window

        """

        self.db_window = DatabaseWindow()
        self.db_window.show()


    def show_brother_window(self):
        """
        Method that calls the Brother Window

        """

        self.bro_window = BrotherWindow()
        self.bro_window.show()


    def show_congregation_window(self):
        """
        Method that calls the Congregation Window

        """

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
    """
    Window for the end user to manage the list of brothers in the database.

    """
    brother_id_sorted = []  # Brother ids in correct sorting order.


    def __init__(self, parent=None):
        super(BrotherWindow, self).__init__(parent)
        self.setupUi(self)
        self.populate_cong()
        self.sorted_list = None
        self.options_selected = {"Name": "first_name", "Resp": "NOT NULL",
                                 "Coord": "NOT NULL", "Cong": "NOT NULL"}
        self.populate_brothers(self.options_selected)

        self.button_add.clicked.connect(self.show_add_brother_window)
        self.tableWidget.doubleClicked.connect(self.show_edit_brother_window)
        self.button_edit.clicked.connect(self.show_edit_brother_window)
        self.tableWidget.resizeColumnsToContents()
        # Sorting of brothers
        self.radio_fname.clicked.connect(self.clicked_button)
        self.radio_l_name.clicked.connect(self.clicked_button)
        self.radio_all.clicked.connect(self.clicked_button)
        self.radio_coord.clicked.connect(self.clicked_button)
        self.radio_elder.clicked.connect(self.clicked_button)
        self.radio_ms.clicked.connect(self.clicked_button)
        self.radio_pub.clicked.connect(self.clicked_button)
        self.combo_cong.currentIndexChanged.connect(self.clicked_button)

    def clicked_button(self):
        """
        Determins which radio buttons have been selected and adds the
        selected radio buttons to the dictionary 'options_selected'. Then it
        calls the populate_cong method and passes the options_selected dic so
        that the table can be sorted using the parameters included in
        options_selected.

        :return: None
        """

        if self.radio_fname.isChecked():
            self.options_selected["Name"] = "first_name"
        else:
            self.options_selected["Name"] = "last_name"

        if self.radio_all.isChecked():
            self.options_selected["Resp"] = "NOT NULL"
            self.options_selected["Coord"] = "NOT NULL"
        elif self.radio_coord.isChecked():
            self.options_selected["Resp"] = "NOT NULL"
            self.options_selected["Coord"] = '"True"'
        elif self.radio_elder.isChecked():
            self.options_selected["Resp"] = '"Elder"'
            self.options_selected["Coord"] = "NOT NULL"
        elif self.radio_ms.isChecked():
            self.options_selected["Resp"] = '"Ministerial Servant"'
            self.options_selected["Coord"] = "NOT NULL"
        elif self.radio_pub.isChecked():
            self.options_selected["Resp"] = '"Publisher"'
            self.options_selected["Coord"] = "NOT NULL"

        if self.combo_cong.currentText() == "All":
            self.options_selected["Cong"] = "NOT NULL"
        else:
            self.options_selected["Cong"] = \
                '"{}"'.format(self.combo_cong.currentText())
        self.populate_brothers(self.options_selected)

    def populate_brothers(self, option_dic):
        """
        Populates the brother item_list
        """

        self.tableWidget.setColumnCount(2)
        bro = Brother()
        sort_name = option_dic["Name"]
        resp = option_dic["Resp"]
        coord = option_dic["Coord"]
        cong = option_dic["Cong"]
        self.tableWidget.clearContents()

        item_list = bro.populate_table(sort_name, resp, coord, cong)
        item_list = (list(enumerate(item_list)))
        self.tableWidget.setRowCount(len(item_list))

        # Set the list of brothers onto the table.
        brother_ids = []  # IDs of the brothers entered in the DB.
        for item in item_list:
            brother_ids.append(item[1][0])
            # First, middle, and last name.
            name = QtGui.QTableWidgetItem("{} {} {}".format(item[1][1],
                                                            item[1][2],
                                                            item[1][3]))

            congregation = QtGui.QTableWidgetItem("{Cong}".format(Cong=item[1][
                4]))

            self.tableWidget.setItem(int(item[0]), 0, name)
            self.tableWidget.setItem(int(item[0]), 1, congregation)

        # Return all of the brother database ids in the correct order based
        # on the sort applied to BrotherWinow.brother_id_sorted.
        BrotherWindow.brother_id_sorted = brother_ids

    def populate_cong(self):
        """
        Populate the congregation combo box with all the names from
        congregations already entered into the database.

        """

        congregations = Congregation.get_list(None, 'ASC')
        self.sorted_list = congregations
        # Adds 'All' to the top of the combo box with the index of 0 so that
        # it can be used with a conditional to determine if sorting wants all
        # congregation to be included.
        self.sorted_list.insert(0, (0, 'All'))

        for congregation in congregations:
            self.combo_cong.addItem(congregation[1])

    def show_add_brother_window(self):
        self.add_bro_window = AddBrotherWindow()
        # If the user saves a new congregation, run populate_table()
        saved = self.add_bro_window.exec_()
        if saved:
            self.populate_brothers()

    def show_edit_brother_window(self):
        self.id_brother()
        self.edit_bro_window = EditBrotherWindow(self.id_brother())
        # If the user saves a new congregation, run populate_table()
        saved = self.edit_bro_window.exec_()
        if saved:
            self.clicked_button()

    def id_brother(self):
        """
        Return the id of the brother selected.

        :returns: The database id of the brother selected
        """

        selected_brother = self.tableWidget.currentRow()
        brothers_id = BrotherWindow.brother_id_sorted
        return brothers_id[selected_brother]


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
        self.button_add.clicked.connect(self.add_brother)
        self.sorted_list = None
        self.populate_cong()

    def populate_cong(self):
        """
        Populate the congregation combo box with all the names from
        congregations already entered into the database.

        """

        congregations = Congregation.get_list(None, 'ASC')
        self.sorted_list = congregations

        for congregation in congregations:
            self.combo_congregation.addItem(congregation[1])

    def add_brother(self):

        chairman = ''
        speaker = ''
        coordinator = ''

        first_name = self.line_f_name.displayText()
        middle_name = self.line_m_name.displayText()
        last_name = self.line_l_name.displayText()
        phone = self.line_phone.displayText()
        email = self.line_email.displayText()
        # Combo box
        selection = self.combo_congregation.currentIndex()
        congregation = self.sorted_list[selection][0]
        responsibility = self.combo_publisher.itemText(
            self.combo_publisher.currentIndex())
        # Capacity radio buttons
        if self.check_chairman.isChecked():
            chairman = 'True'
        if self.check_speaker.isChecked():
            speaker = 'True'
        if self.check_talkC.isChecked():
            coordinator = 'True'
        note = self.text_note.toPlainText()

        new_brother = Brother()
        new_brother.set_attribute(first_name, middle_name, last_name, email,
                                  phone, congregation, responsibility,
                                  speaker, chairman, coordinator, note)

        new_brother.add_brother()
        self.done(True)


class EditBrotherWindow(QtGui.QDialog, gui.AddBrotherWindow.Ui_AddBrotherWindow):
    """
    Opens AddBrotherWindow and changes the GUI for editing.

    """

    def __init__(self, row_id, parent=None):
        super(EditBrotherWindow, self).__init__(parent)
        self.setupUi(self)

        self.button_add.clicked.connect(lambda: self.submit_edits(row_id))
        self.setWindowTitle('Edit Brother')
        self.button_add.setText("Save")
        self.check_batch.hide()
        self.populate_cong()
        #Get the information from the selected brother
        sql = "SELECT * FROM Brother WHERE id={}".format(row_id)
        brother = DB.return_sql(self, sql)

        # Load selected item into the dialog
        self.line_f_name.setText(brother[0][1])
        self.line_m_name.setText(brother[0][2])
        self.line_l_name.setText(brother[0][3])
        self.line_email.setText(brother[0][4])
        self.line_phone.setText(brother[0][5])
        self.combo_congregation.setCurrentIndex(self.cong_index(brother))
        self.combo_publisher.setCurrentIndex(self.resp_index(brother))
        # Check boxes
        if brother[0][8] == 'True':
            self.check_chairman.setChecked(True)
        if brother[0][9] == 'True':
            self.check_speaker.setChecked(True)
        if brother[0][10] == 'True':
            self.check_talkC.setChecked(True)
        self.text_note.setText(brother[0][11])

    def cong_index(self, brother):
        """
        Returns the index of the congregation the brother belongs to.

        :param brother: The list belonging to the brother being edited.
        """

        congregation_index = enumerate(self.sorted_list)
        for item in congregation_index:
            if item[1][0] == brother[0][6]:
                cong_index = item[0]
        return cong_index

    def resp_index(self, brother):
        """
        Finds the correct index for the brother's responsibility.

        :param brother: The list belonging to the brother being edited.
        """

        resp = brother[0][7]
        if resp == 'Elder':
            return 0
        if resp == 'Ministerial Servant':
            return 1
        if resp == 'Publisher':
            return 2

    def populate_cong(self):
        """
        Populate the congregation combo box with all the names from
        congregations already entered into the database.

        """

        congregations = Congregation.get_list(None, 'ASC')
        self.sorted_list = congregations

        for congregation in congregations:
            self.combo_congregation.addItem(congregation[1])

    def submit_edits(self, row):
        """
        Method that submits user made edits to be committed to the database.

        All the fields are submitted to the Brother.edit_brother
        method which will do various checks such as make sure all required
        fields are entered. Then from there it is passed off to the db module
        that will cause the database to be modified.

        :param row: The row (id) in the database that is being modified.

        """

        first_name = self.line_f_name.displayText()
        middle_name = self.line_m_name.displayText()
        last_name = self.line_l_name.displayText()
        phone = self.line_phone.displayText()
        email = self.line_email.displayText()
        # Combo box
        selection = self.combo_congregation.currentIndex()
        congregation = self.sorted_list[selection][0]
        responsibility = self.combo_publisher.itemText(
            self.combo_publisher.currentIndex())
        # Capacity radio buttons
        if self.check_chairman.isChecked():
            chairman = 'True'
        else:
            chairman = 'False'
        if self.check_speaker.isChecked():
            speaker = 'True'
        else:
            speaker = 'Flase'
        if self.check_talkC.isChecked():
            coordinator = 'True'
        else:
            coordinator = 'False'
        note = self.text_note.toPlainText()

        edit = Brother()
        edit.set_attribute(first_name, middle_name, last_name, email, phone,
                           congregation, responsibility, speaker, chairman,
                           coordinator, note)
        edit.edit_brother(row)
        self.done(True)


class CongregationWindow(QtGui.QDialog,
                         gui.CongregationWindow.Ui_CongregationWindow):
    """
    Window that allows the user to add, edit, and delete congregations to the
    database.

    Methods:
      populate_table - Gets all the congregations entered in the database and
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
        self.sorted_list = None
        self.populate_table()
        self.button_delete.clicked.connect(self.delete_congregation)
        self.button_add.clicked.connect(self.show_add_congregation_window)
        self.button_edit.clicked.connect(self.edit_congregation_window)
        self.list_congregation.doubleClicked.connect(
            self.edit_congregation_window)
        # Sorting radio buttons.
        self.radioAscending.clicked.connect(lambda: self.populate_table('ASC'))
        self.radioDesending.clicked.connect(lambda: self.populate_table('DESC'))
        self.radioDate.clicked.connect(lambda: self.populate_table('DATE'))

    def populate_table(self, sort='ASC'):
        """
        Populates the congregation table so the user may select a
        congregation already entered into the database.

        """

        self.list_congregation.clear()
        list = Congregation.get_list(None, "{}".format(sort))
        self.sorted_list = list

        for item in list:
            self.list_congregation.addItem("{}".format(item[1]))


    def edit_congregation_window(self):
        """
        Call EditCongregationDialog class which opens the AddCongregationWindow.

        """

        selection = self.list_congregation.currentRow()
        row_id = self.sorted_list[selection][0]

        # Pass the row ID of the congregation the user has selected.
        self.show_edit = EditCongregationDialog(row_id)

        saved = self.show_edit.exec_()
        if saved:
            self.populate_table()


    def show_add_congregation_window(self):
        """
        Window that allows the user enter a new congregation into the
        database

        """

        self.add_cong_window = AddCongregationWindow()

        # If the user saves a new congregation, run populate_table()
        saved = self.add_cong_window.exec_()
        if saved:
            self.populate_table()


    def delete_congregation(self):
        """
        Switches the visibility to 'False' for a congregation to prevent it
        from being displayed in the congregation list.

        The DB.modify_item requires that the column and value to be a list.

        """

        selection = self.list_congregation.currentRow()
        id = self.sorted_list[selection][0]

        DB.modify_item(None, 'Congregation', ['visibility'], ['False'], id)
        self.populate_table()  # Update the cong. list after deletion


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
        week = self.determine_day()  # Return clicked radio button
        time = str(self.timeEdit.time())[20:-1]
        latitude = self.line_latitude.displayText()
        longitude = self.line_longitude.displayText()
        notes = self.text_note.toPlainText()
        visibility = 'True'

        new_congregation = Congregation()
        new_congregation.set_attributes(name, phone, email, address, city,
                                        state, zipcode, week, time, longitude,
                                        latitude, notes, visibility)
        new_congregation.add_congregation()
        self.done(True)

    def determine_day(self):
        """
        Determine which date the user has selected.

        :return: Return the radio button that is active. If no check radio
        button are active then do not return an empty string.

        Note:
        Radio buttons can be added to a button group and to replace the
        determine_day method by using a code line like this:
        day = group.checkedButton(); week = day.text() if day else ''

        What prevents this: as of December 10, 2014 there's a bug that doesn't
        allow PySide to compile button groups correctly.
        https://bugreports.qt-project.org/browse/PYSIDE-175#comment-267714

        """

        # NOTE: Consider moving this method to the congregation mod.

        if self.radioSaturday.isChecked():
            return "Saturday"
        elif self.radioSunday.isChecked():
            return "Sunday"


class EditCongregationDialog(QtGui.QDialog,
                             gui.AddCongregationWindow.Ui_AddCongregationWindow):
    """
    Opens the AddCongregationWindow for editing congregation entries from the
    database.

    """

    def __init__(self, row_id, parent=None):
        super(EditCongregationDialog, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Edit Congregation")
        self.checkBatch.hide()
        self.button_add.setText("Save")

        sql = "SELECT * FROM Congregation WHERE id={}".format(row_id)
        congregation = DB.return_sql(self, sql)

        self.button_add.clicked.connect(
            lambda: self.submit_edit(congregation[0][0]))

        # load information of selected congregation into the dialog
        self.line_name.setText(str(congregation[0][1]))
        self.line_phone.setText(str(congregation[0][2]))
        self.line_email.setText(str(congregation[0][3]))
        self.line_address.setText(str(congregation[0][4]))
        self.line_city.setText(str(congregation[0][5]))
        self.line_state.setText(str(congregation[0][6]))
        self.line_zipcode.setText(str(congregation[0][7]))
        # select the correct radio box
        if str(congregation[0][8]) == "Saturday":
            self.radioSaturday.setChecked(True)
        else:
            self.radioSunday.setChecked(True)
        # show the time
        h, m, s, ms = congregation[0][9].split(',')
        self.timeEdit.setTime(QtCore.QTime(int(h), int(m)))
        self.line_longitude.setText(str(congregation[0][10]))
        self.line_latitude.setText(str(congregation[0][11]))
        self.text_note.setText(str(congregation[0][12]))


    def submit_edit(self, row):
        """
        Method that submits user made edits to be committed to the database.

        All the fields are submitted to the Congregation.edit_congregation
        method which will do various checks such as make sure all required
        fields are entered. Then from there it is passed off to the db module
        that will cause the database to be modified.

        :param row: The row (id) in the database that is being modified.

        """

        name = self.line_name.displayText()
        phone = self.line_phone.displayText()
        email = self.line_email.displayText()
        address = self.line_address.displayText()
        city = self.line_city.displayText()
        state = self.line_state.displayText()
        zipcode = self.line_zipcode.displayText()
        week = AddCongregationWindow.determine_day(self)
        # Time slices out PySide.QtCore.QTime()
        time = str(self.timeEdit.time())[20:-1]
        latitude = self.line_latitude.displayText()
        longitude = self.line_longitude.displayText()
        notes = self.text_note.toPlainText()
        visibility = "True"

        edit = Congregation()
        edit.set_attributes(name, phone, email, address, city,
                                         state, zipcode, week, time, longitude,
                                         latitude, notes, visibility)
        edit.edit_congregation(row)

        self.done(True)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())
