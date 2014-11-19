__author__ = 'Joel Montes de Oca'

import gui.CongregationWindow as CongWindow
from db import DB

class Congregation:


    def get_list(self):

        sql = "SELECT name from Congregation"

        list = DB.return_pass_sql(None, sql)

        return list