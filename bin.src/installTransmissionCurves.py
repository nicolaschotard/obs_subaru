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
import argparse
import os

from lsst.afw.image import Filter
from lsst.obs.hsc import transmissionCurveData
from lsst.daf.persistence import Butler

DEFAULT_INPUT_NAME = "PIPE_INPUT_ROOT"
DEFAULT_CALIB_NAME = "PIPE_CALIB_ROOT"
DEFAULT_OUTPUT_NAME = "PIPE_OUTPUT_ROOT"


def getLongFilterName(short):
    # HSC tells afw.image.Filter that the short name is canonical
    # but uses the long name for its data IDs, so we need this hack
    # to get the long name from the short name.
    if short.startswith("HSC") or short.startswith("NB"):
        return short
    f = Filter(short)
    for a in f.getAliases():
        if a.startswith("HSC") or a.startswith("NB"):
            return a
    return short


def main(butler):
    for name, curve in transmissionCurveData.filters.items():
        butler.put(curve, "transmission_filter", filter=getLongFilterName(name))
    for ccd, curve in transmissionCurveData.sensors.items():
        butler.put(curve, "transmission_sensor", ccd=ccd)
    for epoch, curve in transmissionCurveData.optics.items():
        # epoch/versioning currently ignored; will be fixed in butler gen. 3
        # if not earlier
        butler.put(curve, "transmission_optics")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Install HSC transmission curve datasets into a data repository.")
    parser.add_argument('root', type=str, help="Directory of the root data repository.")
    parser.add_argument('--rerun', type=str, default=None, metavar="[INPUT:]OUTPUT",
                        help="rerun name: sets OUTPUT to ROOT/rerun/OUTPUT; "
                             "optionally sets ROOT to ROOT/rerun/INPUT")
    args = parser.parse_args()
    if args.rerun is not None:
        try:
            inputRerun, outputRerun = args.rerun.split(":")
            inputRoot = os.path.join(args.root, "rerun", inputRerun)
            outputRoot = os.path.join(args.root, "rerun", outputRerun)
        except ValueError:
            inputRoot = args.root
            outputRoot = os.path.join(args.root, "rerun", args.rerun)
        butler = Butler(inputs={'root': inputRoot, 'mode': 'r'},
                        outputs={'root': outputRoot, 'mode': 'rw'})
    else:
        butler = Butler(outputs={'root': args.repo, 'mode': 'rw'})
    main(butler)
