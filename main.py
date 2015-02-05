#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main file which executes the program
"""

from services.database import Database

db = Database("data/installations.db", "installations")
db.createNew()
db.close()
