#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main file which executes the program
"""

from services.readjson import ReadJSON
from services.database import Database

from model.activity import Activity
from model.installation import Installation
from model.equipment import Equipment


print("Creating database...", end=" ")
database = Database("data/database.db")
database.createNew()
print("Done")

print("Reading installations JSON...", end=" ")
rj = ReadJSON()
rj.readInstallations("data/Installations.json")
print("Done")
print("Writing installations to the database...", end=" ")

for elem in rj.result:
    database.insertInstallation(elem)
database.commit()
print("Done")


print("Reading activities JSON...", end=" ")
rj = ReadJSON()
rj.readActivities("data/Activites.json")
print("Done")

print("Writing activities to the database...", end=" ")
for elem in rj.result:
    database.insertActivity(elem)
database.writeActivities()
database.commit()
print("Done")


print("Reading equipments JSON...", end=" ")
rj = ReadJSON()
rj.readEquipments("data/Equipements.json")
print("Done")

print("Writing equipments to the database...", end=" ")
for elem in rj.result:
    database.insertEquipment(elem)
database.commit()
print("Done")

database.close()

print('Finished')


