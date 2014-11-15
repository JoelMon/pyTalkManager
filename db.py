import sqlite3


class DB:
    """Class that interfaces the database to the project."""


    path = ''  # Path to the SQLite database on the user's system.

    def DbInit():
        """Initialize SQLite database

        This method runs when the user is running pyTalkManager for the first time
        or when the user wants to initialize a new database. The method crates a
        new SQLite database with all the needed tables and fields used by PyTalkManager.
        """

        connection = sqlite3.connect(DB.path)
        c = connection.cursor()

        c.execute('''CREATE TABLE Assignment (
                                              id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                              speaker INTEGER NOT NULL,
                                              talk INTEGER NOT NULL,
                                              congregation INTEGER NOT NULL,
                                              chairman INTEGER NOT NULL,
                                              hospitality INTEGER NOT NULL,
                                              date DATETIME NOT NULL,
                                              FOREIGN KEY(speaker) REFERENCES Brother(id),
                                              FOREIGN KEY(talk) REFERENCES Talk(id),
                                              FOREIGN KEY(congregation) REFERENCES Congregation(id),
                                              FOREIGN KEY(chairman) REFERENCES Brother(id),
                                              FOREIGN KEY(hospitality) REFERENCES Hospitality(id)
                                              )''')

        c.execute('''CREATE TABLE Brother (
                                           id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                           first_name TEXT NOT NULL,
                                           middle_name TEXT,
                                           last_name TEXT NOT NULL,
                                           email TEXT,
                                           phone TEXT NOT NULL,
                                           congregation NUMERIC NOT NULL,
                                           responsibility TEXT NOT NULL,
                                           speaker BOOL NOT NULL DEFAULT 0,
                                           chairman BOOL NOT NULL DEFAULT 0,
                                           coordinator BOOL NOT NULL DEFAULT 0,
                                           note BLOB,
                                           FOREIGN KEY(congregation) REFERENCES Congregation(id)
                                           )''')

        c.execute('''CREATE TABLE Congregation (
                                           id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                           name TEXT NOT NULL,
                                           phone TEXT,
                                           email TEXT,
                                           street TEXT NOT NULL,
                                           city TEXT NOT NULL,
                                           state TEXT NOT NULL,
                                           zip NUMERIC NOT NULL,
                                           long NUMERIC,
                                           lat NUMERIC,
                                           note BLOB
                                           )''')

        c.execute('''CREATE TABLE Hospitality (
                                               id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                               name TEXT NOT NULL,
                                               note TEXT
                                               )''')

        c.execute('''CREATE TABLE SpeakerTalk (
                                               id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                               title INTEGER NOT NULL,
                                               speaker INTEGER NOT NULL,
                                               FOREIGN KEY(title) REFERENCES Talk(id)
                                               FOREIGN KEY(speaker) REFERENCES Brother(id)
                                               )''')

        c.execute('''CREATE TABLE Talk (
                                        id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                        title TEXT NOT NULL,
                                        subject TEXT
                                        )''')

        connection.close()


    def add_item(self, table, column=[], value=[]):
        """Takes an item and adds it to the database."""

    def add_item(self, table, column, value):
        """Takes an item and adds it to the database."""

        list_column = ''
        list_value = ''

        for each_column in column:
            list_column = list_column + each_column + ', '

        for each_value in value:
            list_value = list_value + each_value + ', '

        #Debugging
        print("INSERT INTO " + table + " (" + list_column[:-2] +
              ") VALUES(" + list_value[:-2] + ")")


    def delete_data(self):
        """ Deletes data from the database
        :return:
        """
        pass


    def edit_data(self):
        """ Edits data in the database
        :return:
        """
        pass