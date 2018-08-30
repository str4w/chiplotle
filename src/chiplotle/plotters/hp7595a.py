"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library

standard_library.install_aliases()
from chiplotle.plotters.drawingplotter import _DrawingPlotter


class HP7595A(_DrawingPlotter):
    def __init__(self, ser, **kwargs):
        self.allowedHPGLCommands = tuple(
            [
                "\x1b.",
                "AA",
                "AF",
                "AH",
                "AP",
                "AR",
                "AS",
                "BF",
                "BL",
                "CA",
                "CC",
                "CI",
                "CM",
                "CP",
                "CS",
                "CT",
                "CV",
                "DC",
                "DF",
                "DI",
                "DL",
                "DP",
                "DR",
                "DS",
                "DT",
                "EA",
                "EC",
                "EP",
                "ER",
                "ES",
                "EW",
                "FP",
                "FR",
                "FS",
                "FT",
                "GC",
                "GM",
                "GP",
                "IC",
                "IM",
                "IN",
                "IP",
                "IV",
                "IW",
                "KY",
                "LB",
                "LO",
                "LT",
                "NR",
                "OA",
                "OB",
                "OC",
                "OD",
                "OE",
                "OF",
                "OG",
                "OH",
                "OI",
                "OK",
                "OL",
                "OO",
                "OP",
                "OS",
                "OT",
                "OW",
                "PA",
                "PB",
                "PD",
                "PG",
                "PM",
                "PR",
                "PT",
                "PU",
                "RA",
                "RL",
                "RO",
                "RP",
                "RR",
                "SA",
                "SC",
                "SG",
                "SI",
                "SL",
                "SM",
                "SP",
                "SR",
                "SS",
                "TL",
                "UC",
                "UF",
                "VA",
                "VN",
                "VS",
                "WD",
                "WG",
                "XT",
                "YT",
            ]
        )

        _DrawingPlotter.__init__(self, ser, **kwargs)
        self.type = "HP7595A"