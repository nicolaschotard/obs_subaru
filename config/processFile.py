import lsst.obs.subaru.processFile
assert(type(root)==lsst.obs.subaru.processFile.ProcessFileConfig)
root.doWriteHeavyFootprintsInSources=False
root.doWriteSources=True
root.doDetection=True
root.doWriteSourceMatches=False
root.detection.reEstimateBackground=True
root.detection.nSigmaToGrow=2.4
root.detection.minPixels=1
root.detection.includeThresholdMultiplier=1.0
root.detection.isotropicGrow=False
root.detection.adjustBackground=0.0
root.detection.thresholdType='stdev'
root.detection.background.ignoredPixelMask=['EDGE', 'DETECTED', 'DETECTED_NEGATIVE']
root.detection.background.undersampleStyle='REDUCE_INTERP_ORDER'
root.detection.background.algorithm='NATURAL_SPLINE'
root.detection.background.binSize=256
root.detection.background.isNanSafe=False
root.detection.background.statisticsProperty='MEANCLIP'
root.detection.returnOriginalFootprints=True
root.detection.thresholdPolarity='positive'
root.detection.thresholdValue=5.0
root.doDeblend=False
root.calibrate.initialPsf.model='SingleGaussian'
root.calibrate.initialPsf.fwhm=1.0
root.calibrate.initialPsf.size=15
root.calibrate.repair.doInterpolate=True
root.calibrate.repair.doCosmicRay=True
root.calibrate.repair.cosmicray.keepCRs=False
root.calibrate.repair.cosmicray.cond3_fac=2.5
root.calibrate.repair.cosmicray.cond3_fac2=0.6
root.calibrate.repair.cosmicray.background.ignoredPixelMask=['EDGE', 'DETECTED', 'DETECTED_NEGATIVE']
root.calibrate.repair.cosmicray.background.undersampleStyle='REDUCE_INTERP_ORDER'
root.calibrate.repair.cosmicray.background.algorithm='AKIMA_SPLINE'
root.calibrate.repair.cosmicray.background.binSize=100000
root.calibrate.repair.cosmicray.background.isNanSafe=False
root.calibrate.repair.cosmicray.background.statisticsProperty='MEDIAN'
root.calibrate.repair.cosmicray.niteration=3
root.calibrate.repair.cosmicray.nCrPixelMax=10000
root.calibrate.repair.cosmicray.minSigma=6.0
root.calibrate.repair.cosmicray.min_DN=150.0
root.calibrate.doPsf=True
root.calibrate.astrometry.forceKnownWcs=False
root.calibrate.astrometry.solver.cleaningParameter=3.0
root.calibrate.astrometry.solver.pixelScaleUncertainty=1.1
root.calibrate.astrometry.solver.useWcsParity=True
root.calibrate.astrometry.solver.sipOrder=4
root.calibrate.astrometry.solver.useWcsRaDecCenter=True
root.calibrate.astrometry.solver.matchThreshold=27.631021115928547
root.calibrate.astrometry.solver.useWcsPixelScale=True
root.calibrate.astrometry.solver.maxStars=50
root.calibrate.astrometry.solver.calculateSip=True
root.calibrate.astrometry.solver.maxCpuTime=0.0
root.calibrate.astrometry.solver.catalogMatchDist=1.0
root.calibrate.astrometry.solver.raDecSearchRadius=1.0
root.calibrate.astrometry.solver.filterMap={}
root.calibrate.doBackground=True
root.calibrate.detection.reEstimateBackground=True
root.calibrate.detection.nSigmaToGrow=2.4
root.calibrate.detection.minPixels=1
root.calibrate.detection.includeThresholdMultiplier=10.0
root.calibrate.detection.isotropicGrow=False
root.calibrate.detection.adjustBackground=0.0
root.calibrate.detection.thresholdType='stdev'
root.calibrate.detection.background.ignoredPixelMask=['EDGE', 'DETECTED', 'DETECTED_NEGATIVE']
root.calibrate.detection.background.undersampleStyle='REDUCE_INTERP_ORDER'
root.calibrate.detection.background.algorithm='NATURAL_SPLINE'
root.calibrate.detection.background.binSize=256
root.calibrate.detection.background.isNanSafe=False
root.calibrate.detection.background.statisticsProperty='MEANCLIP'
root.calibrate.detection.returnOriginalFootprints=True
root.calibrate.detection.thresholdPolarity='positive'
root.calibrate.detection.thresholdValue=5.0
root.calibrate.doPhotoCal=True
root.calibrate.initialMeasurement.doReplaceWithNoise=True
root.calibrate.initialMeasurement.centroider['centroid.sdss'].priority=0.0
root.calibrate.initialMeasurement.centroider['centroid.sdss'].peakMin=-1.0
root.calibrate.initialMeasurement.centroider['centroid.sdss'].wfac=1.5
root.calibrate.initialMeasurement.centroider['centroid.sdss'].binmax=16
root.calibrate.initialMeasurement.centroider['centroid.naive'].priority=0.0
root.calibrate.initialMeasurement.centroider['centroid.naive'].background=0.0
root.calibrate.initialMeasurement.centroider['centroid.gaussian'].priority=0.0
root.calibrate.initialMeasurement.centroider.name='centroid.sdss'
root.calibrate.initialMeasurement.prefix='initial.'
root.calibrate.initialMeasurement.algorithms['centroid.sdss'].priority=0.0
root.calibrate.initialMeasurement.algorithms['centroid.sdss'].peakMin=-1.0
root.calibrate.initialMeasurement.algorithms['centroid.sdss'].wfac=1.5
root.calibrate.initialMeasurement.algorithms['centroid.sdss'].binmax=16
root.calibrate.initialMeasurement.algorithms['flux.psf'].priority=2.0
root.calibrate.initialMeasurement.algorithms['flags.pixel'].priority=0.0
root.calibrate.initialMeasurement.algorithms['shape.sdss'].priority=1.0
root.calibrate.initialMeasurement.algorithms['shape.sdss'].tol2=9.999999747378752e-05
root.calibrate.initialMeasurement.algorithms['shape.sdss'].tol1=9.999999747378752e-06
root.calibrate.initialMeasurement.algorithms['shape.sdss'].background=0.0
root.calibrate.initialMeasurement.algorithms['shape.sdss'].maxIter=100
root.calibrate.initialMeasurement.algorithms['centroid.record'].priority=5.0
root.calibrate.initialMeasurement.algorithms['flux.aperture'].priority=2.0
root.calibrate.initialMeasurement.algorithms['flux.aperture'].radii=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.5625, 2.44140625, 3.814697265625, 5.9604644775390625, 9.313225746154785, 14.551915228366852, 22.737367544323206, 35.52713678800501, 55.51115123125783]
root.calibrate.initialMeasurement.algorithms['flux.naive'].priority=2.0
root.calibrate.initialMeasurement.algorithms['flux.naive'].radius=7.0
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].tol2=9.999999747378752e-05
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].tol1=9.999999747378752e-06
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].priority=2.0
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].shape='initial.shape.sdss'
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].centroid='initial.shape.sdss.centroid'
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].background=0.0
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].maxIter=100
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].fixed=True
root.calibrate.initialMeasurement.algorithms['flux.gaussian'].shiftmax=10.0
root.calibrate.initialMeasurement.algorithms['centroid.naive'].priority=0.0
root.calibrate.initialMeasurement.algorithms['centroid.naive'].background=0.0
root.calibrate.initialMeasurement.algorithms['flux.sinc'].priority=2.0
root.calibrate.initialMeasurement.algorithms['flux.sinc'].radius1=0.0
root.calibrate.initialMeasurement.algorithms['flux.sinc'].radius2=7.0
root.calibrate.initialMeasurement.algorithms['flux.sinc'].angle=0.0
root.calibrate.initialMeasurement.algorithms['flux.sinc'].ellipticity=0.0
root.calibrate.initialMeasurement.algorithms['centroid.gaussian'].priority=0.0
root.calibrate.initialMeasurement.algorithms['jacobian'].priority=3.0
root.calibrate.initialMeasurement.algorithms['jacobian'].pixelScale=0.5
root.calibrate.initialMeasurement.algorithms['flux.aperture.elliptical'].priority=1.899999976158142
root.calibrate.initialMeasurement.algorithms['flux.aperture.elliptical'].radii=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.5625, 2.44140625, 3.814697265625, 5.9604644775390625, 9.313225746154785, 14.551915228366852, 22.737367544323206, 35.52713678800501, 55.51115123125783]
root.calibrate.initialMeasurement.algorithms['flux.peakLikelihood'].priority=2.0
root.calibrate.initialMeasurement.algorithms['flux.peakLikelihood'].warpingKernelName='lanczos4'
root.calibrate.initialMeasurement.algorithms['correctfluxes'].doApCorr=True
root.calibrate.initialMeasurement.algorithms['correctfluxes'].canonicalFluxName='flux.psf'
root.calibrate.initialMeasurement.algorithms['correctfluxes'].apCorrRadius=7.0
root.calibrate.initialMeasurement.algorithms['correctfluxes'].priority=3.0
root.calibrate.initialMeasurement.algorithms['correctfluxes'].doFlagTieFailures=True
root.calibrate.initialMeasurement.algorithms['correctfluxes'].doFlagApCorrFailures=True
root.calibrate.initialMeasurement.algorithms['correctfluxes'].canonicalFluxIndex=0
root.calibrate.initialMeasurement.algorithms['correctfluxes'].doTieScaledFluxes=True
root.calibrate.initialMeasurement.algorithms['classification.extendedness'].priority=5.0
root.calibrate.initialMeasurement.algorithms['classification.extendedness'].psfErrFactor=0.0
root.calibrate.initialMeasurement.algorithms['classification.extendedness'].modelErrFactor=0.0
root.calibrate.initialMeasurement.algorithms['classification.extendedness'].fluxRatio=0.9852216748768474
root.calibrate.initialMeasurement.algorithms['skycoord'].priority=5.0
root.calibrate.initialMeasurement.algorithms.names=['flux.psf', 'flags.pixel', 'flux.naive', 'flux.gaussian', 'centroid.naive', 'flux.sinc', 'shape.sdss', 'skycoord', 'classification.extendedness']
root.calibrate.initialMeasurement.replaceWithNoise.noiseSeed=0
root.calibrate.initialMeasurement.replaceWithNoise.noiseOffset=0.0
root.calibrate.initialMeasurement.replaceWithNoise.noiseSource='measure'
root.calibrate.initialMeasurement.slots.psfFlux='flux.psf'
root.calibrate.initialMeasurement.slots.apFlux='flux.sinc'
root.calibrate.initialMeasurement.slots.instFlux='flux.gaussian'
root.calibrate.initialMeasurement.slots.shape='shape.sdss'
root.calibrate.initialMeasurement.slots.centroid='centroid.sdss'
root.calibrate.initialMeasurement.slots.modelFlux='flux.gaussian'
root.calibrate.measurePsf.psfDeterminer['pca'].lam=0.05
root.calibrate.measurePsf.psfDeterminer['pca'].reducedChi2ForPsfCandidates=2.0
root.calibrate.measurePsf.psfDeterminer['pca'].nonLinearSpatialFit=False
root.calibrate.measurePsf.psfDeterminer['pca'].sizeCellX=256
root.calibrate.measurePsf.psfDeterminer['pca'].sizeCellY=256
root.calibrate.measurePsf.psfDeterminer['pca'].spatialReject=3.0
root.calibrate.measurePsf.psfDeterminer['pca'].kernelSize=10.0
root.calibrate.measurePsf.psfDeterminer['pca'].nIterForPsf=3
root.calibrate.measurePsf.psfDeterminer['pca'].constantWeight=True
root.calibrate.measurePsf.psfDeterminer['pca'].kernelSizeMax=45
root.calibrate.measurePsf.psfDeterminer['pca'].nStarPerCellSpatialFit=5
root.calibrate.measurePsf.psfDeterminer['pca'].borderWidth=0
root.calibrate.measurePsf.psfDeterminer['pca'].nEigenComponents=4
root.calibrate.measurePsf.psfDeterminer['pca'].spatialOrder=2
root.calibrate.measurePsf.psfDeterminer['pca'].tolerance=0.01
root.calibrate.measurePsf.psfDeterminer['pca'].kernelSizeMin=25
root.calibrate.measurePsf.psfDeterminer['pca'].nStarPerCell=3
root.calibrate.measurePsf.psfDeterminer.name='pca'
root.calibrate.measurePsf.starSelector['objectSize'].widthMax=10.0
root.calibrate.measurePsf.starSelector['objectSize'].widthStdAllowed=0.15
root.calibrate.measurePsf.starSelector['objectSize'].widthMin=0.0
root.calibrate.measurePsf.starSelector['objectSize'].kernelSize=21
root.calibrate.measurePsf.starSelector['objectSize'].fluxMin=12500.0
root.calibrate.measurePsf.starSelector['objectSize'].borderWidth=0
root.calibrate.measurePsf.starSelector['objectSize'].badFlags=['initial.flags.pixel.edge', 'initial.flags.pixel.interpolated.center', 'initial.flags.pixel.saturated.center', 'initial.flags.pixel.cr.center', 'initial.flags.pixel.bad']
root.calibrate.measurePsf.starSelector['objectSize'].fluxMax=0.0
root.calibrate.measurePsf.starSelector['objectSize'].sourceFluxField='initial.flux.gaussian'
root.calibrate.measurePsf.starSelector['catalog'].fluxLim=0.0
root.calibrate.measurePsf.starSelector['catalog'].fluxMax=0.0
root.calibrate.measurePsf.starSelector['catalog'].badStarPixelFlags=['flags.pixel.edge', 'flags.pixel.interpolated.center', 'flags.pixel.saturated.center', 'initial.flags.pixel.edge', 'initial.flags.pixel.interpolated.center', 'initial.flags.pixel.saturated.center']
root.calibrate.measurePsf.starSelector['catalog'].kernelSize=21
root.calibrate.measurePsf.starSelector['catalog'].borderWidth=0
root.calibrate.measurePsf.starSelector['secondMoment'].kernelSize=21
root.calibrate.measurePsf.starSelector['secondMoment'].histMomentMinMultiplier=2.0
root.calibrate.measurePsf.starSelector['secondMoment'].histSize=64
root.calibrate.measurePsf.starSelector['secondMoment'].histMomentClip=5.0
root.calibrate.measurePsf.starSelector['secondMoment'].borderWidth=0
root.calibrate.measurePsf.starSelector['secondMoment'].badFlags=['initial.flags.pixel.edge', 'initial.flags.pixel.interpolated.center', 'initial.flags.pixel.saturated.center', 'initial.flags.pixel.cr.center']
root.calibrate.measurePsf.starSelector['secondMoment'].histMomentMaxMultiplier=5.0
root.calibrate.measurePsf.starSelector['secondMoment'].fluxMax=0.0
root.calibrate.measurePsf.starSelector['secondMoment'].clumpNSigma=2.0
root.calibrate.measurePsf.starSelector['secondMoment'].fluxLim=12500.0
root.calibrate.measurePsf.starSelector['secondMoment'].histMomentMax=100.0
root.calibrate.measurePsf.starSelector['sizeMagnitude'].startn1=0.1
root.calibrate.measurePsf.starSelector['sizeMagnitude'].minsize=0.0
root.calibrate.measurePsf.starSelector['sizeMagnitude'].fitorder=1
root.calibrate.measurePsf.starSelector['sizeMagnitude'].minmag=0.0
root.calibrate.measurePsf.starSelector['sizeMagnitude'].starfrac=0.5
root.calibrate.measurePsf.starSelector['sizeMagnitude'].maxmag=1e+100
root.calibrate.measurePsf.starSelector['sizeMagnitude'].logsize=False
root.calibrate.measurePsf.starSelector['sizeMagnitude'].starsperbin=30
root.calibrate.measurePsf.starSelector['sizeMagnitude'].fitsigclip=4.0
root.calibrate.measurePsf.starSelector['sizeMagnitude'].maxsize=1e+100
root.calibrate.measurePsf.starSelector['sizeMagnitude'].aperture=5.0
root.calibrate.measurePsf.starSelector['sizeMagnitude'].purityratio=0.05
root.calibrate.measurePsf.starSelector.name='secondMoment'
root.calibrate.background.ignoredPixelMask=['EDGE', 'DETECTED', 'DETECTED_NEGATIVE']
root.calibrate.background.undersampleStyle='REDUCE_INTERP_ORDER'
root.calibrate.background.algorithm='NATURAL_SPLINE'
root.calibrate.background.binSize=1024
root.calibrate.background.isNanSafe=False
root.calibrate.background.statisticsProperty='MEANCLIP'
root.calibrate.measurement.doReplaceWithNoise=True
root.calibrate.measurement.centroider['centroid.sdss'].priority=0.0
root.calibrate.measurement.centroider['centroid.sdss'].peakMin=-1.0
root.calibrate.measurement.centroider['centroid.sdss'].wfac=1.5
root.calibrate.measurement.centroider['centroid.sdss'].binmax=16
root.calibrate.measurement.centroider['centroid.naive'].priority=0.0
root.calibrate.measurement.centroider['centroid.naive'].background=0.0
root.calibrate.measurement.centroider['centroid.gaussian'].priority=0.0
root.calibrate.measurement.centroider.name='centroid.sdss'
root.calibrate.measurement.prefix=None
root.calibrate.measurement.algorithms['centroid.sdss'].priority=0.0
root.calibrate.measurement.algorithms['centroid.sdss'].peakMin=-1.0
root.calibrate.measurement.algorithms['centroid.sdss'].wfac=1.5
root.calibrate.measurement.algorithms['centroid.sdss'].binmax=16
root.calibrate.measurement.algorithms['flux.psf'].priority=2.0
root.calibrate.measurement.algorithms['flags.pixel'].priority=0.0
root.calibrate.measurement.algorithms['shape.sdss'].priority=1.0
root.calibrate.measurement.algorithms['shape.sdss'].tol2=9.999999747378752e-05
root.calibrate.measurement.algorithms['shape.sdss'].tol1=9.999999747378752e-06
root.calibrate.measurement.algorithms['shape.sdss'].background=0.0
root.calibrate.measurement.algorithms['shape.sdss'].maxIter=100
root.calibrate.measurement.algorithms['centroid.record'].priority=5.0
root.calibrate.measurement.algorithms['flux.aperture'].priority=2.0
root.calibrate.measurement.algorithms['flux.aperture'].radii=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.5625, 2.44140625, 3.814697265625, 5.9604644775390625, 9.313225746154785, 14.551915228366852, 22.737367544323206, 35.52713678800501, 55.51115123125783]
root.calibrate.measurement.algorithms['flux.naive'].priority=2.0
root.calibrate.measurement.algorithms['flux.naive'].radius=7.0
root.calibrate.measurement.algorithms['flux.gaussian'].tol2=9.999999747378752e-05
root.calibrate.measurement.algorithms['flux.gaussian'].tol1=9.999999747378752e-06
root.calibrate.measurement.algorithms['flux.gaussian'].priority=2.0
root.calibrate.measurement.algorithms['flux.gaussian'].shape='shape.sdss'
root.calibrate.measurement.algorithms['flux.gaussian'].centroid='shape.sdss.centroid'
root.calibrate.measurement.algorithms['flux.gaussian'].background=0.0
root.calibrate.measurement.algorithms['flux.gaussian'].maxIter=100
root.calibrate.measurement.algorithms['flux.gaussian'].fixed=True
root.calibrate.measurement.algorithms['flux.gaussian'].shiftmax=10.0
root.calibrate.measurement.algorithms['centroid.naive'].priority=0.0
root.calibrate.measurement.algorithms['centroid.naive'].background=0.0
root.calibrate.measurement.algorithms['flux.sinc'].priority=2.0
root.calibrate.measurement.algorithms['flux.sinc'].radius1=0.0
root.calibrate.measurement.algorithms['flux.sinc'].radius2=7.0
root.calibrate.measurement.algorithms['flux.sinc'].angle=0.0
root.calibrate.measurement.algorithms['flux.sinc'].ellipticity=0.0
root.calibrate.measurement.algorithms['centroid.gaussian'].priority=0.0
root.calibrate.measurement.algorithms['jacobian'].priority=3.0
root.calibrate.measurement.algorithms['jacobian'].pixelScale=0.5
root.calibrate.measurement.algorithms['flux.aperture.elliptical'].priority=1.899999976158142
root.calibrate.measurement.algorithms['flux.aperture.elliptical'].radii=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.5625, 2.44140625, 3.814697265625, 5.9604644775390625, 9.313225746154785, 14.551915228366852, 22.737367544323206, 35.52713678800501, 55.51115123125783]
root.calibrate.measurement.algorithms['flux.peakLikelihood'].priority=2.0
root.calibrate.measurement.algorithms['flux.peakLikelihood'].warpingKernelName='lanczos4'
root.calibrate.measurement.algorithms['correctfluxes'].doApCorr=True
root.calibrate.measurement.algorithms['correctfluxes'].canonicalFluxName='flux.psf'
root.calibrate.measurement.algorithms['correctfluxes'].apCorrRadius=7.0
root.calibrate.measurement.algorithms['correctfluxes'].priority=3.0
root.calibrate.measurement.algorithms['correctfluxes'].doFlagTieFailures=True
root.calibrate.measurement.algorithms['correctfluxes'].doFlagApCorrFailures=True
root.calibrate.measurement.algorithms['correctfluxes'].canonicalFluxIndex=0
root.calibrate.measurement.algorithms['correctfluxes'].doTieScaledFluxes=True
root.calibrate.measurement.algorithms['classification.extendedness'].priority=5.0
root.calibrate.measurement.algorithms['classification.extendedness'].psfErrFactor=0.0
root.calibrate.measurement.algorithms['classification.extendedness'].modelErrFactor=0.0
root.calibrate.measurement.algorithms['classification.extendedness'].fluxRatio=0.9852216748768474
root.calibrate.measurement.algorithms['skycoord'].priority=5.0
root.calibrate.measurement.algorithms.names=['flux.psf', 'flags.pixel', 'flux.naive', 'flux.gaussian', 'centroid.naive', 'flux.sinc', 'shape.sdss', 'correctfluxes', 'classification.extendedness', 'skycoord']
root.calibrate.measurement.replaceWithNoise.noiseSeed=0
root.calibrate.measurement.replaceWithNoise.noiseOffset=0.0
root.calibrate.measurement.replaceWithNoise.noiseSource='measure'
root.calibrate.measurement.slots.psfFlux='flux.psf'
root.calibrate.measurement.slots.apFlux='flux.sinc'
root.calibrate.measurement.slots.instFlux='flux.gaussian'
root.calibrate.measurement.slots.shape='shape.sdss'
root.calibrate.measurement.slots.centroid='centroid.sdss'
root.calibrate.measurement.slots.modelFlux='flux.gaussian'
root.calibrate.photocal.nIter=20
root.calibrate.photocal.fluxField='flux.psf'
root.calibrate.photocal.magLimit=22.0
root.calibrate.photocal.sigmaMax=0.25
root.calibrate.photocal.goodFlags=[]
root.calibrate.photocal.outputField='classification.photometric'
root.calibrate.photocal.nSigma=3.0
root.calibrate.photocal.applyColorTerms=True
root.calibrate.photocal.badFlags=['flags.pixel.edge', 'flags.pixel.interpolated.any', 'flags.pixel.saturated.any']
root.calibrate.photocal.useMedian=True
root.calibrate.doAstrometry=True
root.measurement.doReplaceWithNoise=True
root.measurement.centroider['centroid.sdss'].priority=0.0
root.measurement.centroider['centroid.sdss'].peakMin=-1.0
root.measurement.centroider['centroid.sdss'].wfac=1.5
root.measurement.centroider['centroid.sdss'].binmax=16
root.measurement.centroider['centroid.naive'].priority=0.0
root.measurement.centroider['centroid.naive'].background=0.0
root.measurement.centroider['centroid.gaussian'].priority=0.0
root.measurement.centroider.name='centroid.sdss'
root.measurement.prefix=None
root.measurement.algorithms['centroid.sdss'].priority=0.0
root.measurement.algorithms['centroid.sdss'].peakMin=-1.0
root.measurement.algorithms['centroid.sdss'].wfac=1.5
root.measurement.algorithms['centroid.sdss'].binmax=16
root.measurement.algorithms['flux.psf'].priority=2.0
root.measurement.algorithms['flags.pixel'].priority=0.0
root.measurement.algorithms['shape.sdss'].priority=1.0
root.measurement.algorithms['shape.sdss'].tol2=9.999999747378752e-05
root.measurement.algorithms['shape.sdss'].tol1=9.999999747378752e-06
root.measurement.algorithms['shape.sdss'].background=0.0
root.measurement.algorithms['shape.sdss'].maxIter=100
root.measurement.algorithms['centroid.record'].priority=5.0
root.measurement.algorithms['flux.aperture'].priority=2.0
root.measurement.algorithms['flux.aperture'].radii=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.5625, 2.44140625, 3.814697265625, 5.9604644775390625, 9.313225746154785, 14.551915228366852, 22.737367544323206, 35.52713678800501, 55.51115123125783]
root.measurement.algorithms['flux.naive'].priority=2.0
root.measurement.algorithms['flux.naive'].radius=7.0
root.measurement.algorithms['flux.gaussian'].tol2=9.999999747378752e-05
root.measurement.algorithms['flux.gaussian'].tol1=9.999999747378752e-06
root.measurement.algorithms['flux.gaussian'].priority=2.0
root.measurement.algorithms['flux.gaussian'].shape='shape.sdss'
root.measurement.algorithms['flux.gaussian'].centroid='shape.sdss.centroid'
root.measurement.algorithms['flux.gaussian'].background=0.0
root.measurement.algorithms['flux.gaussian'].maxIter=100
root.measurement.algorithms['flux.gaussian'].fixed=True
root.measurement.algorithms['flux.gaussian'].shiftmax=10.0
root.measurement.algorithms['centroid.naive'].priority=0.0
root.measurement.algorithms['centroid.naive'].background=0.0
root.measurement.algorithms['flux.sinc'].priority=2.0
root.measurement.algorithms['flux.sinc'].radius1=0.0
root.measurement.algorithms['flux.sinc'].radius2=7.0
root.measurement.algorithms['flux.sinc'].angle=0.0
root.measurement.algorithms['flux.sinc'].ellipticity=0.0
root.measurement.algorithms['centroid.gaussian'].priority=0.0
root.measurement.algorithms['jacobian'].priority=3.0
root.measurement.algorithms['jacobian'].pixelScale=0.5
root.measurement.algorithms['flux.aperture.elliptical'].priority=1.899999976158142
root.measurement.algorithms['flux.aperture.elliptical'].radii=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.5625, 2.44140625, 3.814697265625, 5.9604644775390625, 9.313225746154785, 14.551915228366852, 22.737367544323206, 35.52713678800501, 55.51115123125783]
root.measurement.algorithms['flux.peakLikelihood'].priority=2.0
root.measurement.algorithms['flux.peakLikelihood'].warpingKernelName='lanczos4'
root.measurement.algorithms['correctfluxes'].doApCorr=True
root.measurement.algorithms['correctfluxes'].canonicalFluxName='flux.psf'
root.measurement.algorithms['correctfluxes'].apCorrRadius=7.0
root.measurement.algorithms['correctfluxes'].priority=3.0
root.measurement.algorithms['correctfluxes'].doFlagTieFailures=True
root.measurement.algorithms['correctfluxes'].doFlagApCorrFailures=True
root.measurement.algorithms['correctfluxes'].canonicalFluxIndex=0
root.measurement.algorithms['correctfluxes'].doTieScaledFluxes=True
root.measurement.algorithms['classification.extendedness'].priority=5.0
root.measurement.algorithms['classification.extendedness'].psfErrFactor=0.0
root.measurement.algorithms['classification.extendedness'].modelErrFactor=0.0
root.measurement.algorithms['classification.extendedness'].fluxRatio=0.9852216748768474
root.measurement.algorithms['skycoord'].priority=5.0
root.measurement.algorithms.names=['flux.psf', 'flags.pixel', 'flux.naive', 'flux.gaussian', 'centroid.naive', 'flux.sinc', 'shape.sdss', 'correctfluxes', 'classification.extendedness', 'skycoord']
root.measurement.replaceWithNoise.noiseSeed=0
root.measurement.replaceWithNoise.noiseOffset=0.0
root.measurement.replaceWithNoise.noiseSource='measure'
root.measurement.slots.psfFlux='flux.psf'
root.measurement.slots.apFlux='flux.sinc'
root.measurement.slots.instFlux='flux.gaussian'
root.measurement.slots.shape='shape.sdss'
root.measurement.slots.centroid='centroid.sdss'
root.measurement.slots.modelFlux='flux.gaussian'
root.doMeasurement=True
root.deblend.psf_chisq_2=1.5
root.deblend.psf_chisq_1=1.5
root.deblend.maxNumberOfPeaks=0
root.deblend.psf_chisq_2b=1.5
root.doWriteCalibrate=True
root.doCalibrate=True
root.persistBackgroundModel=True
root.doWriteCalibrateMatches=True
