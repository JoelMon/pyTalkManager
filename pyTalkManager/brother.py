from db import DB

class Brother:
    """
    Brother class
    """

    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.email = None
        self.phone = None
        self.congregation = None
        self.responsibility = None
        self.speaker = None
        self.chairman = None
        self.coordinator = None
        self.note = None
        self.visibility = 'True'

    columns = ('first_name', 'middle_name', 'last_name', 'email', 'phone',
               'congregation', 'responsibility', 'speaker', 'chairman',
               'coordinator', 'note', 'visibility')

    def set_attribute(self, first_name=None, middle_name=None,
                      last_name=None, email=None, phone=None,
                      congregation=None, responsibility=None, speaker=None,
                      chairman=None, coordinator=None, note=None):
        """
        An interface to allow other methods to set __init__'s variables.

        :param first_name: The first name of the brother
        :param middle_name: The middle name of the brother
        :param last_name: The last name of the brother
        :param email: The email address of the brother
        :param phone: The phone number of the brother
        :param congregation: The congregation the brother belongs to
        :param responsibility: The responsibility held by the brother
        :param speaker: Can the brother give talks?
        :param chairman: Can the brother be a chairman?
        :param coordinator: Is the brother a talk coordinator?
        :param note: Notes about the brother

        """

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.congregation = congregation
        self.responsibility = responsibility
        self.speaker = speaker
        self.chairman = chairman
        self.coordinator = coordinator
        self.note = note

    def add_brother(self):
        """
        Adds a new brother to the database.

        :return:
        """

        values = (self.first_name,
                  self.middle_name,
                  self.last_name,
                  self.email,
                  self.phone,
                  self.congregation,
                  self.responsibility,
                  self.speaker,
                  self.chairman,
                  self.coordinator,
                  self.note,
                  self.visibility)

        missing_fields = Brother.__check_required_fields(self)

        if missing_fields == "Passed":
            DB.add_item(None, 'Brother', Brother.columns, values)
        else:
            print("The following are missing: ", missing_fields)

    def populate_table(self, name="first_name", resp="NOT NULL",
                       coord="NOT NULL", cong="NOT NULL"):
        """
        Returns information about all the brothers in the database for the
        purpose of populating the brother table.

        :param resp: The responsibility that will be displayed. "NOT NULL"
        shows all. In order to show a specific responsibility, the name of
        the responsibility need to be passed within quotations such as:
        '"Elder"'
        :param name: The method in which the brother's names will be sorted.
        The default method is by first name.
        :return: Brother id, first name, middle name, last name,
        and congregation
        """

        sql = """
        SELECT Brother.id, first_name, middle_name, last_name,
        congregation.name FROM Brother JOIN Congregation ON
        Brother.congregation=Congregation.id WHERE
        Brother.responsibility is {RESP} AND Brother.coordinator is {COORD}
        AND Congregation.name is {CONG} ORDER BY {NAME} ASC
        """.format(RESP=resp, COORD=coord, CONG=cong, NAME=name)

        return DB.return_sql(self, sql)

    def __check_required_fields(self):
        """
        Checks for required fields when the user submits a new brother to be
        entered into the database.

        :return:
        """

        missing_fields = []

        if self.first_name == '':
            missing_fields.append('first name')
        if self.last_name == '':
            missing_fields.append('last name')
        if self.phone == '':
            missing_fields.append('phone')
        if self.chairman == '' and self.speaker == '' and self.coordinator ==\
                '':
            missing_fields.append('capacity')
        if missing_fields == []:
            return "Passed"
        else:
            return missing_fields

    def edit_brother(self, row):
        """
        Prepares user entered data for the selected brother before sending
        it to the db module for updating it in the database.

        Checks conducted: Check for required fields the user may have left
        blank.

        :param row: The id within the table Congregation being edited.
        """

        values = [self.first_name,
                  self.middle_name,
                  self.last_name,
                  self.email,
                  self.phone,
                  self.congregation,
                  self.responsibility,
                  self.speaker,
                  self.chairman,
                  self.coordinator,
                  self.note,
                  self.visibility]

        # Check for missing fields
        # TODO: There's a bug when you try to save while there's a missing field
        missing_fields = Brother.__check_required_fields(self)
        if missing_fields == "Passed":
            DB.modify_item(None, 'Brother', Brother.columns, values, row)
        else:
            print("A required field was missing: {}".format(missing_fields))

    # TODO Add a check for duplicates