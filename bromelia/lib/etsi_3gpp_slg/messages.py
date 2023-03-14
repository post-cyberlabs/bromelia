# -*- coding: utf-8 -*-
"""
    bromelia.lib.etsi_3gpp_slg.messages
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains the Diameter protocol messages for 3GPP SLg
    Application Id.

    :copyright: (c) 2023-present Olivier Médoc.
    :license: MIT, see LICENSE for more details.
"""

import platform
import socket

from .avps import *

from ...base import DiameterRequest, DiameterAnswer
from ...constants import *


class ProvideLocationRequest(DiameterRequest):
    """Implementation of Provide-Location-Request (PLR) command as per 
    clause 7.3.1 of ETSI TS 129.172 V15.0.0 (2018-07).

    The Provide-Location-Request is indicated by the Command Code field set to 8388620
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
                    "destination_host": DestinationHostAVP,
                    "destination_realm": DestinationRealmAVP,
                    "slg_location_type": SlgLocationTypeAVP,
                    "lcs_eps_client_name": LcsEpsClientNameAVP,
                    "lcs_client_type": LcsClientTypeAVP,
                    
                    
    }
    optionals = { 
                    "vendor_specific_application_id": VendorSpecificApplicationIdAVP,
                    "user_name": UserNameAVP,
                    "msisdn": MsisdnAVP,
                    "imei": ImeiAVP,
                    #"lcs_request_name": LCSRequestorNameAVP,
                    #"lcs_priority": LCSPriorityAVP,
                    #"lcs_qos": LCSQoSAVP,
                    #"velocity_requested": VelocityRequestedAVP,
                    #"lcs_supported_gad_shapes": LCSSupportedGADShapesAVP,
                    #"lcs_service_type_id": LCSServiceTypeIdAVP,
                    #"lcs_codeword": LCSCodewordAVP,
                    #"lcs_privacy_check_non_session": LCSPrivacyCheckNonSessionAVP,
                    #"lcs_privacy_check_session": LCSPrivacyCheckSessionAVP,
                    "service_selection": ServiceSelectionAVP,
                    #"deferred_location_type": DeferredLocationTypeAVP,
                    "plr_flags": PlrFlagsAVP,
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
                 slg_location_type=None,
                 lcs_eps_client_name=None,
                 lcs_client_type=None,
                 vendor_specific_application_id=[VendorIdAVP(VENDOR_ID_3GPP), AuthApplicationIdAVP(DIAMETER_APPLICATION_SLg)],
                 user_name=None,
                 msisdn=None,
                 imei=None,
                 service_selection=None,
                 plr_flags=None,
                 supported_features=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        DiameterRequest.__init__(self, 
                                command_code=PROVIDE_LOCATION_MESSAGE, 
                                application_id=DIAMETER_APPLICATION_SLg)

        DiameterRequest._load(self, locals())

