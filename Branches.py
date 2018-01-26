#Branches
from Locations import *

class Branch(Location):
    def __init__(self, name, vehicles = []):
        super(Branch,self).__init__(name, vehicles)
        
    
