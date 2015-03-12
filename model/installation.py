#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model for an installation
"""

class Installation:

    def __init__(self, number, name, address, zip_code, city, latitude, longitude):
        self.number = number
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
