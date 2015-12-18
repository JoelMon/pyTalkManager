#!/usr/bin/env python3

import sys
from PySide import QtGui, QtCore
import pyTalkManager as tm
from congregation import Congregation
from db import DB
from brother import Brother
from outline import Outline
# Importation of GUIs
# The following imports are the GUI dialogs/windows.
import gui.MainWindow
import gui.DatabaseWindow
import gui.BrotherWindow
import gui.AddBrotherWindow
import gui.CongregationWindow
import gui.AddCongregationWindow
import gui.OutlineWindow
import gui.AddOutlineWindow


class MainWindow(QtGui.QMainWindow, gui.MainWindow.Ui_MainWindow):
    """
    The main window of pyTalkManager when pyTalkManager starts.

    From MainWindow all functions of pyTalkManager is accessed by the end user.
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.center_on_screen()
        tm.first_run_check()

        # TOOL BAR ACTIONS
        # Connects the tool-bar buttons to functions that are responsible
        # of opening the corresponding dialog.
        self.actionDatabase.triggered.connect(
            self.show_database_window)  # Database Manager
        self.actionBrothers.triggered.connect(
            self.show_brother_window)  # Brother Manager
        self.actionCongregation.triggered.connect(
            self.show_congregation_window)  # Congregation Manager
        self.actionTalks.triggered.connect(
            self.show_outline_window)  # Talk-Outline Manager

    def center_on_screen(self):
        """
        Center the window on the user's screen at boot-up.
        """

        screen_resolution = QtGui.QDesktopWidget().screenGeometry()
        center_horizontal = ((screen_resolution.width() / 2) -
                             (self.frameSize().width() / 2))
        center_vertical = ((screen_resolution.height() / 2) -
                           (self.frameSize().height() / 2))

        self.move(center_horizontal, center_vertical)

    def show_database_window(self):
        """
        Method that opens the Database manager.
        """

        self.db_window = DatabaseWindow()
        self.db_window.show()

    def show_brother_window(self):
        """
        Method that opens the Brother manager.
        """

        self.bro_window = BrotherWindow()
        self.bro_window.show()

    def show_congregation_window(self):
        """
        Method that opens the Congregation manager.
        """

        self.congregation_window = CongregationWindow()
        self.congregation_window.show()

    def show_outline_window(self):
        """
        Method that opens the List manager.
        """

        self.outline_window = OutlineWindow()
        self.outline_window.show()


class DatabaseWindow(QtGui.QDialog, gui.DatabaseWindow.Ui_DatabaseWindow):
    """
    Database manager to manage the database.

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
    Brother manager that allows the user to add, edit, and delete brothers from
    the database.

    Methods:
       - user_option_sorter: Determines which sorting the user wants to use.
       - populate_brothers: Populates the TableWidget with the names and
       congregations of brothers.
       - populate_cong: Populates the combobox used when adding a new brother
       to the database. Also used for the combobox when the user edits a
       brother.
       - show_add_brother_window: Opens the add_brother_window
       show_edit_brother_window: Opens the edit_brother_window
       - id_brother: Returns the database ID of the brother selected by the
       user from the TableWidget.
    """

    brother_id_sorted = []  # Brother IDs in correct sorting order.

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
        # Sorting controls -- call user_option_sorter.
        self.radio_fname.clicked.connect(self.user_option_sorter)
        self.radio_l_name.clicked.connect(self.user_option_sorter)
        self.radio_all.clicked.connect(self.user_option_sorter)
        self.radio_coord.clicked.connect(self.user_option_sorter)
        self.radio_elder.clicked.connect(self.user_option_sorter)
        self.radio_ms.clicked.connect(self.user_option_sorter)
        self.radio_pub.clicked.connect(self.user_option_sorter)
        self.combo_cong.currentIndexChanged.connect(self.user_option_sorter)

    def user_option_sorter(self):
        """
        Determines which radio button(s) have been selected and adds the
        selected radio buttons to the dictionary 'options_selected'. Then it
        calls the populate_cong method and passes the options_selected
        dictionary so that the table can be sorted using the parameters
        included in options_selected.

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

        # call method to populate the tables with the options
        # selected by the user.
        self.populate_brothers(self.options_selected)

    def populate_brothers(self, option_dic):
        """
        Populate the brother item_list. item_list controls how many rows will be
        drawn on the table and etc.

        :param option_dic: A dictionary containing all of the user selected
        sorting options.
        """

        self.tableWidget.setColumnCount(2)
        bro = Brother()

        # Take option_dic and export values of each key to a variable to then be
        # passed to the SQL command.
        sort_name = option_dic["Name"]
        resp = option_dic["Resp"]
        coord = option_dic["Coord"]
        cong = option_dic["Cong"]
        self.tableWidget.clearContents()

        item_list = bro.populate_table(sort_name, resp, coord, cong)
        item_list = (list(enumerate(item_list)))
        self.tableWidget.setRowCount(len(item_list))

        # Add brothers from the database into TableWidget.
        # The brother_ids keeps track of the brothers placed in TableWidget in
        # the correct order. It's used to know which table ID to use when the
        # user selects an item in TableWidget.
        brother_ids = []
        for item in item_list:
            brother_ids.append(item[1][0])

            # Format names based on sorting option.
            if self.options_selected["Name"] == "first_name":
                # First name , middle name , and last name.
                name = QtGui.QTableWidgetItem("{} {} {}".format(item[1][1],
                                                                item[1][2],
                                                                item[1][3]))
            else:
                # Last name, first name, and middle name.
                name = QtGui.QTableWidgetItem("{}, {} {}".format(item[1][3],
                                                                 item[1][1],
                                                                 item[1][2]))

            congregation = QtGui.QTableWidgetItem("{Cong}".format(Cong=item[1][
                4]))

            self.tableWidget.setItem(int(item[0]), 0, name)
            self.tableWidget.setItem(int(item[0]), 1, congregation)

        # Return all of the brother database IDs in the correct order based
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
            self.user_option_sorter()

    def show_edit_brother_window(self):
        self.id_brother()
        self.edit_bro_window = EditBrotherWindow(self.id_brother())
        # If the user saves a new congregation, run populate_table()
        saved = self.edit_bro_window.exec_()
        if saved:
            self.user_option_sorter()

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
        Populate the congregation combo box with all the congregation names
        from database.
        """

        congregations = Congregation.get_list(None, 'ASC')
        self.sorted_list = congregations  # Don't remember why I did this line

        for congregation in congregations:
            self.combo_congregation.addItem(congregation[1])

    def add_brother(self):
        """ Method that collects all the user entered data and then submits it
        to be entered into the database.
        """

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
        # Brother's capacity radio buttons
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


class EditBrotherWindow(QtGui.QDialog,
                        gui.AddBrotherWindow.Ui_AddBrotherWindow):
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
        # Get the information from the selected brother
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

      edit_congregation_window: Repurpose the AddCongregationWindow for
      editing congregation information.
      load_congregation_data: Submits user edits back to the database
      show_add_congregation_window: Opens the AddCongregationWindow
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
        Call EditCongregationDialog class which opens the
        AddCongregationWindow and changes the dialog for editing.
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
        Window that allows the user to enter a new congregation into the
        database.
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
      new_congregation: Takes care of collecting user entered information
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

        # Load information of selected congregation into the dialog.
        self.line_name.setText(str(congregation[0][1]))
        self.line_phone.setText(str(congregation[0][2]))
        self.line_email.setText(str(congregation[0][3]))
        self.line_address.setText(str(congregation[0][4]))
        self.line_city.setText(str(congregation[0][5]))
        self.line_state.setText(str(congregation[0][6]))
        self.line_zipcode.setText(str(congregation[0][7]))
        # Select the correct radio box when dialogs loads.
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


class OutlineWindow(QtGui.QDialog, gui.OutlineWindow.Ui_OutlineWindow):
    """
    Window that shows all outlines available for the user to chose, add, edit,
    or delete.
    """

    def __init__(self, parent=None):
        super(OutlineWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_import.clicked.connect(self.import_file)
        self.button_delete.clicked.connect(self.delete_outline)
        self.button_add.clicked.connect(self.add_outline)
        self.button_edit.clicked.connect(self.edit_outline)
        self.radio_number.clicked.connect(self.populate_list)
        self.radio_title.clicked.connect(self.populate_list)
        self.sorted_list = []
        db = DB()

        # If there's no outlines in the DB then enable the import button
        # for the user, otherwise disable the import button.
        if db.count_rows('Talk', True) > 0:
            self.button_import.setEnabled(False)
            self.populate_list()

    def import_file(self):
        """
        Method that allows the user to import outlines from a file.

        :return: None
        """

        import_file = QtGui.QFileDialog.getOpenFileName(None, "Open Outline "
                                                              "", None,
                                                        "Outline File (*.txt)")
        outline = []
        with open(import_file[0], 'r') as text:
            for line in text:
                outline.append(line[:-1])  # Removes the '\n' at EOL

        database = DB()
        for line in outline:  # Adds the outlines to the DB
            number = line.find(':')
            database.add_item('Talk', ('number', 'title'), (line[:number],
                                                            line[number + 1:]))
        self.button_import.setEnabled(False)

    def populate_list(self):
        """Populates the talk_list widget with the outlines

        Format of outline_list: [(DB ID, number, title, visibility), ...]
        """
        db = DB()
        self.table_outline.clearContents()
        sql_number_sort = "SELECT * FROM Talk WHERE visibility='True' ORDER " \
                          "BY CAST (number AS INTEGER)"
        sql_title_sort = "SELECT * FROM Talk WHERE visibility='True' ORDER BY" \
                         " title ASC"

        if self.radio_number.isChecked():
            outline_list = DB.return_sql(None, sql_number_sort)
        else:
            outline_list = DB.return_sql(None, sql_title_sort)

        self.table_outline.setColumnCount(2)
        self.table_outline.setRowCount(db.count_rows('Talk', True))
        self.sorted_list = []  # Table IDs of items added sorted to the table

        index = 0  # Index of table_outline widget
        for item in outline_list:
            number = QtGui.QTableWidgetItem(item[1])
            title = QtGui.QTableWidgetItem(item[2])
            self.table_outline.setItem(index, 0, number)
            self.table_outline.setItem(index, 1, title)
            self.sorted_list.append(item[0])
            index += 1

    def delete_outline(self):
        """Delete a specific outline from the database."""

        selection = self.table_outline.currentRow()
        db = DB()
        item = db.return_item('Talk', self.sorted_list[selection])

        # Make sure the user intended to delete the outline
        msg = QtGui.QMessageBox()
        msg.setText('Delete outline {NUM} - "{TITLE}"?'.format(NUM=item[0][1],
                                                            TITLE=item[0][2]))
        msg.setStandardButtons(msg.No | msg.Yes)
        msg.setDefaultButton(msg.No)
        go_ahead = msg.exec_()

        if go_ahead == msg.Yes:
            DB.modify_item(None, 'Talk', ['visibility'], ['False'],
                           self.sorted_list[selection])
            self.populate_list()
        else:
            pass

    def add_outline(self):
        """Window for the user to add new outlines to the database."""

        self.add_outline_window = AddOutlineWindow()
        # If the user saves a new outline, run populate_table()
        saved = self.add_outline_window.exec_()
        if saved:
            self.populate_list()

    def edit_outline(self):
        """Window for the user to edit a selected outline"""

        selection = self.table_outline.currentRow()
        outline_id = self.sorted_list[selection]
        self.edit_outline_window = EditOutlineWindow(None, outline_id)
        saved = self.edit_outline_window.exec_()
        if saved:
            self.populate_list()


class AddOutlineWindow(QtGui.QDialog, gui.AddOutlineWindow.Ui_AddOutlineWindow):
    """
    Add Outline Window
    """

    def __init__(self, parent=None):
        super(AddOutlineWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_save.clicked.connect(self.add_outline)

    def add_outline(self):
        """
        Adds the contents of the AddOtlineWindow to the database.
        """

        outline = Outline()

        outline_number = self.line_number.displayText()
        outline_title = self.line_title.displayText()

        submission = outline.add_outline(outline_number, outline_title)

        if submission[0] == "True":
            self.done(True)
        else:
            error = QtGui.QMessageBox.critical(self, 'Error', submission[1])


class EditOutlineWindow(QtGui.QDialog,
                        gui.AddOutlineWindow.Ui_AddOutlineWindow):
    """
    Edit Outline Window
    """

    def __init__(self, parent=None, outline_id=0):
        super(EditOutlineWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Edit Outline')
        self.button_save.clicked.connect(self.save_edit)
        self.outline_id = outline_id

        db = DB()
        self.edited_item = db.return_item("Talk", self.outline_id)
        self.line_number.setText(self.edited_item[0][1])
        self.line_title.setText(self.edited_item[0][2])

    def save_edit(self):
        """
        Save edits made by the user to the selected outline.
        """

        number = self.line_number.displayText()
        title = self.line_title.displayText()

        outline = Outline()
        submission = outline.edit_outline(self.edited_item[0][1],
                                          self.edited_item[0][2], number, title,
                                          self.edited_item[0][0])

        if submission[0] == 'True':
            self.done(True)
        else:
            error = QtGui.QMessageBox.critical(self, 'Error', submission[1])


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())
