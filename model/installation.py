#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model for an installation
"""

class Installation:

    def __init__(self, number, name, address, zipCode, city, latitude, longitude):
        self.number = number
        self.name = name
        self.address = address
        self.zipCode = zipCode
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
