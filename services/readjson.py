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


    def read_activities(self, path):
        """
        Reads a JSON file which contains data for the activities

        >>> reader = ReadJSON()
        >>> activities = reader.read_activities("data/test_activite.json")
        >>> (activities[0].number, activities[0].name, activities[0].equipment_number)
        ('3501', 'Gymnastique volontaire', ' 213704')
        """
        file = open(path)
        data = json.load(file)
        result = []

        pbar = ProgressBar(widgets=['Reading activities JSON: ', Percentage(), ' ', ETA()])
        for line in pbar(data["data"]):
            result.append(Activity(line["ActCode"], line["ActLib"], line["EquipementId"]))

        return result


    def read_equipments(self, path):
        """
        Reads a JSON file which contains data for the equipments

        >>> reader = ReadJSON()
        >>> equipments = reader.read_equipments("data/test_equipements.json")
        >>> (equipments[0].number, equipments[0].name, equipments[0].installation_number)
        ('225442', "Carrière d'été", '490260005')
        """
        file = open(path)
        data = json.load(file)
        result = []

        pbar = ProgressBar(widgets=['Reading equipments JSON: ', Percentage(), ' ', ETA()])
        for line in pbar(data["data"]):
            result.append(Equipment(line["EquipementId"], line["EquNom"], line["InsNumeroInstall"]))

        return result


    def read_installations(self, path):
        """
        Reads a JSON file which contains data for the installations

        >>> reader = ReadJSON()
        >>> installations = reader.read_installations("data/test_installations.json")
        >>> (installations[0].number, installations[0].name, installations[0].address, installations[0].zip_code, installations[0].city, installations[0].latitude, installations[0].longitude)
        ('440010002', 'Terrain de Sports', 'Le Bois Vert', '44170', 'Abbaretz', 47.552265, -1.532627)
        """
        file = open(path)
        data = json.load(file)
        result = []

        pbar = ProgressBar(widgets=['Reading installations JSON: ', Percentage(), ' ', ETA()])
        for line in pbar(data["data"]):
            if str(line["InsNoVoie"]) == "None":
                result.append(Installation(line["InsNumeroInstall"], line["geo"]["name"], str(line["InsLibelleVoie"]), line["InsCodePostal"], line["ComLib"], line["Latitude"], line["Longitude"]))
            else:
                result.append(Installation(line["InsNumeroInstall"], line["geo"]["name"], str(line["InsNoVoie"]) + " " + str(line["InsLibelleVoie"]), line["InsCodePostal"], line["ComLib"], line["Latitude"], line["Longitude"]))

        return result
