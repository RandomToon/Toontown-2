from toontown.building.DistributedVPElevatorAI import DistributedVPElevatorAI
 
 
class DistributedDeadlyVPElevatorAI(DistributedVPElevatorAI):
    def sendAvatarsToDestination(self, avIdList):
        if len(avIdList) > 0:
            bossZone = self.bldg.createBossOffice(avIdList, isDeadly=True)
            for avId in avIdList:
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setBossOfficeZoneForce', [bossZone])