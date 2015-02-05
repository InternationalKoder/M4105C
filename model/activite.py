#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Model for an activity
"""

class Activite:

    def __init__(self, insee, city, equipmentCardId, numberIdenticEquipments, codeActivity, labelActivity, practicable, practiced, inSpecializedHall, practicedLevel):
        self.insee = insee
        self.city = city
        self.equipmentCardId = equipmentCardId
        self.numberIdenticEquipments = numberIdenticEquipments
        self.codeActivity = codeActivity
        self.labelActivity = labelActivity
        self.practicable = practicable
        self.practiced = practiced
        self.inSpecialisableHall = inSpecialisableHall
        self.practicedLevel = practicedLevel
