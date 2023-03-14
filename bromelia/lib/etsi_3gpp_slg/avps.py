# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp_slg.avps
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol AVP library that are used 
    to create Diameter messages for 3GPP Slg Application Id.
    
    :copyright: (c) 2023-present Olivier Médoc.
    :license: MIT, see LICENSE for more details.
"""

from ...avps.etsi_3gpp.ts_129_172 import SlgLocationTypeAVP
from ...avps.etsi_3gpp.ts_129_172 import LcsEpsClientNameAVP
from ...avps.etsi_3gpp.ts_129_172 import LcsClientTypeAVP
from ...avps.etsi_3gpp.ts_129_172 import PlrFlagsAVP

from ...avps.etsi_3gpp.ts_129_229 import SupportedFeaturesAVP

from ...avps.etsi_3gpp.ts_129_329 import MsisdnAVP

from ...avps.etsi_3gpp.ts_129_272 import ImeiAVP
from ...avps.etsi_3gpp.ts_129_272 import ServiceSelectionAVP

from ...avps.etsi_3gpp.ts_132_299 import LcsNameStringAVP

from ...avps.ietf.rfc6733 import SessionIdAVP
from ...avps.ietf.rfc6733 import AuthSessionStateAVP
from ...avps.ietf.rfc6733 import OriginHostAVP
from ...avps.ietf.rfc6733 import OriginRealmAVP
from ...avps.ietf.rfc6733 import DestinationHostAVP
from ...avps.ietf.rfc6733 import DestinationRealmAVP
from ...avps.ietf.rfc6733 import VendorSpecificApplicationIdAVP
from ...avps.ietf.rfc6733 import UserNameAVP
from ...avps.ietf.rfc6733 import ProxyInfoAVP
from ...avps.ietf.rfc6733 import RouteRecordAVP
from ...avps.ietf.rfc6733 import VendorIdAVP
from ...avps.ietf.rfc6733 import AuthApplicationIdAVP
