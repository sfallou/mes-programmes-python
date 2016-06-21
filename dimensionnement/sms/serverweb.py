#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Created on 16-07-2015
 
@author: sfallou
'''
 
from http.server import HTTPServer, CGIHTTPRequestHandler
 
# Port du serveur http
port = 8081
# Allocation de l'objet de gestion du serveur
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
 
# On lance le serveur indéfiniement
print('Lancement du serveur http sur: http://localhost:' + str(httpd.server_port))
httpd.serve_forever()
