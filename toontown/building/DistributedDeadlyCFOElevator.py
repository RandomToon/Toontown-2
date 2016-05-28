from toontown.building.DistributedCFOElevator import DistributedCFOElevator
from toontown.toonbase import TTLocalizer


class DistributedDeadlyCFOElevator(DistributedCFOElevator):
    notify = directNotify.newCategory('DistributedDeadlyCFOElevator')

    def setupElevator(self):
        pass

    def getDestName(self):
        return TTLocalizer.ElevatorDeadlyCashBotBoss
