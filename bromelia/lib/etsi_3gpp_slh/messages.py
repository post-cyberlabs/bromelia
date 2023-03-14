# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_slh.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP SLh
    Application Id.

    :copyright: (c) 2023-present Olivier Médoc.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from ...base import DiameterRequest, DiameterAnswer
from ...constants import *


class LcsRoutingInfoRequest(DiameterRequest):
    """Implementation of LCS-Routing-Info-Request (RIR) command as per 
    clause 6.2.3 of ETSI TS 129.173 V12.2.0 (2014-10).

    The LCS-Routing-Info-Request is indicated by the Command Code field set to 8388622
    and Command Flag's 'R' bit set.

    Usage::

        >>> from bromelia.lib.etsi_3gpp_s6b import AAA
        >>> aaa_avps = {
        ...     "mip6_feature_vector": 70368744177664,
        ...     "session_timeout": 10800,
        ... }
        >>> aaa = AAA(**aaa_avps)
        >>> aaa
        <Diameter Message: 265 [AAA] PXY, 16777272 [3GPP S6b], 8 AVP(s)>        
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "auth_session_state": AuthSessionStateAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
    }
    optionals = {
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "destination_host": DestinationHostAVP,
                    "user_name": UserNameAVP,
                    "msisdn": MsisdnAVP,
                    "gmlc_number": GmlcNumberAVP,
                    "supported_features": SupportedFeaturesAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP,
    }

    def __init__(self,
                 session_id=platform.node(),
                 auth_session_state=NO_STATE_MAINTAINED,
                 origin_host=platform.node(), 
                 origin_realm=socket.getfqdn(), 
                 destination_host=None,
                 destination_realm=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SLh)],
                 user_name=None,
                 msisdn=None,
                 gmlc_number=None,
                 supported_features=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                command_code=LCS_ROUTING_INFO_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_SLh)

        DiameterRequest._load(self, locals())

