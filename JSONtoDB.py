#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program reads data from JSON files and writes the results to a SQLite database
"""

from progressbar import *

from services.readjson import ReadJSON
from services.database import Database

from model.activity import Activity
from model.installation import Installation
from model.equipment import Equipment


print("Creating database...", end=" ")
database = Database("data/database.db")
database.create_new()
print("Done")

rj = ReadJSON()
installations = rj.read_installations("data/Installations.json")

pbar = ProgressBar(widgets=['Writing installations to the database: ', Percentage(), ' ', ETA()])
for elem in pbar(installations):
    database.insert_installation(elem)
database.commit()


activities = rj.read_activities("data/Activites.json")

pbar = ProgressBar(widgets=['Writing activities to the database: ', Percentage(), ' ', ETA()])
for elem in pbar(activities):
    database.insert_activity(elem)
database.write_activities()
database.commit()


equipments = rj.read_equipments("data/Equipements.json")

pbar = ProgressBar(widgets=['Writing equipments to the database: ', Percentage(), ' ', ETA()])
for elem in pbar(equipments):
    database.insert_equipment(elem)
database.commit()

database.close()

print('Finished')


