from db import DB

class Outline:
    def __init__(self):
        self.number = None
        self.title = None

    def set_attributes(self, number=None, title=None):
        """
        Sets the attributes for the outline module

        :param number: The outline number
        :param title: The title for the outline
        """

        self.number = number
        self.title = title


    def check_sanity():
	    """"
	    Checks to make sure data entered by the user confirms to what
	    is expected.  
	    """
	    pass

    def add_outline():
	    """
	    Sends content received to be added to the database.
	    """
	    pass
