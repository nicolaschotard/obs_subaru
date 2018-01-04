#!/usr/bin/env python
#
# LSST Data Management System
#
# Copyright 2017 AURA/LSST.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <https://www.lsstcorp.org/LegalNotices/>.
#
from __future__ import absolute_import, division, print_function

import os
import glob
import numpy as np

from lsst.afw.image import TransmissionCurve, Filter
from lsst.utils import getProductDir

__all__ = ("getOpticsTransmission", "getSensorTransmission", "getAtmosphereTransmission",
           "getFilterTransmission",)

DATA_DIR = os.path.join(getProductDir("obs_subaru"), "hsc", "transmission")

HSC_BEGIN = "2012-12-18"  # initial date for curves valid for entire lifetime of HSC


def getLongFilterName(short):
    # HSC tells afw.image.Filter that the short name is canonical
    # but uses the long name for its data IDs, so we need this hack
    # to get the long name from the short name.
    if short.startswith("HSC") or short.startswith("NB"):
        return short
    f = Filter(short)
    for a in f.getAliases():
        if a.startswith("HSC") or a.startswith("NB") or a.startswith("IB"):
            return a
    return short


def readTransmissionCurveFromFile(filename, unit="angstrom", atMin=None, atMax=None):
    wavelengths, throughput = np.loadtxt(os.path.join(DATA_DIR, filename), usecols=2, unpack=True)
    if unit == "nm":
        wavelengths *= 10
    elif unit != "ansgstrom":
        raise ValueError("Invalid wavelength unit")
    if atMin is None:
        atMin = throughput[0]
    if atMax is None:
        atMax = throughput[-1]
    return TransmissionCurve.makeSpatiallyConstant(throughput=throughput, wavelengths=wavelengths,
                                                   throughputAtMin=atMin, throughputAtMax=atMax)

def getOpticsTransmission():
    """Return a dictionary of TransmissionCurves describing the combined
    throughput of HSC and the Subaru primary mirror.

    Dictionary keys are string dates (YYYY-MM-DD) indicating the beginning of
    the validity period for the curve stored as the associated dictionary
    value.  If the curve is spatially varying, it will be defined in focal
    plane coordinates.

    Dictionary values may be None to indicate that no TransmissionCurve is
    valid after the date provided in the key.
    """
    mirror2010 = readTransmissionCurveFromFile("M1-2010s.txt", unit="nm")
    camera = readTransmissionCurveFromFile("throughput_popt2.txt")
    camera *= readTransmissionCurveFromFile("throughput_win.txt")
    return {
        HSC_BEGIN: mirror2010*camera,
        "2017-10-01": None   # mirror recoating begins, approximately
    }


def getSensorTransmission():
    """Return a nested dictionary of TransmissionCurves describing the
    throughput of each sensor.

    Outer directionary keys are string dates (YYYY-MM-DD), with values
    a dictionary mapping CCD ID to TransmissionCurve.  If the curve
    is spatially varying, it will be defined in pixel coordinates.

    Dictionary values may be None to indicate that no TransmissionCurve is
    valid after the date provided in the key.
    """
    qe = readTransmissionCurveFromFile("qe_ccd_HSC.txt", atMin=0.0, atMax=0.0)
    return {
        HSC_BEGIN: qe
    }


def getAtmosphereTransmission():
    """Return a dictionary of TransmissionCurves describing the atmospheric
    throughput at Mauna Kea.

    Dictionary keys are string dates (YYYY-MM-DD) indicating the beginning of
    the validity period for the curve stored as the associated dictionary
    value.  The curve is guaranteed not to be spatially-varying.

    Dictionary values may be None to indicate that no TransmissionCurve is
    valid after the date provided in the key.
    """
    average = readTransmissionCurveFromFile("modtran_maunakea_am12_pwv15_binned10ang.dat")
    return {
        HSC_BEGIN: average
    }


def getFilterTransmission():
    """Return a nested dictionary of TransmissionCurves describing the
    throughput of each HSC filter.

    Outer directionary keys are string dates (YYYY-MM-DD), with values
    a dictionary mapping filter name to TransmissionCurve.  If the curve
    is spatially varying, it will be defined in pixel coordinates.

    Filter curve names are in the long form used as data ID values (e.g.
    'HSC-I').

    Dictionary values may be None to indicate that no TransmissionCurve is
    valid after the date provided in the key.
    """
    g = {}
    filename = os.path.join(DATA_DIR, "filterTraces.py")
    exec(compile(open(filename), filename, mode='exec'), globals=g)
    result = {}
    for band, data in g["FILTER_DATA"].items():
        result[getLongFilterName(band)] = TransmissionCurve.makeRadial(
            throughput=data["T"], wavelengths=data["lam"]*10,
            radii=data['radius']/g["PIXEL_SIZE"],
            throughputAtMin=0.0, throughputAtMax=0.0
        )
    for filename in glob.glob(os.path.join(DATA_DIR, "wHSC-*.txt")):
        band = filename[len("wHSC-"): -len(".txt")]
        if band not in result:
            result[band] = readTransmissionCurveFromFile(filename, atMin=0.0, atMax=0.0)
    return result
