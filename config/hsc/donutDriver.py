"""
hsc-specific overrides for DonutDriverTask
"""
import os.path

from lsst.utils import getPackageDir

config.processDonut.load(os.path.join(getPackageDir("obs_subaru"), "config", "hsc", "processDonut.py"))
