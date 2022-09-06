from xmlrpc.client import DateTime
from flask import Flask, jsonify, request
import json
from flask_restful import Resource, Api, reqparse, abort
import random,radar,datetime,time,sys,requests

from dgen import *
app = Flask(__name__)
api = Api(app)
beacons=f
class BeaconsList(Resource):
	def get(self):
		return beacons

class Home(Resource):

	def get(self):

		return beacons

	
	def post(self):

		f = request.get_json()   
		f = jsonify(f)
		
	for i in f:
            for x,y in i.items():

                a=("Beaconid :",i["Beaconid"], "date :",i["date"],"Temperaturedata :",i["Temperaturedata"]["temperature"])
                b=("Beaconid :",i["Beaconid"], "date :",i["date"],"Temperaturedata :",i["Batterydata"]["batterydata"])
            print(a)
            print(b)
			  
	     



# adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(BeaconsList, '/beaconslist')



# driver function
if __name__ == '__main__':

	app.run(debug = True)

