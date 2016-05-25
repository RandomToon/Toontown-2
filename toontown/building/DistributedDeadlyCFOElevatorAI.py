from toontown.building.DistributedCFOElevatorAI import DistributedCFOElevatorAI


class DistributedDeadlyCFOElevatorAI(DistributedCFOElevatorAI):
    notify = directNotify.newCategory('DistributedDeadlyCFOElevatorAI')

    def sendAvatarsToDestination(self, avIdList):
        if len(avIdList) > 0:
            bossZone = self.bldg.createBossOffice(avIdList, isDeadly=True)
            for avId in avIdList:
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setBossOfficeZoneForce', [bossZone])
