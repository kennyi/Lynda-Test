import csv
from math import *


# make the airport class - give constructor the values below.
class Airport:
    def __init__(self, airportname, cityname, countryname, code3,lat,long):

        self.airport_name = airportname
        self.city_name = cityname
        self.country_name = countryname
        self.airport_code = code3
        self.latitude = lat
        self.longitude = long

    def getDistanceBetweenCoordinates(lat_1,long_1,lat_2,long_2):
        radius_of_earth = 6373
        θ1 = long_1 * (2*(pi)/360)
        θ2 = long_2 * (2*(pi)/360)
        φ1 = 90 - (lat_1 * (2*(pi)/360))
        φ2 = 90 - (lat_2 * (2*(pi)/360))

        print(θ1,θ2,φ1,φ2)

        distance = int(acos((sin(φ1))*(sin(φ2))*(cos(θ1 - θ2)) + (cos(φ1))*(cos(φ2))) * radius_of_earth)
        print("The distance between your airports is : ",distance, end="")
        return distance
        

#also import the distance between airports calculator

    def getDistanceBetweenAirports(origin,destination):
        if origin in airportLookupDict[origin].airport_code:
            lat_1 = float(airportLookupDict[origin].latitude)
            long_1 = float(airportLookupDict[origin].longitude)


        if destination in airportLookupDict[destination].airport_code:
            lat_2 = float(airportLookupDict[destination].latitude)
            long_2 = float(airportLookupDict[destination].longitude)
        

        return Airport.getDistanceBetweenCoordinates(lat_1,long_1,lat_2,long_2)

    def get_airports():

        origin = input("Enter your departure airport code: ").upper().strip()
        if origin in airportLookupDict[origin].airport_code:
            print("You have chosen", origin, "as your starting point.")
        else:
            print("That's not an airport key, Please try again.")
            return get_airports()
        destination = input("Enter the destination airport code: ").upper().strip()
        if destination in airportLookupDict[destination].airport_code:
            print("You have chosen", destination,"as your destination.")
        else:
            print("That's not an airport key, Please try again.")
            return get_airports()
        if origin == destination:
            print("Oh so you want to stay in the same airport do ye?. Don't waste my time! Try again")
            return get_airports()
        return origin, destination

#bring in the calculate distance from co-ordinates





with open('airport.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)
    airportLookupDict = {}
    for row in reader:
        airportLookupDict[row[4]] = Airport(row[1], row[2],row[3], row[4],row[6],row[7])


##for key in airportLookupDict:
##     print(airportLookupDict[key].latitude, airportLookupDict[key].longitude)

##for key in airportLookupDict:
##     print(airportLookupDict[key].airport_code)

origin, destination = Airport.get_airports()    
Airport.getDistanceBetweenAirports(origin,destination)
