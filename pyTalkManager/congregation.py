__author__ = 'Joel Montes de Oca'

from db import DB


class Congregation:
    def __init__(self):
        self.name = None
        self.phone = None
        self.email = None
        self.street = None
        self.city = None
        self.state = None
        self.zip = None
        self.long = None
        self.lat = None
        self.note = None
        self.visibility = None


    # All of the columns in Congregation Window in correct order
    columns = ['name', 'phone', 'email', 'street', 'city',
               'state', 'zip', 'long', 'lat', 'note']


    def get_entries(self):
        """
        Retrieves all the entries for the Congregation table.
            :returns : list

        """

        sql = "SELECT * FROM Congregation"
        return DB.return_pass_sql(None, sql)


    def get_list(self):
        """Get's all the names of congregations already in the database
        and returns them.

        :return DB.return_pass_sql(None, sql): returns the output of
        the method DB.return_pass_sql(None, sql)

        """

        sql = "SELECT name from Congregation"
        return DB.return_pass_sql(None, sql)


    def add_congregation(self, values):
        """Method that adds a new congregation to the database.

         First checks to make sure all required fields were entered by
         the user. If the user failed to enter a required field then
         do not commit data to the database and return a list of
         missing fields.

        :param columns: a list of all columns in the Congregation table
        :param values: a list of user entered data for each column
        :return: Return True if all required fields were entered
                 otherwise return False.

        """

        # REVIEW long and lat: Leading zeros may be removed.
        required_fields = ['name', 'street', 'city', 'state', 'zip']
        combine = zip(Congregation.columns, values)

        # Check if user entered data repeats. This section checks if the
        # name field of the congregation repeats with congregations already
        # in the database. If so, return error with reason.
        # TODO: Break this section up into it's own method.

        congregation_names = Congregation.get_list(None)

        for item in congregation_names:
            item, value = str(item[0]), str(values[0])
            if item.lower() == value.lower():
                # The return[1] needs to be translated
                return False, "Error: duplicate", "Congregation '{}' has already been entered into the database.".format(
                    item)


        # Check user entered data against required_fields to see if user
        # has left any required fields empty. If required fields are empty,
        # then add the offending field to missing_fields list.
        # TODO: Break this section up into it's own method.

        missing_fields = []
        for item in combine:
            if item[0] in required_fields and item[1] == '':
                missing_fields.append(item[0])


        # If missing_fields list the data entered by the user is
        # submitted to the database. If missing_fields list is not
        # empty then return False and the list of missing_fields so
        # that the information can be relayed to the end user.

        if missing_fields == []:
            DB.add_item(None, 'Congregation', Congregation.columns, values)
            return True
        else:
            return False, "Error: Fields", missing_fields


    def edit_congregation(self, values, row):
        """Method that edits congregation that was entered into the database.

         First checks to make sure all required fields were entered by
         the user. If the user failed to enter a required field then
         do not commit data to the database and return a list of
         missing fields.

        :param columns: a list of all columns in the Congregation table
        :param values: a list of user entered data for each column
        :return: Return True if all required fields were entered
                 otherwise return False.

        """

        required_fields = ['name', 'street', 'city', 'state', 'zip']
        combine = zip(Congregation.columns, values)

        # Check user entered data against required_fields to see if user
        # has left any required fields empty. If required fields are empty,
        # then add the offending field to missing_fields list.

        missing_fields = []
        for item in combine:
            if item[0] in required_fields and item[1] == '':
                missing_fields.append(item[0])


        # If missing_fields list the data entered by the user is
        # submitted to the database. If missing_fields list is not
        # empty then return False and the list of missing_fields so
        # that the information can be relayed to the end user.

        if missing_fields == []:
            DB.modify_item(None, 'Congregation', Congregation.columns, values, row)
            return True
        else:
            return False, "Error: Fields", missing_fields
