#Created by thomas christy

#Vehicles
import re

#vehicle status enums
class StatusCodes:
    standby, transit, service, repair = range(4)

#need regex to check vin
class Vehicle(object):
    #constructor
    def __init__(self, Make, Model, Year, VIN):
        self.Make = Make
        self.Model = Model
        if len(str(abs(Year))) > 4:
            raise ValueError("Year must be 4 digits")
        else:
            self.Year = Year

        #TODO: devise regex for VIN
        #since im not a regex expert ill just use 3 of em
        ValidVin = True
        if re.search('.{24}',VIN) is None:
            print("VIN is not 24 characters")
            ValidVin = False
        if re.search('.*\d{5}',VIN) is None:
            print("Vin does not end with 5 numeric characters")
            ValidVin = False
        if len(re.findall('[a-zA-Z]',VIN)) < 8:
            print("Vin must contain at least 8 Alphas")
            ValidVin = False
        if ValidVin:
            print("Vin is Valid")
            self.VIN = VIN
        else:
            raise ValueError("Vin Invalid")
        self.Status = StatusCodes.standby

    def __str__(self):
        return str(self.Year) + " " + self.Make + " " + self.Model


    
