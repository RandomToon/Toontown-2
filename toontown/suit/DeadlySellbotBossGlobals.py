from toontown.toonbase import ToontownGlobals


PieCount = (
    70,
    60,
    55,
    50,
    45,
    40,
    35,
    30,
)


DamageLevels = {
    ToontownGlobals.BossCogElectricFence: 40,
    ToontownGlobals.BossCogRecoverDizzyAttack: 50,
    ToontownGlobals.BossCogAreaAttack: 60,
    ToontownGlobals.BossCogDirectedAttack: 70,
    ToontownGlobals.BossCogFrontAttack: 80
}


def getDamageFromAttackCode(attackCode):
    return DamageLevels.get(attackCode) or 40
