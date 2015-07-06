import csv



# make the airport class - give constructor the values below.
class Airport:
    def __init__(self, airportname="", cityname="", countryname="", code3="",lat=0,long=0):

        self.airportname = airportname
        self.cityname = cityname
        self.countryname = countryname
        self.code3 = code3
        self.lat = lat
        self.long = long

    def getairportname(self):
        return self.airportname

    def getcityname(self):
        return self.cityname

    def getcountryname(self):
        return self.countryname

    def getcode3(self):
        return self.code3

    def getlat(self):
        return self.lat

    def getlong(self):
        return self.long

def createAirport():
    with open('airport.csv', 'r', encoding="UTF8") as f:
        reader = csv.reader(f)
        airportLookupDict = {}
        for row in reader:
            airportLookupDict[row[4]] = Airport(row[1], row[2],row[3], row[4],row[6],row[7])
    return airportLookupDict      
