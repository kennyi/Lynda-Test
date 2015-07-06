import csv


#make the currencyrate class - give constructor the values below

class Currency:
    def __init__(self, currencyName= "", currencyAlphabeticCode= "", rateToEuro= 0):

        self.currencyName = currencyName
        self.currencyAlphabeticCode = currencyAlphabeticCode
        self.rateToEuro = rateToEuro
        

    def getcurrencyname(self):
        return self.currencyname

    def getcurrencyAlphatbeticCode(self):
        return self.currencyAlphabeticCode

    def getrateToEuro(self):
        return self.rateToEuro


def createCurrency():
    with open('currencyrates.csv', 'r', encoding="UTF8") as f:
        reader = csv.reader(f)
        currencyRatesDict = {}
        for row in reader:
            currencyRatesDict[row[1]] = Currency(row[0], row[1],row[2])
    return currencyRatesDict

##for key in currencyRatesDict:
##     print(currencyRatesDict[key].rate_to_euro)

##for key in currencyRatesDict:
##     print(currencyRatesDict[key].currency_alphabetic_code)
##     
