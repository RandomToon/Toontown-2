from toontown.building import DoorTypes
from toontown.building.DistributedBoardingPartyAI import DistributedBoardingPartyAI
from toontown.coghq import DistributedCogHQDoorAI, DistributedCogHQExteriorDoorAI, LobbyManagerAI
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toon import NPCToons

class CogHQAI:
    notify = directNotify.newCategory('CogHQAI')
    notify.setInfo(True)

    def __init__(
            self, air, zoneId, lobbyZoneId, lobbyFADoorCode,
            lobbyElevatorCtor, bossCtor, DeadlyElevatorCtor=None, DeadlyBossCtor=None):
        self.air = air
        self.zoneId = zoneId
        self.lobbyZoneId = lobbyZoneId
        self.lobbyFADoorCode = lobbyFADoorCode
        self.lobbyElevatorCtor = lobbyElevatorCtor
        self.bossCtor = bossCtor
        self.DeadlyElevatorCtor = DeadlyElevatorCtor
        self.DeadlyBossCtor = DeadlyBossCtor

        self.lobbyMgr = None
        self.lobbyElevator = None
        self.DeadlyElevator = None
        self.boardingParty = None

        self.notify.info('Creating objects... ' + self.getLocationName(zoneId))

    def getLocationName(self, zoneId):
        lookupTable = ToontownGlobals.hoodNameMap
        if (zoneId % 1000) != 0:
            lookupTable = TTLocalizer.GlobalStreetNames
        name = lookupTable.get(zoneId, '')
        if isinstance(name, str):
            return name
        return name[2]

    def startup(self):
        self.createLobbyManager()
        self.createLobbyElevator()
        self.extDoor = self.makeCogHQDoor(self.lobbyZoneId, 0, 0, self.lobbyFADoorCode)
        if simbase.config.GetBool('want-boarding-groups', True):
            self.createBoardingParty()
        self.npcs = NPCToons.createNpcsInZone(self.air, self.zoneId)

    def shutdown(self):
        for npc in self.npcs:
            npc.requestDelete()
        del self.npcs

    def createLobbyManager(self):
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, self.bossCtor, self.DeadlyBossCtor)
        self.lobbyMgr.generateWithRequired(self.lobbyZoneId)

    def createLobbyElevator(self):
        self.lobbyElevator = self.lobbyElevatorCtor(
            self.air, self.lobbyMgr, self.lobbyZoneId)
        self.lobbyElevator.generateWithRequired(self.lobbyZoneId)

        if self.DeadlyElevatorCtor is not None:
            self.DeadlyElevator = self.DeadlyElevatorCtor(
                self.air, self.lobbyMgr, self.lobbyZoneId)
            self.DeadlyElevator.generateWithRequired(self.lobbyZoneId)
 
    def makeCogHQDoor(self, destinationZone, intDoorIndex, extDoorIndex, lock=0):
        intDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(
            self.air, 0, DoorTypes.INT_COGHQ, self.zoneId,
            doorIndex=intDoorIndex, lockValue=lock)
        intDoor.zoneId = destinationZone

        extDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(
            self.air, 0, DoorTypes.EXT_COGHQ, destinationZone,
            doorIndex=extDoorIndex, lockValue=lock)

        extDoor.setOtherDoor(intDoor)
        intDoor.setOtherDoor(extDoor)

        intDoor.generateWithRequired(destinationZone)
        intDoor.sendUpdate('setDoorIndex', [intDoor.getDoorIndex()])

        extDoor.generateWithRequired(self.zoneId)
        extDoor.sendUpdate('setDoorIndex', [extDoor.getDoorIndex()])

        return extDoor

    def createBoardingParty(self):
        elevatorList = [self.lobbyElevator.doId]
        if self.DeadlyElevator is not None:
            elevatorList.append(self.DeadlyElevator.doId)
 
        self.boardingParty = DistributedBoardingPartyAI(self.air, elevatorList, 8)
        self.boardingParty.generateWithRequired(self.lobbyZoneId)
