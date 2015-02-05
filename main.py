#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main file which executes the program
"""

from services.readjson import Readjson
from model.activite import Activite

rj = Readjson("data/Activites.json")
rj.read()
print(rj.getResult())
