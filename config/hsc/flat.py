import os.path

from lsst.utils import getPackageDir
from lsst.obs.subaru.isr import SubaruIsrTask

config.isr.retarget(SubaruIsrTask)
config.isr.load(os.path.join(getPackageDir("obs_subaru"), "config", "hsc", "isr.py"))

from lsst.obs.hsc.calibs import HscFlatCombineTask
config.combination.retarget(HscFlatCombineTask)
config.combination.vignette.load(os.path.join(getPackageDir("obs_subaru"), 'config', 'hsc', 'vignette.py'))

config.isr.doBrighterFatter = False
config.isr.doStrayLight = False
