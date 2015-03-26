#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Allows to read a JSON file
"""

import json
from progressbar import *
from model.activity import Activity
from model.installation import Installation
from model.equipment import Equipment

class ReadJSON:

    def __init__(self):
        self.result = []


    def read_activities(self, path):
        """
        Reads a JSON file which contains data for the activities
        """
        file = open(path)
        data = json.load(file)

        pbar = ProgressBar(widgets=['Reading activities JSON: ', Percentage(), ' ', ETA()])
        for line in pbar(data["data"]):
            self.result.append(Activity(line["ActCode"], line["ActLib"], line["EquipementId"]))


    def read_equipments(self, path):
        """
        Reads a JSON file which contains data for the equipments
        """
        file = open(path)
        data = json.load(file)

        pbar = ProgressBar(widgets=['Reading equipments JSON: ', Percentage(), ' ', ETA()])
        for line in pbar(data["data"]):
            self.result.append(Equipment(line["EquipementId"], line["EquNom"], line["InsNumeroInstall"]))


    def read_installations(self, path):
        """
        Reads a JSON file which contains data for the installations
        """
        file = open(path)
        data = json.load(file)

        pbar = ProgressBar(widgets=['Reading installations JSON: ', Percentage(), ' ', ETA()])
        for line in pbar(data["data"]):
            self.result.append(Installation(line["InsNumeroInstall"], line["geo"]["name"], str(line["InsNoVoie"]) + " " + str(line["InsLibelleVoie"]), line["InsCodePostal"], line["ComLib"], line["Latitude"], line["Longitude"]))
