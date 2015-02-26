#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main file which executes the program
"""

from services.readjson import ReadJSON
from model.activity import Activity

rj = ReadJSON("data/Installations.json")
rj.readInstallations()
result = rj.result

for elem in result:
    print(elem.number, " ; ", elem.name, " ; ", elem.address, " ; ", elem.zipCode, " ; ", elem.city, " ; ", elem.latitude, " ; ", elem.longitude)
