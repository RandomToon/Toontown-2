from toontown.building import ElevatorConstants
from toontown.building.DistributedBossElevatorAI import DistributedBossElevatorAI

class DistributedVPElevatorAI(DistributedBossElevatorAI):

    def __init__(self, air, bldg, zone):
        DistributedBossElevatorAI.__init__(self, air, bldg, zone)
        self.type = ElevatorConstants.ELEVATOR_VP
        self.countdownTime = ElevatorConstants.ElevatorData[self.type]['countdown']
