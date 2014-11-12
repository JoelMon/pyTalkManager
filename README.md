# pyTalkManager

pyTalkManager is a program to aid public talk coordinators in the
congregations of Jehovah's Witness. It is written in
[Python3](https://www.python.org/) and uses the
[Qt](http://qt-project.org/) GUI framework
([PySide](http://qt-project.org/wiki/PySide)) and
[SQLite](https://www.sqlite.org/) for its database, all of which are
open source and cross platform technologies. Visit the project's
[wiki](https://github.com/TheoDevelopers/pyTalkManager/wiki) for more
information.

##Development

pyTalkManager is only now starting to be developed. At the moment I am
in the designing phase and do not expect to have pyTalkManager ready
for quite some time. Check back every few weeks to keep an eye on the
progress.

##Installation

pyTalkManager is still in its early stages of development. It is not
recommended for you to download and try to run pyTalkManager.

pyTalkManager will be compiled for Windows and packaged for Linux and
Mac OS X for easy installation once pyTalkManager v.1.0 is released.

If you are still curious and want to install pyTalkManager as it is
being developed then you can follow the instructions in this section
to do so.

###Windows

At the moment it requires a bit of effort to run pyTalkManager in its
current state on Windows. 

Download the source files for pyTalkManager from the
[pyTalkManager website](https://theodevelopers.github.io/pyTalkManager/)
and decompress the file.

In order to install pyTalkManager you will have to have
[Python3](https://www.python.org/downloads/) installed on your
system. Once Python is installed, you must adjust your system
variables so that that you may run the `python` interpreter without
having to `cd` into the Python installed directory. Instructions for
setting system variables can be found in the
[Python documentation](https://docs.python.org/3.4/using/windows.html).

Once Python3 is installed, you must install the
[PySide framework](http://qt-project.org/wiki/PySide_Binaries_Windows).

Once everything is installed correctly, open your terminal and `cd`
insto the directory containing the source files you downloaded from
this repository. Run the command `python main.py` and pyTalkManager
will run.

###Linux/GNU

Download the source files for pyTalkManager from the
[pyTalkManager website](https://theodevelopers.github.io/pyTalkManager/)
and decompress the file. main.py is the main script for pyTalkManager.

Make sure you have Python3 and PySide installed.

####Debian

`sudo apt-get install python3 && sudo apt-get install python3-pyside`

Once that is installed, run `python3 main.py` and pyTalkManager will run. 

##Dependencies

There is only one dependency that is not included in the Python's
Standard Library which must be installed.

* [pySide](http://qt-project.org/wiki/PySide) - pySide is used as the
  user interface framework and must be installed on your system for
  pyTalkmanager to run. pySide can be downloaded from [here]
  (http://qt-project.org/wiki/Category:LanguageBindings::PySide::Downloads).

##Open Source

I have decided to create pyTalkManager as an open source project. By
using an [open source](https://en.wikipedia.org/wiki/Open_source)
model, features and bug fixes can be submitted by anyone who is
willing to help. Furthermore, if the project becomes stagnate, others
may take the source code of pyTalkManager and continue its
development. This is in stark contrast to how programs for talk
coordinators have been developed in the past and it is my opinion that
developing these important programs with an open source model is both
productive and beneficial for the end user.

Not sure what open source software means? The following video gives a
basic overview of the open source
model. [Open Source Basics](https://www.youtube.com/watch?v=Tyd0FO0tko8)


##Note

pyTalkManager is not affiliated with the [Watch Tower Bible and Tract Society of Pennsylvania](http://www.JW.org).
