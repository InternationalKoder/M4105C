#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program is a web server which allows to display a database's content
"""

import cherrypy
from services.database import Database

from model.activity import Activity
from model.installation import Installation
from model.equipment import Equipment


class WebManager(object):
    """
    Exposes web services
    """


    def add_HTML_header(self, title):
        html = '''<!DOCTYPE html>\n<html>\n
        <head>\n<title>''' + title + '''</title>\n<meta charset="utf-8"/>\n</head>\n
        <body>'''
        return html


    def add_HTML_footer(self):
        return '</body>\n</html>'


    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        html = self.add_HTML_header('Accueil')
        html += '''<h1>Installations Sportives des Pays de la Loire</h1>\n
        <a href="show_installations">Voir les installations</a><br/>\n
        <a href="show_equipments">Voir les équipements</a><br/>\n
        <a href="show_activities">Voir les activités</a>'''
        html += self.add_HTML_footer()
        return html


    @cherrypy.expose
    def show_installations(self):
        """
        Shows all the installations from the database
        """
        html = self.add_HTML_header('Installations')
        database = Database('data/database.db')
        installations = database.read_installations()
        html += '<table>\n<tr><th>Numéro</th><th>Nom</th><th>Adresse</th><th>Code postal</th><th>Ville</th><th>Latitude</th><th>Longitude</th></tr>\n'
        for inst in installations:
            html += '<tr><td>' + str(inst.number) + '</td><td>' + inst.name + '</td><td>' + inst.address + '</td><td>' + str(inst.zip_code) + '</td><td>' + inst.city + '</td><td>' + str(inst.latitude) + '</td><td>' + str(inst.longitude) + '</td></tr>\n'

        html += '</table>\n'
        html += self.add_HTML_footer()

        return html


    @cherrypy.expose
    def show_equipments(self):
        """
        Shows all the equipments from the database
        """
        html = self.add_HTML_header('Équipements')
        database = Database('data/database.db')
        equipments = database.read_equipments()
        html += '<table>\n<tr><th>Numéro</th><th>Nom</th><th>Numéro d\'installation</th></tr>\n'
        for equip in equipments:
            html += '<tr><td>' + str(equip.number) + '</td><td>' + equip.name + '</td><td>' + str(equip.installation_number) + '</td></tr>\n'

        html += '</table>\n'
        html += self.add_HTML_footer()

        return html


    @cherrypy.expose
    def show_activities(self):
        """
        Shows all the activities from the database
        """
        html = self.add_HTML_header('Activités')
        database = Database('data/database.db')
        activities = database.read_activities()
        html += '<table>\n<tr><th>Numéro</th><th>Nom</th><th>Numéro d\'équipement</th></tr>\n'
        for activ in activities:
            html += '<tr><td>' + str(activ.number) + '</td><td>' + activ.name + '</td><td>' + str(activ.equipment_number) + '</td></tr>\n'

        html += '</table>\n'
        html += self.add_HTML_footer()

        return html


    @cherrypy.expose
    def show_installation(self, number):
        """
        Shows the installation which has the given number from the database
        """
        html = self.add_HTML_header('Installation ' + number)
        database = Database('data/database.db')
        inst = database.read_installation(number)
        html += '<table>\n<tr><th>Numéro</th><th>Nom</th><th>Adresse</th><th>Code postal</th><th>Ville</th><th>Latitude</th><th>Longitude</th></tr>\n'

        try:
            html += '<tr><td>' + str(inst.number) + '</td><td>' + inst.name + '</td><td>' + inst.address + '</td><td>' + str(inst.zip_code) + '</td><td>' + inst.city + '</td><td>' + str(inst.latitude) + '</td><td>' + str(inst.longitude) + '</td></tr>\n'
        except AttributeError:
            html = self.add_HTML_header('Installation non trouvée') + inst

        html += '</table>\n'
        html += self.add_HTML_footer()

        return html


    @cherrypy.expose
    def show_equipment(self, number):
        """
        Shows the equipment which has the given number from the database
        """
        html = self.add_HTML_header('Équipement ' + number)
        database = Database('data/database.db')
        equip = database.read_equipment(number)
        html += '<table>\n<tr><th>Numéro</th><th>Nom</th><th>Numéro d\'installation</th></tr>\n'

        try:
            html += '<tr><td>' + str(equip.number) + '</td><td>' + equip.name + '</td><td>' + str(equip.installation_number) + '</td></tr>\n'
        except AttributeError:
            html = self.add_HTML_header('Équipement non trouvé') + equip

        html += '</table>\n'
        html += self.add_HTML_footer()

        return html


    @cherrypy.expose
    def show_activity(self, number):
        """
        Shows the activity which has the given number from the database
        """
        html = self.add_HTML_header('Activité ' + number)
        database = Database('data/database.db')
        activ = database.read_activity(number)
        html += '<table>\n<tr><th>Numéro</th><th>Nom</th><th>Numéro d\'équipement</th></tr>\n'

        try:
            html += '<tr><td>' + str(activ.number) + '</td><td>' + activ.name + '</td><td>' + str(activ.equipment_number) + '</td></tr>\n'
        except AttributeError:
            html = self.add_HTML_header('Activité non trouvée') + activ

        html += '</table>\n'
        html += self.add_HTML_footer()

        return html

 
cherrypy.quickstart(WebManager()) 
