#distribution centers
from Locations import *

class DistributionCenter(Location):
    def __init__(self, name, vehicles, branches):
        super(DistributionCenter,self).__init__(name, vehicles)
        self.branches = branches
        
    
