from db import DB


class Congregation:
    """Congregation class"""

    def __init__(self):
        self.name = ''
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
               'state', 'zip', 'week', 'time', 'long', 'lat',
               'note', 'visibility']


    def set_attributes(self,
                       name=None,
                       phone=None,
                       email=None,
                       street=None,
                       city=None,
                       state=None,
                       zipcode=None,
                       week=None,
                       time=None,
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
        self.zip = zipcode
        self.week = week
        self.time = time
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


    def get_list(self, sort=None):
        """
        Get's all the names of congregations already in the database
        and returns them. The names are all returned within a list.

        :return DB.return_pass_sql(None, sql): returns the output of
        the method DB.return_pass_sql(None, sql)

        """

        if sort == "ASC":
            sql = "SELECT id, name FROM Congregation ORDER BY name ASC"
            return DB.return_pass_sql(None, sql)
        if sort == "DESC":
            sql = "SELECT id, name FROM Congregation ORDER BY name DESC"
            return DB.return_pass_sql(None, sql)
        if sort == "DATE":
            sql = "SELECT id, name FROM Congregation ORDER BY id ASC"
            return DB.return_pass_sql(None, sql)
        else:
            sql = "SELECT id, name FROM Congregation"
            return DB.return_pass_sql(None, sql)

    def add_congregation(self):
        """
        Method that prepares user entered data for a new congregation
        before sending it to the db module for insertion into the database.
        """

        values = [self.name,
                 self.phone,
                 self.email,
                 self.street,
                 self.city,
                 self.state,
                 self.zip,
                 self.week,
                 self.time,
                 self.long,
                 self.lat,
                 self.note,
                 self.visibility]

        # REVIEW long and lat: Leading zeros may be removed.

        dup_congregation = Congregation.__check_for_dup(self, values[0])
        missing_fields = Congregation.__check_required_fields(self)

        if dup_congregation == "Passed" and missing_fields == "Passed":
            DB.add_item(None, 'Congregation', Congregation.columns, values)
        else:
            if dup_congregation != "Passed":
                print("A duplicate entry was found: {}".format(dup_congregation[1]))
            else:
                print("A required field was missing: {}".format(missing_fields[1]))


    def edit_congregation(self, row):
        """
        Method that prepares user entered data for the selected congregation
        before sending it to the db module for updating it in the database.

        :param row: The row within the table Congregation being edited.
        """

        values = [self.name,
                 self.phone,
                 self.email,
                 self.street,
                 self.city,
                 self.state,
                 self.zip,
                 self.week,
                 self.time,
                 self.long,
                 self.lat,
                 self.note,
                 self.visibility]

        # REVIEW long and lat: Leading zeros may be removed.

        missing_fields = Congregation.__check_required_fields(self)

        if missing_fields == "Passed":
            DB.modify_item(None, 'Congregation', Congregation.columns, values, row)
        else:
            print("A required field was missing: {}".format(missing_fields[1]))


    def __check_for_dup(self, name):
        """
        Checks to see if the congregation already exists in the database.
        If the congregation exists then return 'Failed' along with the
        name of the duplicated congregation, otherwise return Passed.

        :argument name: The name of the congregation to check.
        :returns Passed: If no duplicates are found.
        :returns (Failed, 'item'): If a duplicate is found.
        """

        congregation = Congregation()
        list_of_congregations = congregation.get_list()
        check_name = name

        if list_of_congregations == []:
            return "Passed"
        else:
            for item in list_of_congregations:
                item = item[0]
                if item.lower() == check_name.lower():
                    return ("Failed", item)
                else:
                    return "Passed"


    def __check_required_fields(self):
        """
        Checks to see if all required fields for Congregation has been
        entered by the user.

        :returns 'Passed': If all required fields were entered.
        :returns ('Failed', [field, ...]: If required fields were not entered.
        """

        missing_fields = []

        if self.name == '':
            missing_fields.append("name")
        if self.street == '':
            missing_fields.append("street")
        if self.city == '':
            missing_fields.append("city")
        if self.state == '':
            missing_fields.append("state")
        if self.zip == '':
            missing_fields.append("zip")
        if self.week == '':
            missing_fields.append("week")
        if self.time == '':
            missing_fields.append('time')

        if missing_fields == []:
            return "Passed"
        else:
            return ("Failed", missing_fields)


    def zero_out(self):
        """
        Returns all of the Congregation's attributes back to null.
        """

        self.name = None
        self.phone = None
        self.email = None
        self.street = None
        self.city = None
        self.state = None
        self.zip = None
        self.week = None
        self.time = None
        self.long = None
        self.lat = None
        self.note = None
        self.visibility = None
