from toontown.coghq.SpecImports import *

GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE07a',
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
    10015: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(0.35536468029, 1.03268241882, 0.0),
        'hpr': Point3(99.4599990845, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'gagLevel': 5,
        'gagLevelMax': 0,
        'gagTrack': 'random',
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 10
    },
    10007: {
        'type': 'gear',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(2.0, -65.0800018311, 11.0900001526),
        'hpr': Vec3(0.0, 90.0, 0.0),
        'scale': Point3(10.0, 10.0, 10.0),
        'degreesPerSec': 10.0,
        'gearScale': 1,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0
    },
    10008: {
        'type': 'gear',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-15.0, -65.0800018311, 15.0),
        'hpr': Vec3(0.0, 90.0, 0.0),
        'scale': Point3(10.0, 10.0, 10.0),
        'degreesPerSec': -10.0,
        'gearScale': 1,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0.26
    },
    10016: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(2.0886592865, -5.19625711441, 0.0),
        'hpr': Vec3(80.5376815796, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 7,
        'rewardPerGrabMax': 10
    },
    10001: {
        'type': 'locator',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'searchPath': '**/EXIT'
    },
    10012: {
        'type': 'mintProduct',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10013: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(33.1602783203, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10014: {
        'type': 'mintProduct',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, -26.4398918152, 0.0),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'mintId': 12500
    },
    10002: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/VaultDoorCover.bam'
    },
    10004: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(28.4207668304, 0.886719465256, 0.0890568122268),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.42410159111, 1.42410159111, 1.42410159111),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_D.bam'
    },
    10005: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(1.02179563046, -5.71805810928, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(0.912700533867, 0.912700533867, 0.912700533867),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_G1.bam'
    },
    10006: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(28.0896816254, 6.65470600128, 0.0692733898759),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam'
    },
    10010: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-30.3416347504, -52.2014503479, 4.94085407257),
        'hpr': Vec3(180.0, 270.0, 270.0),
        'scale': Vec3(0.496759712696, 0.496759712696, 0.496759712696),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10017: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-47.7702331543, -15.7725839615, 0.0),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(0.75, 0.75, 0.75),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10000: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-16.2589473724, 49.1446685791, 10.2881116867),
        'hpr': Vec3(90.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10003: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10009: {
        'type': 'nodepath',
        'name': 'barrels',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(39.311466217, 1.05693364143, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10011: {
        'type': 'nodepath',
        'name': 'product',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-24.7985076904, 59.8468132019, 10.0710220337),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    }
}
Scenario0 = {}
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [Scenario0]
}
