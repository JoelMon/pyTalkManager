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

    def check_sanity(self, number, title, edit=False, new_number=0, new_title=0):
        """"
        Checks to make sure there are no duplicates in the database. 

        :param number: The outline number being checked
        :param title: The outline title being checked
        :param new_number: The new outline number if edit is True.
        :param new_title: The new outline title if edit is True.
        """
        self.number = number
        self.title = title
        self.new_number = new_number
        self.new_title = new_title

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

        # If edit is true, remove the original item to not cause false duplicate warnings.
        if edit:  
            outline_number_list.remove(self.number)
            outline_title_list.remove(self.title)
            self.number = self.new_number
            self.title = self.new_title

        if str(self.number) in outline_number_list:
            return ('False', "duplicate outline number")
        if self.title in outline_title_list:
            return ('False', "duplicate outline title")

        return ('True',)

    def edit_outline(self, old_number, old_title, number, title, id):
        """
        Edits the content of the selected item selected.

        :param old_number: The outline number before the user edits it.
        :param old_title: The outline title before the user edits it.
        :param number: The new outline number entered by the user.
        :param title: The new outline title entered by the user.
        :param id: The database id for the item being edited by the user.
        """

        check = self.check_sanity(old_number, old_title, True, number, title)
        if check[0] == 'True':
            column = ['number', 'title']
            value = [number, title]
            DB.modify_item(self, 'Talk', column, value, id)
            return ('True',)
        else:
            return check

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
