#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This class can be used to create a database and to do operations on it
"""

import sqlite3

class Database:

    def __init__(self, path, name):
        self.conn = sqlite3.connect(path)
        self.path = path
        self.name = name
        

    def createNew(self):
        c = self.conn.cursor()

        c.execute("DROP TABLE IF EXISTS " + self.name)
        c.execute("CREATE TABLE " + self.name + "(numero integer, nom text)")
        
        self.conn.commit()


    def close(self):
        """
        Closes the connexion to the database
        """
        self.conn.close()
