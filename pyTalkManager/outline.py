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

    def check_sanity(self, number, title):
        """"
        Checks to make sure there are no duplicates in the database. 

        :param number: The outline number being checked
        :param title: The outline title being checked
        """
        self.number = number
        self.title = title

        if str(self.number) == '':
            return ('False', 'Outline number is missing.')
        if str(self.title) == '':
            return ('False', 'Outline title is missing.')

        outline_number_list = []
        outline_title_list = []

        sql_code = """SELECT * FROM Talk WHERE visibility IS 'True'"""
        database_titles = DB.return_sql(None, sql_code)
        
        # Check for duplicates

        for outline in database_titles:
            outline_number_list.append(outline[1])
            outline_title_list.append(outline[2])

        if str(self.number) in outline_number_list:
            return ('False', "duplicate outline number")
        if self.title in outline_title_list:
            return ('False', "duplicate outline title")

        return ('True',)

    def add_outline(self, number, title):
        """
        Sends content received to be added to the database.
        """

        check = self.check_sanity(number, title) 
        if check[0] == 'True':
            DB.add_item(self,'Talk', ('number', 'title', 'visibility'), (number, title, 'True'))
            return ('True',) 
           
        else:
          return check 
