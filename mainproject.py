import csv
import airportClass
import currencyClass
import countryClass
from math import pi, sin, cos, acos, radians, atan2, sqrt
import itertools
import tkinter
from tkinter import *
from tkinter import filedialog



#creates the lookup dictionaries for airports, countrys and currencies
airportLookupDict = airportClass.createAirport()
countryCurrencyDict = countryClass.createCountry()
currencyRatesDict = currencyClass.createCurrency()

#this function takes origin and destination variables and uses them to get their
#longtitude and latitude values. It then passes them to get the distance
#between the airports.

def getDistanceBetweenAirports(origin,destination):
    
    lat_1 = float(airportLookupDict[origin].getlat())
    long_1 = float(airportLookupDict[origin].getlong())

    lat_2 = float(airportLookupDict[destination].getlat())
    long_2 = float(airportLookupDict[destination].getlong())
    
    distance = getDistanceBetweenCoordinates(lat_1,long_1,lat_2,long_2)
    #print ("The distance between", origin, "and", destination, "is: " ,distance)
    return distance
           

def getDistanceBetweenCoordinates(lat_1,long_1,lat_2,long_2):
    Radius = 6371.0 #radius of the earth

    lat1 = radians(lat_1) #turns longitude and latitude values to radians
    lon1 = radians(long_1)
    lat2 = radians(lat_2)
    lon2 = radians(long_2)

    diffLon = lon2 - lon1
    diffLat = lat2 - lat1
    a = (sin(diffLat/2))**2 + cos(lat1) * cos(lat2) * (sin(diffLon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = Radius * c
    return distance
    

def getRate(origin): #gets the rate to euro from the lookup dictionaries
    countryName = airportLookupDict[origin].getcountryname()
    currencyAlphabeticCode = countryCurrencyDict[countryName].getcurrencyAlphabeticCode()    
    rate = float(currencyRatesDict[currencyAlphabeticCode].getrateToEuro())
    return rate            

def exchangeRate(rate, distance): #gets cost of each journey
    cost = float(distance * rate)
    return cost
    

#takes a route and calculates the distance between each airport in sequence
#and records a total cost for each route 
def calculateRouteCost(route):
    costList= []
    
    for i in range(len(route)-1):
        origin = route[i]
        destination = route[i+1]
        distance = getDistanceBetweenAirports(origin,destination)
        rate = float(getRate(origin))
        cost = int(exchangeRate(rate, distance))
        costList.append(cost)
    
    totalCost = 0
       
    for item in costList: 
        totalCost += item #adds each leg cost together for totalCost
        
    bestOption = [route, totalCost] #saves the route and cost
    return bestOption


#this takes airportList as parameter, finds permutations and stores them into a
#list of routes called possibleRoutes
def findPossibleRoutes(airportList):
    routes = list(itertools.permutations(airportList[2:6]))
    possibleRoutes = []
    cheapestRoute = []
    for route in routes:
        route = list(route)
        route.insert(0, airportList[1])
        route.append(airportList[1])
        possibleRoutes.append(route)

#extra airport permutations, creates with each of the different airports
#added on as extra
    extraAirport1 = airportList[2:6]
    extraAirport1.append(airportList[1])
    
    extraAirport2 = airportList[2:6]
    extraAirport2.append(airportList[2])
    
    extraAirport3 = airportList[2:6]
    extraAirport3.append(airportList[3])
    
    extraAirport4 = airportList[2:6]
    extraAirport4.append(airportList[4])
    
    extraAirport5 = airportList[2:6]
    extraAirport5.append(airportList[5])

#create a new list "extraPermutaions" and add all of the permutations
#for the different extraAirports to that list"
    extraPermutations = []
    extraPermutations += list(itertools.permutations(extraAirport1))
    extraPermutations += list(itertools.permutations(extraAirport2))
    extraPermutations += list(itertools.permutations(extraAirport3))
    extraPermutations += list(itertools.permutations(extraAirport4))
    extraPermutations += list(itertools.permutations(extraAirport5))

#this inserts the home airport at the start and end of every permutaion
    for route in extraPermutations:
        route = list(route)
        route.insert(0, airportList[1])
        route.append(airportList[1])
        possibleRoutes.append(route)
    
    return possibleRoutes
           
    
def getAirportList():
    airportList = []

    name = input("Enter your name: ").capitalize()
    airportList.append(name)
    while True:
        home = input("Please enter your home airport: ").upper()
        if home not in airportLookupDict:
            print("That is not a recognizable airport code. Enter again")
            home
        else:
            airportList.append(home)
            break
    while True:
        air1 = input("Please enter your 1st airport: ").upper()
        if air1 not in airportLookupDict:
            print("That is not a recognizable airport code. Enter again")
            air1
        else:
            airportList.append(air1)
            break
    while True:
        air2 = input("Please enter your 2nd airport: ").upper()
        if air2 not in airportLookupDict:
            print("That is not a recognizable airport code. Enter again")
            air2
        else:
            airportList.append(air2)
            break
    while True:
        air3 = input("Please enter your 3rd airport: ").upper()
        if air3 not in airportLookupDict:
            print("That is not a recognizable airport code. Enter again")
            air3
        else:
            airportList.append(air3)
            break
    while True:      
        air4 = input("Please enter your 4th airport: ").upper()
        if air4 not in airportLookupDict:
            print("That is not a recognizable airport code. Enter again")
            air4
        else:
            airportList.append(air4)
            print(airportList)
            break
    return airportList
        
        
def calculateCheapestRoute(airportList):
    possibleRoutes = findPossibleRoutes(airportList)
    cheapestRoute = []
    for route in possibleRoutes:
        cheapestRoute.append(calculateRouteCost(route)) #this calculates cost of each route
    cheapest = cheapestRoute[0]
    for route in cheapestRoute: 
        if route[1] < cheapest[1]: #iterates through list and makes lowest the new cheapest
            cheapest = route
    results = "The best route for " + str(airportList[0]) + " is: " + str(cheapest[0]) + " which costs: €" + str(cheapest[1])
    print(results)
    return results
    

def menuOptions():
    print("Options: ")
    print("'A' -- Enter your own details")
    print("'B' -- Input from a file")
    print("'M' -- Menu Options")
    print("'Q' -- Quit the program")

def getFileName():
    
    fileName = tkinter.filedialog.askopenfilename()
    results = open("results.txt", "w")
    with open(fileName, 'r', encoding="UTF8") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                airportList = row
                results.write(calculateCheapestRoute(airportList) + "\n")
            except KeyError:
                print("There is an error with route:",airportList," cannot calculate distance")
                results.write("There is an error with route:"+ str(airportList) + " cannot calculate distance" + "\n")            
    print("\n File : results.txt has been created \n")
    
            
def main():
    choice = "M"
    while choice != "Q":
        if choice == "A":
            airportList = getAirportList()
            calculateCheapestRoute(airportList)
            menuOptions()
            choice = input("Choose another option: ").upper()
        elif choice == "B":
            getFileName()
            menuOptions()
            choice = input("Choose another option: ").upper()
        elif choice != "Q":
            menuOptions()
            choice = input("Choose an option: ").upper()

main()
