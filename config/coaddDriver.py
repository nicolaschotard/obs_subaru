# Load from sub-configurations
import os.path

from lsst.utils import getPackageDir

from lsst.pipe.tasks.assembleCoadd import CompareWarpAssembleCoaddTask
config.assembleCoadd.retarget(CompareWarpAssembleCoaddTask)
config.assembleCoadd.assembleStaticSkyModel.subregionSize = (10000, 200)
config.assembleCoadd.assembleStaticSkyModel.badMaskPlanes = ("BAD", "EDGE", "SAT", "INTRP", "NO_DATA",)
config.assembleCoadd.assembleStaticSkyModel.doApplyUberCal = True

for sub in ("makeCoaddTempExp", "backgroundReference", "assembleCoadd", "processCoadd"):
    path = os.path.join(getPackageDir("obs_subaru"), "config", sub + ".py")
    if os.path.exists(path):
        getattr(config, sub).load(path)

config.doBackgroundReference = False

from lsst.pipe.tasks.selectImages import PsfWcsSelectImagesTask
config.select.retarget(PsfWcsSelectImagesTask)

from lsst.pipe.drivers.utils import NullSelectImagesTask
config.assembleCoadd.select.retarget(NullSelectImagesTask)
