from toontown.building.DistributedVPElevator import DistributedVPElevator
from toontown.toonbase import TTLocalizer
 
 
class DistributedDeadlyVPElevator(DistributedVPElevator):
    notify = directNotify.newCategory('DistributedDeadlyVPElevator')

    def setupElevator(self):
        pass
 
    def getDestName(self):
        return TTLocalizer.ElevatorDeadlySellBotBoss