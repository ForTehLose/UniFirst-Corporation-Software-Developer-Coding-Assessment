#application

import Vehicles as V
import Trucks as T
import Vans
import Semis
import Locations as L
import DistributionCenters as DC
import Branches as B


#transfer
def transferVehicle(self, destination, vehicle):
    legalTransfer = True
    if vehicle.Status != V.StatusCodes.standby:
        print("Vehicles cannot be transfered unless they are in standby")
        legalTransfer = False

    if isinstance(destination, B.Branch) and isinstance(vehicle,Semis.Semi):
        print("Semis cannot be transfered to branches")
        legalTransfer = False



    if legalTransfer:
        self.vehicles.remove(vehicle)
        destination.vehicles.append(vehicle)
        print("vehicle transfered")


#example stuff
#vehicle = V.Vehicle("Test","Test",1995,"VINVINVIN012345678901234")
#vehicleNonNumericEnding = V.Vehicle("Test","Test",1995,"0asdfg1wer1zxcv1asd1poiu")
#vehicleLessThanEightAlphas = V.Vehicle("Test","Test",1995,"012345678901234567890123")


#truck = T.Truck("Ford","F150",1995,"VINVINVIN012345678901234")
#print(truck)

#van = Vans.Van("Ford","Econoline",1995,"VINVINVIN012345678901234")
#vanInRepair = Vans.Van("Ford","Econoline",1995,"VINVINVIN012345678901234")
#vanInRepair.Status = V.StatusCodes.repair

#semi = Semis.Semi("Ford","L-Series",1995,"VINVINVIN012345678901234")

#MainBranch = B.Branch("Main Branch")

#MainDC = DC.DistributionCenter("Main DC", [truck,van,vanInRepair,semi], [MainBranch])
#transferVehicle(MainDC, MainBranch,truck)
#transferVehicle(MainDC, MainBranch,vanInRepair)
#transferVehicle(MainDC, MainBranch,semi)
