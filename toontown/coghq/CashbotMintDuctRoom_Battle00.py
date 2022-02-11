from toontown.coghq.SpecImports import *

GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE15a',
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
    10001: {
        'type': 'battleBlocker',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(44.257774353, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'cellId': 0,
        'radius': 10.0
    },
    10003: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(39.3964080811, 22.2593421936, 16.0659122467),
        'hpr': Vec3(270.0, 0.0, 90.0),
        'scale': Vec3(0.560864269733, 0.560864269733, 0.560864269733),
        'collisionsOnly': 0,
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10005: {
        'type': 'model',
        'name': 'farLeft',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(41.8226966858, 16.5434036255, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10006: {
        'type': 'model',
        'name': 'farRight',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(41.8226966858, -16.5400009155, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10007: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(39.3192749023, -22.8234348297, 13.6092739105),
        'hpr': Vec3(270.0, 0.0, 270.0),
        'scale': Point3(0.560000002384, 0.560864269733, 0.560864269733),
        'collisionsOnly': 0,
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10008: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-39.3800811768, -22.8855381012, 16.0659122467),
        'hpr': Point3(90.0, 0.0, 90.0),
        'scale': Vec3(0.560864269733, 0.560864269733, 0.560864269733),
        'collisionsOnly': 0,
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10009: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-39.3062858582, 22.1807098389, 13.6092739105),
        'hpr': Point3(90.0, 0.0, 270.0),
        'scale': Point3(0.560000002384, 0.560864269733, 0.560864269733),
        'collisionsOnly': 0,
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_C.bam'
    },
    10010: {
        'type': 'model',
        'name': 'nearLeft',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(-41.8199996948, 16.5434036255, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10011: {
        'type': 'model',
        'name': 'nearRight',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(-41.8199996948, -16.5400009155, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(2.28777551651, 2.28777551651, 2.28777551651),
        'collisionsOnly': 1,
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'
    },
    10000: {
        'type': 'nodepath',
        'name': 'cogs',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0)
    },
    10002: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    },
    10004: {
        'type': 'nodepath',
        'name': 'collisions',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1
    }
}
Scenario0 = {}
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [Scenario0]
}
