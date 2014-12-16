__author__ = 'Joel Montes de Oca'

import configparser
from PySide import QtGui
from db import DB

version = '0.1'
name = 'pyTalkManager'
configLocation = './config.ini'


def config_get(section, key):
    """
    Takes arguments for the config.ini file and return the key.

    :return: key from config.ini
    """

    # Testing the file with exceptions rather than os.access() due to security risk.
    # Source: https://docs.python.org/3.4/library/os.html#os.X_OK
    try:
        open(configLocation)

    except FileNotFoundError:
        print("-" * 80)
        print("The config.ini file was not found.")
        print("-" * 80)
        print("Something may have gone wrong with the installation.\n"
              "Make sure the config.ini file is located in the "
              "application's root directory.")
        quit()

    except PermissionError:
        print("-" * 80)
        print("Permission problem.")
        print("-" * 80)
        print("You do not have sufficient permission for the config.ini file.")
        print("Fix the problem then run {} again.".format(name))
        quit()

    config = configparser.ConfigParser()
    config.read(configLocation)

    return config[section].get(key)


def config_set(section, key, value):
    """
    Takes arguments for the config.ini file and writes to file.

    NOTE: The exceptions must be changed to print to avoid
    errors. This is code left behind from the time that pyTalkmanager
    was using the Tkinter framework.
    """

    # Testing the file with exceptions rather than os.access() due to security risk.
    # Source: https://docs.python.org/3.4/library/os.html#os.X_OK
    try:
        open(configLocation)
    except FileNotFoundError:
        print("File config.ini was not found.\n",
              "The config.ini file was not found. "
              "Something may have gone wrong with the installation. "
              "Make sure the config.ini file is located in the "
              "application's root directory.")

        print("The config.ini file was not found.")
        quit()
    except PermissionError:
        print("Permission problem.",
              "You do not have sufficient permission for the config.ini file. "
              "Fix the problem then run {} again.".format(name))

        print("You do not have permission to read the config.ini file.")
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

    return 'The command worked.'


def first_run_check():
    """
    Checks to see if it's pyTalkManager first time running.

    If it is pyTalkManager's first time running then initialize
    a SQLite database.
    """

    first_run = config_get('APP', 'first_time_running')

    if first_run == 'True':
        print("-" * 80)
        print("First time running pyTalkManager")
        print("-" * 80)
        print("This is the first time you run pyTalkManager.\n",
              "Please select a location to save pyTalkManager.")

        # Display QT Save File dialog window.
        file_name = QtGui.QFileDialog.getSaveFileName(
            None, "Save New Database", "New_Database.tdb",
            "pyTalkManager Database *.tdb")

        if file_name[0] == '':
            print("Warning\n")
            print("You did not select a location to save the database. "
                  "Run pyTalkManager again and select a location to save "
                  "the database.")
            quit()

        else:
            config_set('APP', 'first_time_running', 'False')
            config_set('DB', 'location', file_name[0])
            DB.DbInit()
