This program uses data related to sport facilities from http://data.paysdelaloire.fr.

The JSONtoDB.py script reads JSON files and writes the data to a SQLite database. The JSON files must be placed in a "data" folder. The script uses the Progressbar python module : https://github.com/coagulant/progressbar-python3.

The cherryserver.py script starts a new HTTP server on the 8080 port. This server displays data from the database. The script uses the Cherrypy python module : https://github.com/cherrypy/cherrypy.
