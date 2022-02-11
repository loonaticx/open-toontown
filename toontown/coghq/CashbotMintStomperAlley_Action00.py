from toontown.coghq.SpecImports import *

GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE17a',
        'wantDoors': 1
    },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None
    },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': []
    },
    10020: {
        'type': 'attribModifier',
        'name': 'range',
        'comment': '',
        'parentEntId': 10016,
        'attribName': 'range',
        'recursive': 1,
        'typeName': 'stomper',
        'value': '7.3'
    },
    10026: {
        'type': 'attribModifier',
        'name': 'period',
        'comment': '',
        'parentEntId': 10016,
        'attribName': 'period',
        'recursive': 1,
        'typeName': 'stomper',
        'value': '6'
    },
    10011: {
        'type': 'conveyorBelt',
        'name': 'conveyorBelt',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(3.37029790878, 24.4200267792, 13.000869751),
        'hpr': Point3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'platformcollision',
        'length': 42.0,
        'speed': 2.0,
        'treadLength': 10.0,
        'treadModelPath': 'phase_9/models/cogHQ/platform1',
        'widthScale': 1.0
    },
    10014: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10013,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.2,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 8,
        'velocity': 4
    },
    10025: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.2,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 8,
        'velocity': 4
    },
    10002: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-1.80931818485, 65.0541229248, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0
    },
    10008: {
        'type': 'mintShelf',
        'name': 'frontShelf',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(0.75479054451, -116.741004944, 0.0),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10009: {
        'type': 'mintShelf',
        'name': 'backShelf1',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(5.09813165665, 63.6601753235, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10010: {
        'type': 'mintShelf',
        'name': 'copy of backShelf1',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(-3.80197167397, 81.7602081299, 0.0),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10000: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, -9.59561252594, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'
    },
    10003: {
        'type': 'model',
        'name': 'downLift',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(4.43959569931, 36.9850654602, 0.880278944969),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(0.550000011921, 0.550000011921, 0.550000011921),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer.bam'
    },
    10004: {
        'type': 'model',
        'name': 'upLift',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-3.25595784187, -35.5523605347, 0.880278944969),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(0.550000011921, 0.550000011921, 0.550000011921),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer.bam'
    },
    10012: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, 10.1246709824, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam'
    },
    10023: {
        'type': 'model',
        'name': 'penaltyLift',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-4.46345901489, -13.5, 0.880278944969),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(0.34999999404, 0.34999999404, 0.34999999404),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer.bam'
    },
    10027: {
        'type': 'model',
        'name': 'shadow',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0.0, 0.0, -1.56577277184),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(3.5935189724, 3.5935189724, 3.5935189724),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam'
    },
    10028: {
        'type': 'model',
        'name': 'shadow',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, -1.56577277184),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(3.5935189724, 3.5935189724, 3.5935189724),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam'
    },
    10029: {
        'type': 'model',
        'name': 'copy of shadow',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0.0, 0.0, -2.47000002861),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(3.5935189724, 3.5935189724, 3.5935189724),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam'
    },
    10001: {
        'type': 'nodepath',
        'name': 'crates',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.660497009754, 0.0, 0.0133484890684),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.50575017929, 2.50575017929, 2.50575017929)
    },
    10007: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10016: {
        'type': 'nodepath',
        'name': 'stompers',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(5.0, 10.4380426407, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10021: {
        'type': 'nodepath',
        'name': 'goons',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10005: {
        'type': 'paintMixer',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0.0, 0.0, 3.56454277039),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'noBlend',
        'offset': Point3(0.0, 0.0, 20.0),
        'period': 10.0,
        'phaseShift': 0.0,
        'shaftScale': 2.5,
        'waitPercent': 0.4
    },
    10006: {
        'type': 'paintMixer',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 3.56454277039),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'noBlend',
        'offset': Point3(0.0, 0.0, 20.0),
        'period': 5.0,
        'phaseShift': 0.0,
        'shaftScale': 2.5,
        'waitPercent': 0.4
    },
    10024: {
        'type': 'paintMixer',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0.0, 0.0, 3.56454277039),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'floorName': 'PaintMixerFloorCollision',
        'modelPath': 'phase_9/models/cogHQ/PaintMixer',
        'modelScale': Vec3(1.0, 1.0, 1.0),
        'motion': 'noBlend',
        'offset': Point3(0.0, 0.0, 33.0),
        'period': 10.0,
        'phaseShift': 0.5,
        'shaftScale': 4.0,
        'waitPercent': 0.4
    },
    10013: {
        'type': 'path',
        'name': 'right',
        'comment': '',
        'parentEntId': 10021,
        'pos': Point3(4.0, 0.0, 0.0),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 3,
        'pathScale': 1.0
    },
    10022: {
        'type': 'path',
        'name': 'left',
        'comment': '',
        'parentEntId': 10021,
        'pos': Point3(-4.0, 2.0, 0.0),
        'hpr': Point3(-90.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 3,
        'pathScale': 1.0
    },
    10015: {
        'type': 'stomper',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.0,
        'range': 7.3,
        'shaftScale': Point3(1.89999997616, 7.5, 1.89999997616),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0
    },
    10017: {
        'type': 'stomper',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 8.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.75,
        'range': 7.3,
        'shaftScale': Point3(1.89999997616, 7.5, 1.89999997616),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0
    },
    10018: {
        'type': 'stomper',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 16.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.25,
        'range': 7.3,
        'shaftScale': Point3(1.89999997616, 7.5, 1.89999997616),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0
    },
    10019: {
        'type': 'stomper',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 24.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': 1,
        'crushCellId': None,
        'damage': 3,
        'headScale': Point3(4.0, 2.0, 4.0),
        'modelPath': 0,
        'motion': 1,
        'period': 6,
        'phaseShift': 0.5,
        'range': 7.3,
        'shaftScale': Point3(1.89999997616, 7.5, 1.89999997616),
        'soundLen': 0,
        'soundOn': 0,
        'soundPath': 0,
        'style': 'horizontal',
        'switchId': 0,
        'wantShadow': 1,
        'wantSmoke': 0,
        'zOffset': 0
    }
}
Scenario0 = {}
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [Scenario0]
}
