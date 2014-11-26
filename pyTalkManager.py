__author__ = 'Joel Montes de Oca'

import configparser

from PySide import QtGui

from db import DB


version = '0.1'
name = 'pyTalkManager'
configLocation = './config.ini'


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
        print("-"*80)
        print("The config.ini file was not found.")
        print("-"*80)
        print("Something may have gone wrong with the installation.\n"
              "Make sure the config.ini file is located in the "
              "application's root directory.")
        quit()

    except PermissionError:
        print("-"*80)
        print("Permission problem.")
        print("-"*80)
        print("You do not have sufficient permission for the config.ini file.")
        print("Fix the problem then run {} again.".format(name))
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
        messagebox.showerror("File config.ini was not found.",
                             "The config.ini file was not found. "
                             "Something may have gone wrong with the installation. "
                             "Make sure the config.ini file is located in the "
                             "application's root directory.")

        print('The config.ini file was not found.')
        quit()
    except PermissionError:
        messagebox.showerror('Permission problem.',
                             "You do not have sufficient permission for the config.ini file. "
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

    first_run = configGet('APP', 'first_time_running')

    if first_run == 'True':

        message_box = QtGui.QMessageBox()
        message_box.setWindowTitle("First time running pyTalkManager")
        message_box.setText("This is the first time you run pyTalkManager.\n\n"
                            "Please select a location to save pyTalkManager.")

        message_box.exec_()
        file_name = QtGui.QFileDialog.getSaveFileName(
            None, "Save New Database", "New_Database.tdb",
            "pyTalkManager Database *.tdb")
        if file_name[0] == '':
            message_box = QtGui.QMessageBox()
            message_box.setWindowTitle("Warning")
            message_box.Warning
            message_box.setText("You did not select a location to save the database.\n"
                                "Run pyTalkManager again and select a location to save\n"
                                "the database.")
            message_box.exec_()
            quit()

        else:
            configSet('APP', 'first_time_running', 'False')
            configSet('DB', 'location', file_name[0])
            DB.DbInit()
