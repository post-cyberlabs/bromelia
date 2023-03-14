# -*- coding: utf-8 -*-
"""
    bromelia.constants.etsi_3gpp.ts_129_172
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains constants defined in ETSI TS 129 172.
    
    :copyright: (c) 2023-present Olivier Médoc.
    :license: MIT, see LICENSE for more details.
"""

from ..._internal_utils import convert_to_3_bytes
from ..._internal_utils import convert_to_4_bytes

#: Diameter Messages
PROVIDE_LOCATION_MESSAGE = convert_to_3_bytes(8388620)

#: Diameter AVPs
SLG_LOCATION_TYPE_AVP_CODE = convert_to_4_bytes(2500)
LCS_EPS_CLIENT_NAME_AVP_CODE = convert_to_4_bytes(2501)

#: List of Slg-Location-Type AVP values.
#: For more information, please refer to Section 7.4.2 of 
#: ETSI TS 129 172 V15.0.0 (2018-07).
SLG_LOCATION_TYPE_CURRENT_LOCATION = convert_to_4_bytes(0)
SLG_LOCATION_TYPE_CURRENT_OR_LAST_KNOWN_LOCATION = convert_to_4_bytes(1)
SLG_LOCATION_TYPE_INITIAL_LOCATION = convert_to_4_bytes(2)
SLG_LOCATION_TYPE_ACTIVATE_DEFERRED_LOCATION = convert_to_4_bytes(3)
SLG_LOCATION_TYPE_CANCEL_DEFERRED_LOCATION = convert_to_4_bytes(4)
SLG_LOCATION_TYPE_NOTIFICATION_VERIFICATION_ONLY = convert_to_4_bytes(5)
