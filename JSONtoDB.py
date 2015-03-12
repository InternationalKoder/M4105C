#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program reads data from JSON files and writes the results to a SQLite database
"""

from services.readjson import ReadJSON
from services.database import Database

from model.activity import Activity
from model.installation import Installation
from model.equipment import Equipment


print("Creating database...", end=" ")
database = Database("data/database.db")
database.create_new()
print("Done")

print("Reading installations JSON...", end=" ")
rj = ReadJSON()
rj.read_installations("data/Installations.json")
print("Done")
print("Writing installations to the database...", end=" ")

for elem in rj.result:
    database.insert_installation(elem)
database.commit()
print("Done")


print("Reading activities JSON...", end=" ")
rj = ReadJSON()
rj.read_activities("data/Activites.json")
print("Done")

print("Writing activities to the database...", end=" ")
for elem in rj.result:
    database.insert_activity(elem)
database.write_activities()
database.commit()
print("Done")


print("Reading equipments JSON...", end=" ")
rj = ReadJSON()
rj.read_equipments("data/Equipements.json")
print("Done")

print("Writing equipments to the database...", end=" ")
for elem in rj.result:
    database.insert_equipment(elem)
database.commit()
print("Done")

database.close()

print('Finished')


