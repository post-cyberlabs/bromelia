# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_336
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 336.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_336 import *
from ...types import *


class ScefIdAVP(DiameterAVP, DiameterIdentityType):
    """Implementation of SCEF-ID AVP in Section 8.4.5 
    of ETSI TS 129 336 V14.2.0 (2017-07).

    The SCEF-ID AVP (AVP Code 3125) is of type DiameterIdentity.
    """
    code = SCEF_ID_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SCEFIdAVP.code,
                             SCEFIdAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        DiameterIdentityType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)
