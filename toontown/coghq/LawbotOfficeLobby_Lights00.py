from toontown.coghq.SpecImports import *

GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone04a',
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
    100016: {
        'type': 'beanBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-1.17415, -2.82071, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'rewardPerGrab': 42,
        'rewardPerGrabMax': 0
    },
    100017: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(1.70419, 4.05857, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'gagLevel': 5,
        'gagLevelMax': 5,
        'gagTrack': 'random',
        'rewardPerGrab': 3,
        'rewardPerGrabMax': 0
    },
    100018: {
        'type': 'gagBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-6.14262, 5.87553, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'gagLevel': 5,
        'gagLevelMax': 5,
        'gagTrack': 'random',
        'rewardPerGrab': 3,
        'rewardPerGrabMax': 0
    },
    100011: {
        'type': 'mover',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'cycleType': 'loop',
        'entity2Move': 100000,
        'modelPath': 0,
        'moveTarget': 100012,
        'pos0Move': 60.0,
        'pos0Wait': 10.0,
        'pos1Move': 60.0,
        'pos1Wait': 10.0,
        'startOn': 1,
        'switchId': 0
    },
    100000: {
        'type': 'nodepath',
        'name': 'cameraRing',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    100006: {
        'type': 'nodepath',
        'name': 'centerTarget',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1
    },
    100007: {
        'type': 'nodepath',
        'name': 'sidetarget1',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(8.39848, 43.7828, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1)
    },
    100008: {
        'type': 'nodepath',
        'name': 'sidetarget2',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(7.54716, -38.4515, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1)
    },
    100009: {
        'type': 'nodepath',
        'name': 'sidetarget3',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(-39.4668, 1.83033, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1)
    },
    100010: {
        'type': 'nodepath',
        'name': 'sidetarget4',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(39.47, 1.83033, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1)
    },
    100012: {
        'type': 'nodepath',
        'name': 'moverTarget',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(360, 0, 0),
        'scale': 1
    },
    100013: {
        'type': 'nodepath',
        'name': 'target exit',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.535633, 68.0682, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1)
    },
    100014: {
        'type': 'nodepath',
        'name': 'targetoff1',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(47.1742, 5.53207, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1)
    },
    100015: {
        'type': 'nodepath',
        'name': 'targetoff2',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-47.17, 5.53207, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1)
    },
    100001: {
        'type': 'securityCamera',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(24.3, -17, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'accel': 5.0,
        'damPow': 8,
        'hideModel': 0,
        'maxVel': 15.0,
        'modelPath': 0,
        'projector': Point3(5, 5, 25),
        'radius': 5,
        'switchId': 0,
        'trackTarget1': 100006,
        'trackTarget2': 100013,
        'trackTarget3': 100008
    },
    100002: {
        'type': 'securityCamera',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(28.5, 9.27, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'accel': 5.0,
        'damPow': 8,
        'hideModel': 0,
        'maxVel': 15.0,
        'modelPath': 0,
        'projector': Point3(5, 5, 25),
        'radius': 5,
        'switchId': 0,
        'trackTarget1': 100006,
        'trackTarget2': 100008,
        'trackTarget3': 100013
    },
    100003: {
        'type': 'securityCamera',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(0, 30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'accel': 5.0,
        'damPow': 8,
        'hideModel': 0,
        'maxVel': 15.0,
        'modelPath': 0,
        'projector': Point3(5, 5, 25),
        'radius': 5,
        'switchId': 0,
        'trackTarget1': 100006,
        'trackTarget2': 100009,
        'trackTarget3': 100014
    },
    100004: {
        'type': 'securityCamera',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(-24.3, -17, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'accel': 5.0,
        'damPow': 8,
        'hideModel': 0,
        'maxVel': 15.0,
        'modelPath': 0,
        'projector': Point3(6, 6, 25),
        'radius': 5,
        'switchId': 0,
        'trackTarget1': 100006,
        'trackTarget2': 100010,
        'trackTarget3': 100007
    },
    100005: {
        'type': 'securityCamera',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 100000,
        'pos': Point3(-28.5, 9.27, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'accel': 5.0,
        'damPow': 8,
        'hideModel': 0,
        'maxVel': 15.0,
        'modelPath': 0,
        'projector': Point3(5, 5, 25),
        'radius': 5,
        'switchId': 0,
        'trackTarget1': 100006,
        'trackTarget2': 100007,
        'trackTarget3': 100015
    }
}
Scenario0 = {}
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [Scenario0]
}
