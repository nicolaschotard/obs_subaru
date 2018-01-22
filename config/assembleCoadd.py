config.doSigmaClip = False
config.subregionSize = (10000, 200) # 200 rows (since patch width is typically < 10k pixels)
config.doMaskBrightObjects = True
config.removeMaskPlanes.append("CROSSTALK")
config.doNImage = True
config.badMaskPlanes += ["SUSPECT"]

from lsst.pipe.tasks.selectImages import PsfWcsSelectImagesTask
config.select.retarget(PsfWcsSelectImagesTask)
