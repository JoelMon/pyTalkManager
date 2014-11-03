#!/usr/bin/env python3

__author__ = 'Joel Montes de Oca'

import pyTalkManagerDatabase as DB
import pyTalkManager as TM
from tkinter import *
from tkinter import ttk


def main():

    firstrun = TM.configGet('APP', 'FirstTimeRunning')

    if firstrun == 'True':
        print('This is the first time the user runs pyTalkManager.')

        initWindow = Tk()
        initWindow.title('Setup of pyTalkManager')

        Label(initWindow, text='This is the first time that pyTalkManager runs. '
                               'Fill out the information bellow. Do not skip this step '
                               'in order to insure the program runs properly.', justify=LEFT,
              wraplength=TM.configGet('WINDOWS', 'InitWndowSize')[:3]).grid(row=0, column=0, columnspan=2, ipadx=10, ipady=10)

        ttk.Label(initWindow, text='Your First Name:').grid(row=1, column=0, sticky=E, ipadx=10)
        efirstname = ttk.Entry(initWindow).grid(row=1, column=1, sticky=W, ipadx=5)
        ttk.Label(initWindow, text='Your Middle Name:').grid(row=2, column=0, sticky=E, ipadx=10)
        emiddlename = ttk.Entry(initWindow).grid(row=2, column=1, sticky=W, ipadx=5)
        ttk.Label(initWindow, text='Your Last Name:').grid(row=3, column=0, sticky=E, ipadx=10)
        elastname = ttk.Entry(initWindow).grid(row=3, column=1, sticky=W, ipadx=5)
        ttk.Label(initWindow, text='Your email address:').grid(row=4, column=0, sticky=E, ipadx=10)
        eemailaddress = ttk.Entry(initWindow).grid(row=4, column=1, sticky=W, ipadx=5)
        ttk.Label(initWindow, text='Your Congregation Name:').grid(row=5, column=0, sticky=E, ipadx=10)
        econgname = ttk.Entry(initWindow).grid(row=5, column=1, sticky=W, ipadx=5)
        ttk.Label(initWindow, text='').grid(row=6, columnspan=2) # Spacer

        bquit = ttk.Button(initWindow, text='Quit', command=initWindow.quit).grid(row=7, column=0, sticky=E)
        bsave = ttk.Button(initWindow, text='Save', command=TM.initsave).grid(row=7, column=1, sticky=W)
        ttk.Label(initWindow, text='').grid(row=8, columnspan=2) # Spacer
        mainloop()
    else:
        # Load GUI

        mWindow = Tk()
        mWindow.title('pyTalkManager')
        mWindow.geometry(TM.configGet('WINDOWS', 'MainWindowSize'))

        # The Menubar
        menubar = Menu(mWindow)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='exit', command=mWindow.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help', command=TM.buttonTest)
        helpmenu.add_command(label='About', command=TM.buttonTest)
        menubar.add_cascade(label='Help', menu=helpmenu)

        mWindow.config(menu=menubar)

        mainloop()

if __name__ == '__main__':
    main()
