import sqlite3
import pyTalkManager as tm


class DB:
    """Class that interfaces the database to the project."""


    def get_path():
        """Returns the path of the database located in config.ini"""
        return tm.configGet('DB', 'location')


    def DbInit():
        """Initialize SQLite database

        This method runs when the user is running pyTalkManager for the first time
        or when the user wants to initialize a new database. The method crates a
        new SQLite database with all the needed tables and fields used by PyTalkManager.
        """

        conn = sqlite3.connect(DB.get_path())
        c = conn.cursor()

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

        conn.close()


    def add_item(self, table, column=[], value=[]):
        """Takes an item and adds it to the database."""

    def add_item(self, table, column, value):
        """Takes an item and adds it to the database.

        :arguments
        table - a string with the table that will be written to
        column - a list with the the column(s) that will be written in
        value - a list with the value(s) that will be written.

        """

        list_column = ', '.join(column)
        list_value = "', '".join(value)

        command = "INSERT INTO {table}({column}) VALUES('{values}')".format(table=table,
                                                                          column=list_column,
                                                                          values=list_value)
        print(command)
        comm = sqlite3.connect(DB.get_path())
        c = comm.cursor()

        c.execute("PRAGMA foreign_keys = ON")
        c.execute(command)

        comm.commit()
        c.close()


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