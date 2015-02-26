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

    def __init__(self, path):
        self.file = open(path)
        self.result = []


    def readActivities(self):
        data = json.load(self.file)

        for line in data["data"]:
            self.result.append(Activity(line["EquipementId"], line["ActLib"]))


    def readEquipments(self):
        data = json.load(self.file)

        for line in data["data"]:
            self.result.append(Equipment(line["EquipementId"], line["EquNom"], line["InsNumeroInstall"]))


    def readInstallations(self):
        data = json.load(self.file)

        for line in data["data"]:
            self.result.append(Installation(line["InsNumeroInstall"], line["geo"]["name"], str(line["InsNoVoie"]) + " " + str(line["InsLibelleVoie"]), line["InsCodePostal"], line["ComLib"], line["Latitude"], line["Longitude"]))
