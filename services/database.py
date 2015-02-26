#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This class can be used to create a database and to do operations on it
"""

import sqlite3

class Database:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.path = path
        

    def createNew(self):
        """
        Creates a new database to the path given in the constructor
        """
        c = self.conn.cursor()

        c.execute("DROP TABLE IF EXISTS installations")
        c.execute("CREATE TABLE installations(numero INTEGER, nom VARCHAR, adresse VARCHAR, code_postal VARCHAR, ville VARCHAR, latitude DECIMAL, longitude DECIMAL)")

        c.execute("DROP TABLE IF EXISTS equipements")
        c.execute("CREATE TABLE equipements(numero INTEGER, nom VARCHAR, numero_installation VARCHAR)")

        c.execute("DROP TABLE IF EXISTS activites")
        c.execute("CREATE TABLE activites(numero INTEGER, nom VARCHAR)")
        
        self.commit()


    def insertInstallation(self, inst):
        """
        Inserts an installation in the 'installations' table
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO installations VALUES(:number, :name, :address, :zipCode, :city, :latitude, :longitude)',
                  {'number':inst.number, 'name':inst.name, 'address':inst.address, 'zipCode':inst.zipCode, 'city':inst.city, 'latitude':inst.latitude, 'longitude':inst.longitude})


    def insertEquipment(self, equip):
        """
        Inserts an equipment in the 'equipements' table
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO equipements VALUES(:number, :name, :installationNumber)',
                  {'number':equip.number, 'name':equip.name, 'installationNumber':equip.installationNumber})


    def insertActivity(self, activ):
        """
        Inserts an activity in the 'activites' table
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO activites VALUES(:number, :name)',
                  {'number':activ.number, 'name':activ.name})


    def commit(self):
        self.conn.commit()


    def close(self):
        """
        Closes the connexion to the database
        """
        self.conn.close()
