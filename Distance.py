# Distance = arccos (sin φ1 sin φ2 cos(θ1 - θ2) + cos φ1 cos φ2) * radius_of_earth
#Radius_of_earth=6373 km
#θ = degrees east of prime meridian (latitude)
# φ = 90 - longitude
# degrees to radians -> = angle * 2pi/360degrees

from math import *  # imports all the maths functions.

airport_key = {
    "JFK": ("John F Kennedy Intl","United States",40.639751,-73.778925),
    "AAL": ("Aalborg","Denmark",57.092789,9.849164),
    "CDG": ("Charles De Gaulle","France",49.012779,2.55),
    "SYD": ("Sydney Intl","Australia",-33.946111,151.177222),
    "LHR": ("Heathrow","United Kingdom",51.4775,-0.461389),
    "DUB": ("Dublin","Ireland",53.421333,-6.270075),
    "ARN": ("Arlanda","Sweden",59.651944,17.918611),
    "SIN": ("Changi Intl","Singapore",1.350189,103.994433),
    "AMS": ("Schiphol","Netherlands",52.308613,4.763889),
    "SFO": ("San Francisco Intl","United States",37.618972,-122.374889)

}

#create function that asks user for airport codes with exception handling
def get_airports():

    airport_1 = input("Enter your departure airport code: ").upper().strip()
    if airport_1 in airport_key:
        print("You have chosen", airport_1, "as your starting point.")
    else:
        print("That's not an airport key, Please try again.")
        return get_airports()
    airport_2 = input("Enter the destination airport code: ").upper().strip()
    if airport_2 in airport_key:
        print("You have chosen", airport_2,"as your destination.")
    else:
        print("That's not an airport key, Please try again.")
        return get_airports()
    if airport_1 == airport_2:
        print("Oh so you want to stay in the same airport do ye?. Don't waste my time! Try again")
        return get_airports()
    return airport_1, airport_2

#this function calculates the distance between co-ordinates
def getDistanceBetweenCoordinates(lat_1,long_1,lat_2,long_2):
    radius_of_earth = 6373
    θ1 = long_1 * (2*(pi)/360)
    θ2 = long_2 * (2*(pi)/360)
    φ1 = 90 - (lat_1 * (2*(pi)/360))
    φ2 = 90 - (lat_2 * (2*(pi)/360))


    distance = acos((sin(φ1))*(sin(φ2))*(cos(θ1 - θ2)) + (cos(φ1))*(cos(φ2))) * radius_of_earth
    print("The distance between your airports is : ", end="")
    return int(distance)

def getDistanceBetweenAirports(airport_1,airport_2):

    if airport_1 in airport_key:
        lat_1 = float(airport_key[airport_1][2])
        long_1 = float(airport_key[airport_1][3])


    if airport_2 in airport_key:
        lat_2 = float(airport_key[airport_2][2])
        long_2 = float(airport_key[airport_2][3])
    return getDistanceBetweenCoordinates(lat_1,long_1,lat_2,long_2)

airport_1, airport_2 = get_airports()
print(getDistanceBetweenAirports(airport_1,airport_2))

