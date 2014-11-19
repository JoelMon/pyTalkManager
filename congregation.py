__author__ = 'Joel Montes de Oca'

import gui.CongregationWindow as CongWindow
from db import DB

class Congregation:


    def get_list(self):

        sql = "SELECT name from Congregation"

        return DB.return_pass_sql(None, sql)

    def add_congregation(self, columns, values):
        """Method that adds a new congregation to the database.

         First checks to make sure all required
         fields were entered by the user. If the user failed to enter
         a required field then do not commit data to the database
         and return a list of missing fields.

         :var required_fields: a list of required fields
         :var missing_fields: a list of required fields found to be empty
        :param columns: a list of all columns in the Congregation table
        :param values: a list of user entered data for each column
        :return: Return True if all required fields were entered
                 otherwise return False.

        """

        required_fields = ['name', 'street', 'city', 'state', 'zip']

        combine = zip(columns, values)

        missing_fields = []
        for x in combine:
            if x[0] in required_fields and x[1] == '':
                missing_fields.append(x[0])

        if missing_fields == []:
            DB.add_item(None, 'Congregation', columns, values)
            return True
        else:
            print(missing_fields)
            return False