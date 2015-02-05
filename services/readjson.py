#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Allows to read a JSON file
"""

import json

class Readjson:

    def __init__(self, path):
        self.file = open(path)
        self.result = []


    def read(self):
        data = json.load(self.file)

        for line in data["data"]:
            self.result.append(line["EquipementId"])


    def getResult(self):
        return self.result
