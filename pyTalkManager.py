__author__ = 'Joel Montes de Oca'

import sys
import configparser
import sqlite3
from PySide import QtGui


version = '0.1'
name = 'pyTalkManager'
configLocation = './config.ini'


class db:

    path = ''

    def dbinit():
        """Initialize SQLite database

        This method runs when the user is running pyTalkManager for the first time
        or when the user wants to initialize a new database. The method crates a
        new SQLite database with all the needed tables and fields used by PyTalkManager.
        """

        connection = sqlite3.connect(db.path)
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


def configGet(section, key):
    """
    Takes arguments for the config.ini file and returns the key.
    :return: key from config.ini
    """

    # Testing the file with exceptions rather than os.access() due to security risk.
    # Source: https://docs.python.org/3.4/library/os.html#os.X_OK
    try:
        open(configLocation)
    except FileNotFoundError:
        messagebox.showerror("File config.ini was not found.", "The config.ini file was not found. "
                                                               "Something may have gone wrong with the installation. "
                                                               "Make sure the config.ini file is located in the "
                                                               "application's root directory.")
        print('The config.ini file was not found.')
        quit()
    except PermissionError:
        messagebox.showerror('Permission problem.', "You do not have sufficient permission for the config.ini file. "
                                                    "Fix the problem then run %s again." % name)
        print('You do not have permission to read the config.ini file.')
        quit()

    config = configparser.ConfigParser()
    config.read(configLocation)

    return config[section].get(key)


def configSet(section, key, value):
    """
    Takes arguments for the config.ini file and writes to file.
    """

    # Testing the file with exceptions rather than os.access() due to security risk.
    # Source: https://docs.python.org/3.4/library/os.html#os.X_OK
    try:
        open(configLocation)
    except FileNotFoundError:
        messagebox.showerror("File config.ini was not found.", "The config.ini file was not found. "
                                                               "Something may have gone wrong with the installation. "
                                                               "Make sure the config.ini file is located in the "
                                                               "application's root directory.")
        print('The config.ini file was not found.')
        quit()
    except PermissionError:
        messagebox.showerror('Permission problem.', "You do not have sufficient permission for the config.ini file. "
                                                    "Fix the problem then run %s again." % name)
        print('You do not have permission to read the config.ini file.')
        quit()

    config = configparser.ConfigParser()
    config.read(configLocation)
    config.set(section, key, value)
    file = open(configLocation, 'w')
    config.write(file)


def buttonTest():
    """
    Test if a command works by printing a confirmation.
    :return: 'The command worked.'
    """
    print('The command worked.')


def firstRunCheck():
    """Checks to see if it's pyTalkManager first time running.

    If it is pyTalkManager's first time running then initialize
    a SQLite database.

    TODO: Have to add exception encase the config.ini file is
    not found.
    """

    first_run = configGet('APP', 'FirstTimeRunning')

    if first_run == 'True':

        message_box = QtGui.QMessageBox()
        message_box.setWindowTitle("First time running pyTalkManager")
        message_box.setText("This is the first time you run pyTalkManager.\n\n"
                            "The next window you will be asked to choose\n"
                            "a location where you would like to save\n"
                            "pyTalkManager's database.")
        message_box.exec_()
        file_name = QtGui.QFileDialog.getSaveFileName(
            None, "Save New Database", "New_Database.tdb",
            "pyTalkManager Database *.tdb")
        if file_name[0] == '':
            message_box = QtGui.QMessageBox()
            message_box.setWindowTitle("Warning")
            message_box.Warning
            message_box.setText("You did not select a location to save the database.\n"
                                "Run pyTalkManager again and select a location to save.")
            message_box.exec_()
            quit()

        else:
            db.path = file_name[0]
            db.dbinit()
            configSet('APP', 'firsttimerunning', 'False')
            configSet('DB', 'location', db.path)
