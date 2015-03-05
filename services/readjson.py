#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Allows to read a JSON file
"""

import json
from model.activity import Activity
from model.installation import Installation
from model.equipment import Equipment

class ReadJSON:

    def __init__(self):
        self.result = []


    def readActivities(self, path):
        file = open(path)
        data = json.load(file)

        for line in data["data"]:
            self.result.append(Activity(line["ActCode"], line["ActLib"], line["EquipementId"]))


    def readEquipments(self, path):
        file = open(path)
        data = json.load(file)

        for line in data["data"]:
            self.result.append(Equipment(line["EquipementId"], line["EquNom"], line["InsNumeroInstall"]))


    def readInstallations(self, path):
        file = open(path)
        data = json.load(file)

        for line in data["data"]:
            self.result.append(Installation(line["InsNumeroInstall"], line["geo"]["name"], str(line["InsNoVoie"]) + " " + str(line["InsLibelleVoie"]), line["InsCodePostal"], line["ComLib"], line["Latitude"], line["Longitude"]))
