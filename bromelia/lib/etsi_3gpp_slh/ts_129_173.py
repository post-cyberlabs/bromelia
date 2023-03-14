# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_173
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 173.
    
    :copyright: (c) 2023-present Olivier Médoc.
    :license: MIT, see LICENSE for more details.
"""

from ..etsi_3gpp.ts_132_299 import LcsNameStringAVP
from ..etsi_3gpp.ts_132_299 import LcsFormatIndicatorAVP
from ..etsi_3gpp.ts_132_299 import LcsClientTypeAVP

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_172 import *
from ...types import *

class SlgLocationTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of SLg-Location-Type AVP in Section 7.4.2  
    of ETSI TS 129 172 V15.0.0 (2018-07).

    The SLg-Location-Type AVP (AVP Code 2500) is of type Enumerated.
    """
    code = SLG_LOCATION_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
    
    values = [
                SLG_LOCATION_TYPE_CURRENT_LOCATION,
                SLG_LOCATION_TYPE_CURRENT_OR_LAST_KNOWN_LOCATION,
                SLG_LOCATION_TYPE_INITIAL_LOCATION,
                SLG_LOCATION_TYPE_ACTIVATE_DEFERRED_LOCATION,
                SLG_LOCATION_TYPE_CANCEL_DEFERRED_LOCATION,
                SLG_LOCATION_TYPE_NOTIFICATION_VERIFICATION_ONLY,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SlgLocationTypeAVP.code,
                             SlgLocationTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class LcsEpsClientNameAVP(DiameterAVP, GroupedType):
    """Implementation of LCS-EPS-Client-Name AVP in Section 7.4.3  
    of ETSI TS 129 172 V15.0.0 (2018-07).

    The LCS-EPS-Client-Name AVP (AVP Code 2) is of type Grouped.
    """
    code = LCS_EPS_CLIENT_NAME_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "lcs_name_string": LcsNameStringAVP,
                    "lcs_format_indicator": LcsFormatIndicatorAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             LcsEpsClientNameAVP.code,
                             LcsEpsClientNameAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PlrFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of PLR-Flags AVP in Section 7.4.52  
    of ETSI TS 129 172 V15.0.0 (2018-07).

    The PLR-Flags AVP (AVP Code XXX) is of type Grouped.
    """
    code = ULR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PlrFlagsAVP.code,
                             PlrFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

