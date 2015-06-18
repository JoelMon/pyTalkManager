from db import DB
from PySide import QtGui

class Outline:
    def __init__(self):
        self.number = None
        self.title = None

    def set_attributes(self, number=None, title=None):
        """
        Sets the attributes for the outline module

        :param number: The outline number
        :param title: The title for the outline
        """

        self.number = number
        self.title = title

    def check_sanity(self):
        """"
        Checks to make sure there are no duplicates in the database. 
        """
        outline_number_list = []
        outline_title_list = []

        sql_code = """SELECT * FROM Talk WHERE visibility IS 'True'"""
        database_titles = DB.return_sql(None, sql_code)
        print(database_titles)
        
        # Check for duplicates

        for outline in database_titles:
           outline_number_list.append(outline[1])
           outline_title_list.append(outline[2])

        if self.number in outline_number_list:
           return ('False', "duplicate outline number")
        if self.title in outline_title_list:
           return ('False', "duplicate outline title")

        return 'True'

    def add_outline(self):
        """
        Sends content received to be added to the database.
        """

        check = self.check_sanity()
        if check == 'True':
          # TODO Finish this function
          print("Passed")
        else:
          print(check)
          mesg_box = QtGui.QMessageBox() 
          mesg_box.setIcon(QtGui.QMessageBox.Critical)
          #mesg_box.setTitle("Error")
          mesg_box.setText("The information you have entered already exists in the database. Please revise your information or press cancel. Error: {}".format(check[1]))
          run = mesg_box.exec_()
