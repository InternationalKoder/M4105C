#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This class can be used to create a database and to do operations on it
"""

import sqlite3
from model.installation import Installation
from model.equipment import Equipment
from model.activity import Activity

class Database:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.path = path
        

    def create_new(self):
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


    def insert_installation(self, inst):
        """
        Inserts an installation in the 'installations' table
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO installations VALUES(:number, :name, :address, :zip_code, :city, :latitude, :longitude)',
                  {'number':inst.number, 'name':inst.name, 'address':inst.address, 'zip_code':inst.zip_code, 'city':inst.city, 'latitude':inst.latitude, 'longitude':inst.longitude})


    def insert_equipment(self, equip):
        """
        Inserts an equipment in the 'equipements' table
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO equipements VALUES(:number, :name, :installationNumber)',
                  {'number':equip.number, 'name':equip.name, 'installationNumber':equip.installation_number})


    def insert_activity(self, activ):
        """
        Inserts an activity in the 'activites_temp' table
        You must call this method for all the lines you want to insert, and then call the 'writeActivities' method to finish the insertion
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO activites_temp VALUES(:number, :name, :numberEquipment)',
                  {'number':activ.number, 'name':activ.name, 'numberEquipment':activ.equipment_number})


    def write_activities(self):
        """
        Writes all the activities from 'activites_temp' to 'activites'
        """
        c = self.conn.cursor()
        c.execute('INSERT INTO activites(numero, nom) SELECT numero, nom FROM activites_temp GROUP BY numero')
        c.execute('INSERT INTO equipements_activites(numero_equipement, numero_activite) SELECT numero_equipement, numero FROM activites_temp GROUP BY numero')
        c.execute("DROP TABLE IF EXISTS activites_temp")


    def read_installations(self):
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


    def read_installation(self, number):
        """
        Reads the installation which has the given number from the 'installations' table
        """
        c = self.conn.cursor()
        c.execute('SELECT * FROM installations WHERE numero = :numero', {'numero':number})
        row = c.fetchone()

        try:
            installation = Installation(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        except TypeError:
            return '<h2>Aucune installation ne correspond à ce numéro</h2>'

        return installation


    def read_equipments(self):
        """
        Reads all the equipments from the 'equipements' table
        """
        c = self.conn.cursor()
        c.execute('SELECT * FROM equipements')
        rows = c.fetchall()
        equipments = []

        for row in rows:
            equipments.append(Equipment(row[0], row[1], row[2]))

        return equipments


    def read_equipment(self, number):
        """
        Reads the equipment which has the given number from the 'equipments' table
        """
        c = self.conn.cursor()
        c.execute('SELECT * FROM equipements WHERE numero = :numero', {'numero':number})
        row = c.fetchone()

        try:
            equipment = Equipment(row[0], row[1], row[2])
        except TypeError:
            return '<h2>Aucun équipement ne correspond à ce numéro</h2>'

        return equipment


    def read_activities(self):
        """
        Reads all the activities from the 'activites' table
        """
        c = self.conn.cursor()
        c.execute('SELECT ac.numero, ac.nom, aceq.numero_equipement FROM activites ac, equipements_activites aceq WHERE ac.numero = aceq.numero_activite')
        rows = c.fetchall()
        activities = []

        for row in rows:
            activities.append(Activity(row[0], row[1], row[2]))

        return activities


    def read_activity(self, number):
        """
        Reads the activity which has the given number from the 'activites' table
        """
        c = self.conn.cursor()
        c.execute('SELECT ac.numero, ac.nom, aceq.numero_equipement FROM activites ac, equipements_activites aceq WHERE ac.numero = aceq.numero_activite AND ac.numero = :numero', {'numero':number})
        row = c.fetchone()

        try:
            activity = Activity(row[0], row[1], row[2])
        except TypeError:
            return '<h2>Aucune activité ne correspond à ce numéro</h2>'

        return activity


    def get_infos(self, activity_name, city):
        """
        Gives all the installations, equipments and activities which match the given activity and city
        """
        c = self.conn.cursor()
        c.execute("""SELECT i.numero, i.nom, e.numero, e.nom, a.numero, a.nom
        FROM installations i
        JOIN equipements e ON i.numero = e.numero_installation
        JOIN equipements_activites ea ON e.numero = ea.numero_equipement
        JOIN activites a ON ea.numero_activite = a.numero
        WHERE LOWER(i.ville) = LOWER('""" + city + """') AND a.nom LIKE '%""" + activity_name + """%'""")
        rows = c.fetchall()
        results = []

        for row in rows:
            results.append((Installation(row[0], row[1]), Equipment(row[2], row[3], row[0]), Activity(row[4], row[5], row[2])))

        return results


    def commit(self):
        self.conn.commit()


    def close(self):
        """
        Closes the connexion to the database
        """
        self.conn.close()
