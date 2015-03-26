#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program is a web server which allows to display a database's content
"""

import cherrypy
from services.database import Database

from mako.template import Template
from mako.lookup import TemplateLookup 

from model.activity import Activity
from model.installation import Installation
from model.equipment import Equipment


lookup = TemplateLookup(directories=[""])

class WebManager(object):
    """
    Exposes web services
    """

    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """     
        return Template(filename="view/index.html", lookup=lookup).render()


    @cherrypy.expose
    def show_installations(self):
        """
        Shows all the installations from the database
        """
        database = Database('data/database.db')
        installations = database.read_installations()
        view = Template(filename="view/template.html", lookup=lookup)
        
 
        return view.render(
            rows = [[item.number, item.name, item.address, item.zip_code, item.city, item.latitude, item.longitude] for item in installations],
            pageTitle = "Installations",
            tableTitle = "Liste de toutes les installations",
            ths = ["Numéro", "Nom", "Adresse", "Code postal", "Ville", "Latitude", "Longitude"]
        )


    @cherrypy.expose
    def show_equipments(self):
        """
        Shows all the equipments from the database
        """        
        database = Database('data/database.db')
        equipments = database.read_equipments()
        view = Template(filename="view/template.html", lookup=lookup)
        
 
        return view.render(
            rows = [[item.number, item.name, item.installation_number] for item in equipments],
            pageTitle = "Équipements",
            tableTitle = "Liste de tous les équipements",
            ths = ["Numéro", "Nom", "Numéro d'installation"]
        ) 
        


    @cherrypy.expose
    def show_activities(self):
        """
        Shows all the activities from the database
        """      
        database = Database('data/database.db')
        activities = database.read_activities()
        view = Template(filename="view/template.html", lookup=lookup)
        
 
        return view.render(
            rows = [[item.number, item.name] for item in activities],
            pageTitle = "Activités",
            tableTitle = "Liste de toutes les activités",
            ths = ["Numéro", "Nom"]
        ) 


    @cherrypy.expose
    def show_installation(self, number):
        """
        Shows the installation which has the given number from the database
        """    
        database = Database('data/database.db')
        inst = database.read_installation(number)
        view = Template(filename="view/template.html", lookup=lookup)

        try:
            render = view.render(
                rows = [[inst.number, inst.name, inst.address, inst.zip_code, inst.city, inst.latitude, inst.longitude]],
                pageTitle = "Installation " + number,
                tableTitle = "Installation " + number,
                ths = ["Numéro", "Nom", "Adresse", "Code postal", "Ville", "Latitude", "Longitude"]
            )
        except AttributeError:
            render = view.render(
                rows = [],
                pageTitle = "Installation " + number,
                tableTitle = "Installation " + number,
                ths = ["Numéro", "Nom", "Adresse", "Code postal", "Ville", "Latitude", "Longitude"]
            )
 
        return render


    @cherrypy.expose
    def show_equipment(self, number):
        """
        Shows the equipment which has the given number from the database
        """
        database = Database('data/database.db')
        equip = database.read_equipment(number)
        view = Template(filename="view/template.html", lookup=lookup)

        try:
            render = view.render(
                rows = [[equip.number, equip.name, equip.installation_number]],
                pageTitle = "Équipement " + number,
                tableTitle = "Équipement " + number,
                ths = ["Numéro", "Nom", "Numéro d'installation"]
            )
        except AttributeError:
            render = view.render(
                rows = [],
                pageTitle = "Équipement " + number,
                tableTitle = "Équipement " + number,
                ths = ["Numéro", "Nom", "Numéro d'installation"]
            )
 
        return render


    @cherrypy.expose
    def show_activity(self, number):
        """
        Shows the activity which has the given number from the database
        """
        database = Database('data/database.db')
        activ = database.read_activity(number)
        view = Template(filename="view/template.html", lookup=lookup)

        try:
            render = view.render(
                rows = [[activ.number, activ.name]],
                pageTitle = "Activité " + number,
                tableTitle = "Activité " + number,
                ths = ["Numéro", "Nom"]
            )
        except AttributeError:
            render = view.render(
                rows = [],
                pageTitle = "Activité " + number,
                tableTitle = "Activité " + number,
                ths = ["Numéro", "Nom"]
            )
 
        return render


    @cherrypy.expose
    def find_infos(self, activity_name, city):
        """
        Shows all the installations, equipments and activities which match the given activity and city
        """
        database = Database('data/database.db')
        infos = database.get_infos(activity_name, city)
        view = Template(filename="view/template.html", lookup=lookup)

        try:
            render = view.render(
                rows = [[item[0].number, item[0].name, item[1].number, item[1].name, item[2].number, item[2].name] for item in infos],
                pageTitle = "Informations pour " + activity_name + " à " + city,
                tableTitle = "Informations pour " + activity_name + " à " + city,
                ths = ["Numéro d'installation", "Nom d'installation", "Numéro d'équipement", "Nom d'équipement", "Numéro d'activité", "Nom d'activité"]
            )
        except AttributeError:
            render = view.render(
                rows = [],
                pageTitle = "Informations pour " + activity_name + " à " + city,
                tableTitle = "Informations pour " + activity_name + " à " + city,
                ths = ["Numéro d'installation", "Nom d'installation", "Numéro d'équipement", "Nom d'équipement", "Numéro d'activité", "Nom d'activité"]
            )
 
        return render

 
cherrypy.quickstart(WebManager()) 
