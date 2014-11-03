__author__ = 'Joel Montes de Oca'

import sys
import configparser

version = '0.1'
name    = 'pyTalkManager'
configLocation = './config.ini'


def initsave():
    messagebox.showinfo('Information Saved', 'The information you entered have been saved. Please restart the program.')
    config = configparser.ConfigParser()
    config.read(configLocation)
    config.set('APP', 'FirstTimeRunning', 'False')
    file = open(configLocation, 'w')
    config.write(file)
    file.close()

    quit()


def WinSize(size, padding):
    """
    Takes a window size in the format 'LENGTHxHIGHT' and padding.
    :return: Outputs a new LENGTH that takes into account padding.
    """

    size = size.split('x')


def configGet(section, key):
    """
    Takes arguements for the config.ini file and returns the key.
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

def buttonTest():
    """
    Test if a command works by printing a confirmation.
    :return: 'The command worked.'
    """
    print('The command worked.')
