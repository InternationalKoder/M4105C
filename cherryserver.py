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


    def addHTMLHeader(self, title):
        html = '''<!DOCTYPE html>\n<html>\n
        <head>\n<title>''' + title + '''</title>\n<meta charset="utf-8"/>\n</head>\n
        <body>'''
        return html


    def addHTMLFooter(self):
        return '</body>\n</html>'


    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        html = self.addHTMLHeader('Accueil')
        html += '''<h1>Installations Sportives des Pays de la Loire</h1>
        <a href="showInstallations">Voir les installations</a>'''
        html += self.addHTMLFooter()
        return html


    @cherrypy.expose
    def showInstallations(self):
        """
        Shows all the installations from the database
        """
        html = self.addHTMLHeader('Accueil')
        database = Database("data/database.db")
        installations = database.readInstallations()
        html += '<table>\n<tr><th>Numéro</th><th>Nom</th><th>Adresse</th><th>Code postal</th><th>Ville</th><th>Latitude</th><th>Longitude</th></tr>\n'
        for inst in installations:
            html += '<tr><td>' + str(inst.number) + '</td><td>' + inst.name + '</td><td>' + inst.address + '</td><td>' + str(inst.zipCode) + '</td><td>' + inst.city + '</td><td>' + str(inst.latitude) + '</td><td>' + str(inst.longitude) + '</td></tr>\n'

        html += '</table>\n'
        html += self.addHTMLFooter()

        return html

 
cherrypy.quickstart(WebManager()) 
