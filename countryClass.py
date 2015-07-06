import csv

class Country:
    def __init__(self, countryName= "", currencyAlphabeticCode= "", currencyName =""):

        self.countryname = countryName
        self.currencyAlphabeticCode = currencyAlphabeticCode
        self.currencyName = currencyName

    def getcountryName(self):
        return self.countryName

    def getcurrencyAlphabeticCode(self):
        return self.currencyAlphabeticCode

    def getcurrencyName(self):
        return self.currencyName
    
def createCountry():
    with open('countrycurrency.csv', 'r', encoding="UTF8") as f:
        reader = csv.reader(f)
        countryCurrencyDict = {}
        for row in reader:
            countryCurrencyDict[row[0]] = Country(row[0], row[14],row[17])
    return countryCurrencyDict



##for key in countryCurrencyDict:
##     print(countryCurrencyDict[key].alphabetic_code)



##Have the distance between airports, to get exchange rate, Need to multiply the
##(origin airport.rate_to_euro) by the distance between them.
##
##so for this i need to check if origin airport letter codes coutnry name
##is equal to the country class country name


    
