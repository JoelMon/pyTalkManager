__author__ = 'Joel Montes de Oca'

from db import DB


class Congregation:
    """Congregation class"""


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
        self.visibility = True


    # All of the columns in Congregation Window in correct order
    columns = ['name', 'phone', 'email', 'street', 'city',
               'state', 'zip', 'long', 'lat', 'note', 'visibility']


    def set_attributes(self,
                       name=None,
                       phone=None,
                       email=None,
                       street=None,
                       city=None,
                       state=None,
                       zip=None,
                       long=None,
                       lat=None,
                       note=None,
                       visibility=True):

        self.name = name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.long = long
        self.lat = lat
        self.note = note
        self.visibility = visibility


    def get_entries(self):
        """
        Retrieves all the entries for the Congregation table.
            :returns : list

        """

        sql = "SELECT * FROM Congregation"
        return DB.return_pass_sql(None, sql)


    def get_list(self):
        """
        Get's all the names of congregations already in the database
        and returns them. The names are all returned within a list.

        :return DB.return_pass_sql(None, sql): returns the output of
        the method DB.return_pass_sql(None, sql)

        """

        sql = "SELECT name from Congregation"
        return DB.return_pass_sql(None, sql)


    def add_congregation(self):
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

        values = [self.name,
                 self.phone,
                 self.email,
                 self.street,
                 self.city,
                 self.state,
                 self.zip,
                 self.long,
                 self.lat,
                 self.note,
                 self.visibility]

        # REVIEW long and lat: Leading zeros may be removed.

        # Check for dupicates in the database.
        # TODO: Break this section up into it's own method.
        congregation_names = Congregation.get_list(None)

        for item in congregation_names:
            item, value = str(item[0]), str(values[0])
            if item.lower() == value.lower():
                # The return[1] needs to be translated
                return False, "Error: duplicate", "Congregation '{}' has already been entered into the database.".format(
                    item)

        missing_fields = Congregation.__check_required_fields(self)

        if missing_fields:
            DB.add_item(None, 'Congregation', Congregation.columns, values)
        else:
            print("ERROR: The following fields were missing and are reqired: {}".format(missing_fields))


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


    def __check_required_fields(self):

        # required_fields = ['name', 'street', 'city', 'state', 'zip']
        missing_fields = []

        if self.name is None:
            missing_fields.append("name")
        elif self.street is None:
            missing_fields.append("street")
        elif self.city is None:
            missing_fields.append("city")
        elif self.state is None:
            missing_fields.append("state")
        elif self.zip is None:
            missing_fields.append("zip")

        # If missing_fields list the data entered by the user is
        # submitted to the database. If missing_fields list is not
        # empty then return False and the list of missing_fields so
        # that the information can be relayed to the end user.

        if missing_fields == []:
            return True
        else:
            return False, missing_fields


    def zero_out(self):
        """
        Returns all of the Congregation's atributes back to null.
        """

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
