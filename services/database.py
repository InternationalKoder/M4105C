#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This class can be used to create a database and to do operations on it
"""

import sqlite3
from model.installation import Installation

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
        c.execute("CREATE TABLE installations(numero INTEGER PRIMARY KEY, nom VARCHAR, adresse VARCHAR, code_postal VARCHAR, ville VARCHAR, latitude DECIMAL, longitude DECIMAL)")

        c.execute("DROP TABLE IF EXISTS equipements")
        c.execute("CREATE TABLE equipements(numero INTEGER PRIMARY KEY, nom VARCHAR, numero_installation VARCHAR, FOREIGN KEY(numero_installation) REFERENCES installations(numero))")

        c.execute("DROP TABLE IF EXISTS activites")
        c.execute("CREATE TABLE activites(numero INTEGER PRIMARY KEY, nom VARCHAR)")

        c.execute("DROP TABLE IF EXISTS activites_temp")
        c.execute("CREATE TABLE activites_temp(numero INTEGER, nom VARCHAR, numero_equipement INTEGER)")

        c.execute("DROP TABLE IF EXISTS equipements_activites")
        c.execute("CREATE TABLE equipements_activites(numero_equipement INTEGER, numero_activite INTEGER, FOREIGN KEY(numero_equipement) REFERENCES equipements(numero), FOREIGN KEY(numero_activite) REFERENCES activites(numero))")
        
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
        Inserts an activity in the 'activites_temp' table
        You must call this method for all the lines you want to insert, and then call the 'writeActivities' method to finish the insertion
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO activites_temp VALUES(:number, :name, :numberEquipment)',
                  {'number':activ.number, 'name':activ.name, 'numberEquipment':activ.numberEquipment})


    def writeActivities(self):
        """
        Writes all the activities from 'activites_temp' to 'activites'
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO activites(numero, nom) SELECT numero, nom FROM activites_temp GROUP BY numero')
        c.execute('INSERT INTO equipements_activites(numero_equipement, numero_activite) SELECT numero, numero_equipement FROM activites_temp GROUP BY numero')
        c.execute("DROP TABLE IF EXISTS activites_temp")


    def readInstallations(self):
        """
        Reads all the installations from the 'installations' table
        """
        c = self.conn.cursor()
        c.execute('SELECT * FROM installations')
        rows = c.fetchall()
        installations = []

        for row in rows:
            installations.append(Installation(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        return installations


    def commit(self):
        self.conn.commit()


    def close(self):
        """
        Closes the connexion to the database
        """
        self.conn.close()
