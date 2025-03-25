# -*- coding: utf-8 -*-
"""
    bromelia.etsi_3gpp.ts_129_272
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains Diameter AVP classes defined in ETSI TS 129 272.
    
    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from ..etsi_3gpp.ts_129_061 import X3gppChargingCharacteristicsAVP

from ..etsi_3gpp.ts_129_212 import PreEmptionCapabilityAVP
from ..etsi_3gpp.ts_129_212 import PreEmptionVulnerabilityAVP
from ..etsi_3gpp.ts_129_212 import PriorityLevelAVP
from ..etsi_3gpp.ts_129_212 import QosClassIdentifierAVP

from ..etsi_3gpp.ts_129_214 import MaxRequestedBandwidthDlAVP
from ..etsi_3gpp.ts_129_214 import MaxRequestedBandwidthUlAVP

from ..etsi_3gpp.ts_129_229 import VisitedNetworkIdentifierAVP

from ..etsi_3gpp.ts_129_329 import MsisdnAVP

from ..ietf.rfc5447 import Mip6AgentInfoAVP

from ...base import DiameterAVP
from ...constants.etsi_3gpp.ts_129_272 import *
from ...exceptions import AVPAttributeValueError
from ...types import *
from ...utils import decode_from_tbcd, encode_to_tbcd

import datetime
import struct

class StnSrAVP(DiameterAVP, OctetStringType):
    """Implementation of STN-SR AVP in Section 7.3.39 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The STN-SR AVP (AVP Code 1433) is of type OctetString.
    """
    code = STN_SR_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             StnSrAVP.code,
                             StnSrAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=self.encode(data), vendor_id=VENDOR_ID_3GPP)


    def encode(self, data):
        if isinstance(data, int):
            return bytes.fromhex(encode_to_tbcd(data))

        elif isinstance(data, str):
            return bytes.fromhex(encode_to_tbcd(int(data)))

        elif isinstance(data, bytes):
            return data


    def decode(self):
        return decode_from_tbcd(self.data)


class AmbrAVP(DiameterAVP, GroupedType):
    """Implementation of AMBR AVP in Section 7.3.41 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The AMBR AVP (AVP Code 1435) is of type Grouped.
    """
    code = AMBR_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "max_requested_bandwidth_ul": MaxRequestedBandwidthUlAVP,
                    "max_requested_bandwidth_dl": MaxRequestedBandwidthDlAVP,
    }
    optionals = {
                    # "extended_max_requested_bw_ul": ExtendedMaxRequestedBwUlAVP,
                    # "extended_max_requested_bw_dl": ExtendedMaxRequestedBwDlAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AmbrAVP.code,
                             AmbrAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SubscriberStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of Subscriber-Status AVP in Section 7.3.29 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Subscriber-Status AVP (AVP code 1424) is of type Enumerated.
    """
    code = SUBSCRIBER_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                 SUBSCRIBER_STATUS_SERVICE_GRANTED,
                 SUBSCRIBER_STATUS_OPERATOR_DETERMINED_BARRING,
     ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SubscriberStatusAVP.code,
                             SubscriberStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ContextIdentifierAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Context-Identifier AVP in Section 7.3.27
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Context-Identifier AVP (AVP Code 1423) is of type Unsigned32.
    """
    code = CONTEXT_IDENTIFIER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ContextIdentifierAVP.code,
                             ContextIdentifierAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PdnTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of PDN-Type AVP in Section 7.3.62 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The PDN-Type AVP (AVP Code 1456) is of type Enumerated.
    """
    code = PDN_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                PDN_TYPE_IPV4,
                PDN_TYPE_IPV6,
                PDN_TYPE_IPV4V6,
                PDN_TYPE_IPV4_OR_IPV6
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PdnTypeAVP.code,
                             PdnTypeAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServiceSelectionAVP(DiameterAVP, UTF8StringType):
    """Implementation of Service-Selection AVP in Section 7.3.36
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Service-Selection AVP (AVP Code 493) is of type UTF8String.
    """
    code = SERVICE_SELECTION_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ServiceSelectionAVP.code,
                             ServiceSelectionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class AllocationRetentionPriorityAVP(DiameterAVP, GroupedType):
    """Implementation of Allocation-Retention-Priority AVP in Section 7.3.40 
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Allocation-Retention-Priority AVP (AVP Code 1034) is of type Grouped.
    """
    code = ALLOCATION_RETENTION_PRIORITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "priority_level": PriorityLevelAVP
    }
    optionals = {
                    "pre_emption_capability": PreEmptionCapabilityAVP,
                    "pre_emption_vulnerability": PreEmptionVulnerabilityAVP

    }

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             AllocationRetentionPriorityAVP.code,
                             AllocationRetentionPriorityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EpsSubscribedQosProfileAVP(DiameterAVP, GroupedType):
    """Implementation of EPS-Subscribed-QoS-Profile AVP in Section 7.3.37 
    of ETSI TS 129 272 V15.10.0 (2020-01)

    The EPS-Subscribed-QoS-Profile AVP (AVP Code 1431) is of type Grouped.
    """
    code = EPS_SUBSCRIBED_QOS_PROFILE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "qos_class_identifier": QosClassIdentifierAVP,
                    "allocation_retention_priority": AllocationRetentionPriorityAVP
    }
    optionals = {}

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             EpsSubscribedQosProfileAVP.code,
                             EpsSubscribedQosProfileAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class VplmnDynamicAddressAllowedAVP(DiameterAVP, EnumeratedType):
    """Implementation of VPLMN-Dynamic-Address-Allowed AVP in Section 7.3.38 
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The VPLMN-Dynamic-Address-Allowed AVP (AVP Code 1432) is of type 
    Enumerated.
    """
    code = VPLMN_DYNAMIC_ADDRESS_ALLOWED_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                VPLMN_DYNAMIC_ADDRESS_ALLOWED_NOT_ALLOWED,
                VPLMN_DYNAMIC_ADDRESS_ALLOWED_ALLOWED
    ]


    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             VplmnDynamicAddressAllowedAVP.code,
                             VplmnDynamicAddressAllowedAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PdnGwAllocationTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of PDN-GW-Allocation-Type AVP in Section 7.3.44 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The PDN-GW-Allocation-Type AVP (AVP Code 1438) is of type Enumerated.
    """
    code = PDN_GW_ALLOCATION_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                PDN_GW_ALLOCATION_TYPE_STATIC,
                PDN_GW_ALLOCATION_TYPE_DYNAMIC
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PdnGwAllocationTypeAVP.code,
                             PdnGwAllocationTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ApnConfigurationAVP(DiameterAVP, GroupedType):
    """Implementation of APN-Configuration AVP in Section 7.3.35 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The APN-Configuration AVP (AVP Code 1430) is of type Grouped.
    """
    code = APN_CONFIGURATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "context_identifier": ContextIdentifierAVP,
                    "pdn_type": PdnTypeAVP,
                    "service_selection": ServiceSelectionAVP,
    }
    optionals = {
                    # "served_party_ip_address": ServedPartyIdAddressAVP,
                    "eps_subscribed_qos_profile": EpsSubscribedQosProfileAVP,
                    "vplmn_dynamic_address_allowed": VplmnDynamicAddressAllowedAVP,
                    "mip6_agent_info": Mip6AgentInfoAVP,
                    "visited_network_identifier": VisitedNetworkIdentifierAVP,
                    "pdn_gw_allocation_type": PdnGwAllocationTypeAVP,
                    "x3gpp_charging_characteristics": X3gppChargingCharacteristicsAVP,
                    "ambr": AmbrAVP,
                    # "specific_apn_info": SpecificApnInfoAVP,
                    # "apn_oi_replacement": ApnOiReplacementAVP,
                    # "sipto_permission": SiptoPermissionAVP,
                    # "lipa_permission": LipaPermissionAVP,
                    # "restoration_priority": RestorationPriorityAVP,
                    # "sipto_local_network_permission": SiptoLocalNetworkPermissionAVP,
                    # "wlan_offloadability": WlanOffloadabilityAVP,
                    # "non_ip_pdn_type_indicator": NonIpPdnTypeIndicatorAVP,
                    # "non_ip_data_delivery_mechanism": NonIpDataDeliveryMechanismAVP,
                    # "scef_id": ScefIdAVP,
                    # "scef_realm": ScefRealmAVP,
                    # "preferred_data_mode": PreferredDataModeAVP,
                    # "pdn_connectivity_continuity": PdnConnectivityContinuityAVP,
                    # "rds_indicator": RdsIndicatorAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ApnConfigurationAVP.code,
                             ApnConfigurationAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AllApnConfigurationsIncludedIndicatorAVP(DiameterAVP, EnumeratedType):
    """Implementation of All-APN-Configurations-Included-Indicator AVP in 
    Section 7.3.33 of ETSI TS 129 272 V15.4.0 (2018-07).

    The All-APN-Configurations-Included-Indicator AVP (AVP Code 1428) is of 
    type Enumerated.
    """
    code = ALL_APN_CONFIGURATIONS_INCLUDED_INDICATOR_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                ALL_APN_CONFIGURATIONS_INCLUDED,
                MODIFIED_ADDED_APN_CONFIGURATIONS_INCLUDED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AllApnConfigurationsIncludedIndicatorAVP.code,
                             AllApnConfigurationsIncludedIndicatorAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)    
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ApnConfigurationProfileAVP(DiameterAVP, GroupedType):
    """Implementation of APN-Configuration-Profile AVP in Section 7.3.34 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The APN-Configuration-Profile AVP (AVP Code 1429) is of type Grouped.
    """
    code = APN_CONFIGURATION_PROFILE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "context_identifier": ContextIdentifierAVP,
                    "all_apn_configurations_included_indicator": AllApnConfigurationsIncludedIndicatorAVP,
                    "apn_configuration": ApnConfigurationAVP,
    }
    optionals = {
                    # "additional_context_identifier": AdditionalContextIdentifierAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ApnConfigurationProfileAVP.code,
                             ApnConfigurationProfileAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UeUsageTypeAVP(DiameterAVP, Unsigned32Type):
    """Implementation of UE-Usage-Type AVP in Section 7.3.202 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The UE-Usage-Type AVP (AVP Code 1680) is of type Unsigned32.
    """
    code = UE_USAGE_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UeUsageTypeAVP.code,
                             UeUsageTypeAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class OperatorDeterminedBarringAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Operator-Determined-Barring AVP in Section 7.3.30 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Operator-Determined-Barring AVP (AVP Code 1425) is of type Unsigned32.
    """
    code = OPERATOR_DETERMINED_BARRING_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data=convert_to_4_bytes(0)):
        DiameterAVP.__init__(self, 
                             OperatorDeterminedBarringAVP.code,
                             OperatorDeterminedBarringAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SubscriptionDataAVP(DiameterAVP, GroupedType):
    """Implementation of Subscription-Data AVP in Section 7.3.2 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Subscription-Data AVP (AVP Code 1400) is of type Grouped.
    """
    code = SUBSCRIPTION_DATA_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    optionals = {
                    "subscriber_status": SubscriberStatusAVP,
                    "msisdn": MsisdnAVP,
                    # "a_msisdn": AMsisdnAVP,
                    "stn_sr": StnSrAVP,
                    # "ics_indicator": IcsIndicatorAVP,
                    # "network_access_mode": NetworkAccessModeAVP,
                    "operator_determined_barring": OperatorDeterminedBarringAVP,
                    # "hplmn_odb": HplmnOdbAVP,
                    # "regional_subscription_zone_code": RegionalSubscriptionZoneCodeAVP,
                    # "access_restriction_data": AccessRestrictionDataAVP,
                    # "apn_oi_replacement": ApnOiReplacementAVP,
                    # "lcs_info": LcsInfoAVP,
                    # "teleservice_list": TeleserviceListAVP,
                    # "call_barring_info": CallBarringInfoAVP,
                    "x3pp_charging_characteristics": X3gppChargingCharacteristicsAVP,
                    "ambr": AmbrAVP,
                    "apn_configuration_profile": ApnConfigurationProfileAVP,
                    # "rat_frequency_selection_priority_id": RatFrequencySelectionPriorityIdAVP,
                    # "trace_data": TraceDataAVP,
                    # "gprs_subscription_data": GprsSubscriptionDataAVP,
                    # "mps_priority": MpsPriorityAVP,
                    # "vplmn_lipa_allowed": VplmnLipaAllowedAVP,
                    # "relay_node_indicator": RelayNodeIndicatorAVP,
                    # "mdt_user_consent": MdtUserConsentAVP,
                    # "subscribed_vsrvcc": SubscribedVsrvccAVP,
                    # "prose_subscription_data": ProseSubscriptionDataAVP,
                    # "subscription_data_flags": SubscriptionDataFlagsAVP,
                    # "adjacent_access_restriction_data": AdjacentAccessRestrictionDataAVP,
                    # "dl_buffering_suggested_packet_count": DlBufferingSuggestedPacketCountAVP,
                    # "imsi_group_id": ImsiGroupIdAVP,
                    "ue_usage_type": UeUsageTypeAVP,
                    # "aese_communication_pattern": AeseCommunicationPatternAVP,
                    # "monitoring_event_configuration": MonitoringEventConfigurationAVP,
                    # "emergency_info": EmergencyInfoAVP,
                    # "v2x_subscription_data": V2xSubscriptionDataAVP,
                    # "edrx_cycle_length": EdrxCycleLengthAVP,
                    # "external_identifier": ExternalIdentifierAVP,
                    # "active_time": ActiveTimeAVP,
                    # "service_gap_time": ServiceGapTimeAVP,
                    # "broadcast_location_assistance_data_types": BroadcastLocationAssistanceDataTypesAVP,
                    # "aerial_ue_subscription_information": AerialUeSubscriptionInformationAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SubscriptionDataAVP.code,
                             SubscriptionDataAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ImeiAVP(DiameterAVP, UTF8StringType):
    """Implementation of IMEI AVP in Section 7.3.4 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The IMEI AVP (AVP Code 1402) is of type UTF8String.
    """
    code = IMEI_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ImeiAVP.code,
                             ImeiAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class NumberOfRequestedVectorsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Number-Of-Requested-Vectors AVP in Section 7.3.14 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Number-Of-Requested-Vectors AVP (AVP Code 1410) is of type Unsigned32.
    """
    code = NUMBER_OF_REQUESTED_VECTORS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             NumberOfRequestedVectorsAVP.code,
                             NumberOfRequestedVectorsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ReSynchronizationInfoAVP(DiameterAVP, OctetStringType):
    """Implementation of Re-Synchronization-Info AVP in Section 7.3.15 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Re-Synchronization-Info AVP (AVP Code 1411) is of type OctetString.
    """
    code = RE_SYNCHRONIZATION_INFO_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ReSynchronizationInfoAVP.code,
                             ReSynchronizationInfoAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ImmediateResponsePreferredAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Immediate-Response-Preferred AVP in Section 7.3.16 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Immediate-Response-Preferred AVP (AVP Code 1412) is of type Unsigned32.
    """
    code = IMMEDIATE_RESPONSE_PREFERRED_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ImmediateResponsePreferredAVP.code,
                             ImmediateResponsePreferredAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class RequestedEutranAuthenticationInfoAVP(DiameterAVP, GroupedType):
    """Implementation of Requested-EUTRAN-Authentication-Info AVP in 
    Section 7.3.11 of ETSI TS 129 272 V15.10.0 (2020-01).

    The Requested-EUTRAN-Authentication-Info AVP (AVP Code 1408) is of type 
    Grouped.
    """
    code = REQUESTED_EUTRAN_AUTHENTICATION_INFO_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {}
    optionals = {
                    "number_of_requested_vectors": NumberOfRequestedVectorsAVP,
                    "immediate_response_preferred": ImmediateResponsePreferredAVP,
                    "re_synchronization_info": ReSynchronizationInfoAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             RequestedEutranAuthenticationInfoAVP.code,
                             RequestedEutranAuthenticationInfoAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SoftwareVersionAVP(DiameterAVP, UTF8StringType):
    """Implementation of Software-Version AVP in Section 7.3.5 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Software-Version AVP (AVP Code 1403) is of type UTF8String.
    """
    code = SOFTWARE_VERSION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SoftwareVersionAVP.code,
                             SoftwareVersionAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class TerminalInformationAVP(DiameterAVP, GroupedType):
    """Implementation of Terminal-Information AVP in Section 5.3.14 of
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Terminal-Information AVP (AVP Code 1401) is of type Grouped.
    """
    code = TERMINAL_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {}
    optionals = {
                     "imei": ImeiAVP,
                    # "x3gpp2_meid": x3gpp2MeidAVP,
                    "software_version": SoftwareVersionAVP       
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             TerminalInformationAVP.code,
                             TerminalInformationAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EquipmentStatusAVP(DiameterAVP, EnumeratedType):
    """Implementation of Equipment-Status AVP in Section 7.3.51 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Equipment-Status AVP (AVP Code 1445) is of type Enumerated.
    """
    code = EQUIPMENT_STATUS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                EQUIPMENT_STATUS_WHITELISTED,
                EQUIPMENT_STATUS_BLACKLISTED,
                EQUIPMENT_STATUS_GREYLISTED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             EquipmentStatusAVP.code,
                             EquipmentStatusAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UlrFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of ULR-Flags AVP in Section 7.3.7 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The ULR-Flags AVP (AVP Code 1405) is of type Unsigned32.
    """
    code = ULR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UlrFlagsAVP.code,
                             UlrFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

class IdrFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of IDR-Flags AVP in Section 7.3.103 of 
    ETSI TS 129 272 V15.8.0 (2019-07).

    The IDR-Flags AVP (AVP Code 1490) is of type Unsigned32.
    """
    code = IDR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             IdrFlagsAVP.code,
                             IdrFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


################
### ISD AVPs ###
################
#: List of User-State AVP values.
#: For more information, please refer to Section 7.3.114 of
#: ETSI TS 129 272 V15.4.0 (2018-07)
USER_STATE_DETACHED = convert_to_4_bytes(0)
USER_STATE_ATTACHED_NOT_REACHABLE_FOR_PAGING = convert_to_4_bytes(1)
USER_STATE_ATTACHED_REACHABLE_FOR_PAGING = convert_to_4_bytes(2)
USER_STATE_CONNECTED_NOT_REACHABLE_FOR_PAGING = convert_to_4_bytes(3)
USER_STATE_CONNECTED_REACHABLE_FOR_PAGING = convert_to_4_bytes(4)
USER_STATE_RESERVED = convert_to_4_bytes(5)

#: List of Daylight-Saving-Time AVP values.
#: For more information, please refer to Section 7.3.164 of
#: ETSI TS 129 272 V15.4.0 (2018-07)
DAYLIGHT_SAVING_TIME_NO_ADJUSTMENT = convert_to_4_bytes(0)
DAYLIGHT_SAVING_TIME_PLUS_ONE_HOUR_ADJUSTMENT = convert_to_4_bytes(1)
DAYLIGHT_SAVING_TIME_PLUS_TWO_HOURS_ADJUSTMENT = convert_to_4_bytes(2)

DSA_FLAGS_AVP_CODE = convert_to_4_bytes(1422)
USER_STATE_AVP_CODE = convert_to_4_bytes(1499)
IMS_VOICE_OVER_PS_SESSIONS_SUPPORTED = convert_to_4_bytes(1492)
SGSN_USER_STATE_AVP_CODE = convert_to_4_bytes(1601)
MME_USER_STATE_AVP_CODE = convert_to_4_bytes(1497)
EPS_USER_STATE_AVP_CODE = convert_to_4_bytes(1495)
LAST_UE_ACTIVITY_TIME_AVP_CODE = convert_to_4_bytes(1494)
EPS_LOCATION_INFORMATION_AVP_CODE = convert_to_4_bytes(1496)
IDA_FLAGS_AVP_CODE = convert_to_4_bytes(1441)
SGSN_LOCATION_INFORMATION_AVP_CODE = convert_to_4_bytes(1601)
MME_LOCATION_INFORMATION_AVP_CODE = convert_to_4_bytes(1600)
AGE_OF_LOCATION_INFORMATION_AVP_CODE = convert_to_4_bytes(1611)
EUTRAN_CELL_GLOBAL_IDENTITY_AVP_CODE = convert_to_4_bytes(1602)
TRACKING_AREA_IDENTITY_AVP_CODE = convert_to_4_bytes(1603)
CELL_GLOBAL_IDENTITY_AVP_CODE = convert_to_4_bytes(1604)
LOCATION_AREA_IDENTITY_AVP_CODE = convert_to_4_bytes(1606)
SERVICE_AREA_IDENTITY_AVP_CODE = convert_to_4_bytes(1607)
ROUTING_AREA_IDENTITY_AVP_CODE = convert_to_4_bytes(1605)
TIME_ZONE_AVP_CODE = convert_to_4_bytes(1642)
DAYLIGHT_SAVING_TIME_AVP_CODE = convert_to_4_bytes(1650)
LOCAL_TIME_ZONE_AVP_CODE = convert_to_4_bytes(1649)


def convert_from_4_bytes(content: bytes) -> int:
    return struct.unpack(">L", content)[0]


from typing import Any
class CellIdentityType(OctetStringType):

    @abc.abstractmethod
    def __init__(self, data, vendor_id=None):
        OctetStringType.__init__(self, data, vendor_id)

    def decode_tbcd(self, chars: bytes) -> str:
        
        number=''

        for char in chars:
            for val in (char & 0xF, char >> 4):
                if val != 0xF:
                    number += str(val) 

        return number
    
    def decode_mncmcc(self) -> tuple[str,str]:
        vals = self.decode_tbcd(self.data[0:3])
        return vals[0:3], vals[3:]


    def decode(self) -> tuple[str,str,Any]:
        vals = self.decode_mncmcc()
        return vals[0], vals[1], self.decode_tbcd(self.data[3:])


class IdaFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of IDA-Flags AVP in Section 7.3.47 of 
    ETSI TS 129 272 V15.8.0 (2019-07).

    The IDA-Flags AVP (AVP Code 1441) is of type Unsigned32.
    """
    code = IDA_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             IdaFlagsAVP.code,
                             IdaFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class DsrFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of DSR-Flags AVP in Section 7.3.25 of 
    ETSI TS 129 272 V15.08.0 (2019-07).

    The DSR-Flags AVP (AVP Code 1421) is of type Unsigned32.
    """
    code = DSR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             DsrFlagsAVP.code,
                             DsrFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class DsaFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of DSA-Flags AVP in Section 7.3.26 of 
    ETSI TS 129 272 V15.08.0 (2019-07).

    The DSA-Flags AVP (AVP Code 1422) is of type Unsigned32.
    """
    code = DSA_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             DsaFlagsAVP.code,
                             DsaFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UlaFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of ULA-Flags AVP in Section 7.3.8 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The ULA-Flags AVP (AVP Code 1406) is of type Unsigned32.
    """
    code = ULA_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UlaFlagsAVP.code,
                             UlaFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AirFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of AIR-Flags AVP in Section 7.3.201 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The AIR-Flags AVP (AVP Code 1679) is of type Unsigned32.
    """
    code = AIR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AirFlagsAVP.code,
                             AirFlagsAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class NorFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of NOR-Flags AVP in Section 7.3.49 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The NOR-Flags AVP (AVP Code 1443) is of type Unsigned32.
    """
    code = NOR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             NorFlagsAVP.code,
                             NorFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UserIdAVP(DiameterAVP, UTF8StringType):
    """Implementation of User-Id AVP in Section 7.3.50 pf ETSI TS 129 272 V15.4.0 (2018-07).

    The User-Id AVP (AVP Code 1) is of type UTF8String.
    """
    code = USER_ID_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             UserIdAVP.code,
                             UserIdAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        UTF8StringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PurFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of PUR-Flags AVP in Section 7.3.149 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The PUR-Flags AVP (AVP Code 1635) is of type Unsigned32.
    """
    code = PUR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PurFlagsAVP.code,
                             PurFlagsAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class PuaFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of PUA-Flags AVP in Section 7.3.49 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The PUA-Flags AVP (AVP Code 1442) is of type Unsigned32.
    """
    code = PUA_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             PuaFlagsAVP.code,
                             PuaFlagsAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AlertReasonAVP(DiameterAVP, EnumeratedType):
    """Implementation of Alert-Reason AVP in Section 7.3.83 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Alert-Reason AVP (AVP Code 1434) is of type Enumerated.
    """
    code = ALERT_REASON_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                ALERT_REASON_UE_PRESET,
                ALERT_REASON_UE_MEMORY_AVAILABLE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AlertReasonAVP.code,
                             AlertReasonAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ErrorDiagnosticAVP(DiameterAVP, EnumeratedType):
    """Implementation of Error-Diagnostic AVP in Section 7.3.128 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Error-Diagnostic AVP (AVP Code 1614) is of type Enumerated.
    """
    code = ERROR_DIAGNOSTIC_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                ERROR_DIAGNOSTIC_GPRS_DATA_SUBSCRIBED,
                ERROR_DIAGNOSTIC_NO_GPRS_DATA_SUBSCRIBED,
                ERROR_DIAGNOSTIC_ODB_ALL_APN,
                ERROR_DIAGNOSTIC_ODB_HPLMN_APN,
                ERROR_DIAGNOSTIC_ODB_VPLMN_APN
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ErrorDiagnosticAVP.code,
                             ErrorDiagnosticAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class VisitedPlmnIdAVP(DiameterAVP, OctetStringType):
    """Implementation of Visited-PLMN-Id AVP in Section 7.3.9 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Visited-PLMN-Id AVP (AVP Code 1407) is of type OctetString.
    """
    code = VISITED_PLMN_ID_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             VisitedPlmnIdAVP.code,
                             VisitedPlmnIdAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ItemNumberAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Item-Number AVP in Section 7.3.23 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Item-Number AVP (AVP Code 1419) is of type Unsigned32.
    """
    code = ITEM_NUMBER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ItemNumberAVP.code,
                             ItemNumberAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class RandAVP(DiameterAVP, OctetStringType):
    """Implementation of RAND AVP in Section 7.3.53 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The RAND AVP (AVP Code 1447) is of type OctetString.
    """
    code = RAND_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             RandAVP.code,
                             RandAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class XresAVP(DiameterAVP, OctetStringType):
    """Implementation of XRES AVP in Section 7.3.54 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The XRES AVP (AVP Code 1448) is of type OctetString.
    """
    code = XRES_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             XresAVP.code,
                             XresAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AutnAVP(DiameterAVP, OctetStringType):
    """Implementation of AUTN AVP in Section 7.3.55 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The AUTN AVP (AVP Code 1449) is of type OctetString.
    """
    code = AUTN_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AutnAVP.code,
                             AutnAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class KasmeAVP(DiameterAVP, OctetStringType):
    """Implementation of KASME AVP in Section 7.3.56 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The KASME AVP (AVP Code 1450) is of type OctetString.
    """
    code = KASME_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             KasmeAVP.code,
                             KasmeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EUtranVectorAVP(DiameterAVP, GroupedType):
    """Implementation of E-UTRAN-Vector AVP in Section 7.3.18 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The E-UTRAN-Vector AVP (AVP Code 1414) is of type Grouped.
    """
    code = E_UTRAN_VECTOR_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {}
    optionals = {
                     "item_number": ItemNumberAVP,
                     "rand": RandAVP,
                     "xres": XresAVP,
                     "autn": AutnAVP,
                     "kasme": KasmeAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             EUtranVectorAVP.code,
                             EUtranVectorAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class AuthenticationInfoAVP(DiameterAVP, GroupedType):
    """Implementation of Authentication-Info AVP in Section 7.3.17 of
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Authentication-Info AVP (AVP Code 1413) is of type Grouped.
    """
    code = AUTHENTICATION_INFO_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {}
    optionals = {
                     "e_utran_vector": EUtranVectorAVP,
                    #  "utran_vector": UtranVectorAVP,
                    #  "geran_vector": GeranVectorAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             AuthenticationInfoAVP.code,
                             AuthenticationInfoAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class HomogeneousSupportOfImsVoiceOverPsSessionsAVP(DiameterAVP, EnumeratedType):
    """Implementation of Homogeneous-Support-of-IMS-Voice-Over-PS-Sessions AVP 
    in Section 7.3.107 of ETSI TS 129 272 V15.4.0 (2018-07).

    The Homogeneous-Support-of-IMS-Voice-Over-PS-Sessions AVP (AVP Code 1493) 
    is of type Enumerated.
    """
    code = HOMOGENEOUS_SUPPORT_OF_IMS_VOICE_OVER_PS_SESSION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                IMS_VOICE_OVER_PS_NOT_SUPPORTED,
                IMS_VOICE_OVER_PS_SUPPORTED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             HomogeneousSupportOfImsVoiceOverPsSessionsAVP.code,
                             HomogeneousSupportOfImsVoiceOverPsSessionsAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class UeSrvccCapabilityAVP(DiameterAVP, EnumeratedType):
    """Implementation of UE-SRVCC-Capability AVP in Section 7.3.130 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The UE-SRVCC-Capability AVP (AVP Code 1615) is of type Enumerated.
    """
    code = UE_SRVCC_CAPABILITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                UE_SRVCC_NOT_SUPPORTED,
                UE_SRVCC_SUPPORTED
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             UeSrvccCapabilityAVP.code,
                             UeSrvccCapabilityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SupportedServicesAVP(DiameterAVP, GroupedType):
    """Implementation of Supported-Services AVP in Section 7.3.199 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Supported-Services AVP (AVP Code 3143) is of type Grouped.
    """
    code = SUPPORTED_SERVICES_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SupportedServicesAVP.code,
                             SupportedServicesAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SupportedMonitoringEventsAVP(DiameterAVP, Unsigned64Type):
    """Implementation of Supported-Monitoring-Events AVP in Section 7.3.200 of 
    ETSI TS 129 272 V15.10.0 (2020-01).

    The Supported-Monitoring-Events AVP (AVP Code 3144) is of type Unsigned64.
    """
    code = SUPPORTED_MONITORING_EVENTS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             SupportedMonitoringEventsAVP.code,
                             SupportedMonitoringEventsAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned64Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class CancellationTypeAVP(DiameterAVP, EnumeratedType):
    """Implementation of Cancellation-Type AVP in Section 7.3.24 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The Cancellation-Type AVP (AVP Code 1420) is of type Enumerated.
    """
    code = CANCELLATION_TYPE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
                CANCELLATION_TYPE_MME_UPDATE_PROCEDURE,
                CANCELLATION_TYPE_SGSN_UPDATE_PROCEDURE,
                CANCELLATION_TYPE_SUBSCRIPTION_WITHDRAWAL,
                CANCELLATION_TYPE_UPDATE_PROCEDURE_IWF,
                CANCELLATION_TYPE_INITIAL_ATTACH_PROCEDURE
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             CancellationTypeAVP.code,
                             CancellationTypeAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ClrFlagsAVP(DiameterAVP, Unsigned32Type):
    """Implementation of CLR-Flags AVP in Section 7.3.152 of 
    ETSI TS 129 272 V15.4.0 (2018-07).

    The CLR-Flags AVP (AVP Code 1638) is of type Unsigned32.
    """
    code = CLR_FLAGS_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             ClrFlagsAVP.code,
                             ClrFlagsAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class GmlcNumberAVP(DiameterAVP, OctetStringType):
    """Implementation of GMLC-Number AVP in Section 7.3.85 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The GMLC-Number AVP (AVP Code 1474) is of type OctetString.
    """
    code = GMLC_NUMBER_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             GmlcNumberAVP.code,
                             GmlcNumberAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        DiameterAVP.set_vendor_id_bit(self, True)
        OctetStringType.__init__(self, data=self.encode(data), vendor_id=VENDOR_ID_3GPP)


    def encode(self, data):
        if isinstance(data, int):
            return bytes.fromhex(encode_to_tbcd(data))

        elif isinstance(data, str):
            return bytes.fromhex(encode_to_tbcd(int(data)))

        elif isinstance(data, bytes):
            return data


    def decode(self):
        return decode_from_tbcd(self.data)


class ImsVoiceOverPsSessionsSupportedAVP(DiameterAVP, EnumeratedType):
    """Implementation of IMS-Voice-Over-PS-Sessions-Supported AVP in Section 7.3.106 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The IMS-Voice-Over-PS-Sessions-Supported AVP (AVP Code 1492) is of type Enumerated.
    """
    code = IMS_VOICE_OVER_PS_SESSIONS_SUPPORTED
    vendor_id = VENDOR_ID_3GPP

    values = [
            IMS_VOICE_OVER_PS_NOT_SUPPORTED,
            IMS_VOICE_OVER_PS_SUPPORTED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             ImsVoiceOverPsSessionsSupportedAVP.code,
                             ImsVoiceOverPsSessionsSupportedAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class LastUeActivityTimeAVP(DiameterAVP, TimeType):
    """Implementation of Last-UE-Activity-Time AVP in Section 7.3.108 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The Last-UE-Activity-Time AVP (AVP Code 1494) is of type Time.
    """
    code = LAST_UE_ACTIVITY_TIME_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             LastUeActivityTimeAVP.code,
                             LastUeActivityTimeAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        TimeType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


    def decode(self):
        ref1900 = datetime.datetime(1900, 1, 1, 0, 0, 0)
        timestamp1900 = convert_from_4_bytes(self.data)
        timestamp = ref1900 + datetime.timedelta(seconds=timestamp1900)
        return timestamp


class UserStateAVP(DiameterAVP, EnumeratedType):
    """Implementation of User-State AVP in Section 7.3.114 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The User-State AVP (AVP Code 1499) is of type Enumerated.
    """
    code = USER_STATE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
        USER_STATE_DETACHED,
        USER_STATE_ATTACHED_NOT_REACHABLE_FOR_PAGING,
        USER_STATE_ATTACHED_REACHABLE_FOR_PAGING,
        USER_STATE_CONNECTED_NOT_REACHABLE_FOR_PAGING,
        USER_STATE_CONNECTED_REACHABLE_FOR_PAGING,
        USER_STATE_RESERVED,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             UserStateAVP.code,
                             UserStateAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class MmeUserStateAVP(DiameterAVP, GroupedType):
    """Implementation of MME-User-State AVP in Section 7.3.112 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The MME-User-State AVP (AVP Code 1497) is of type Grouped.
    """
    code = MME_USER_STATE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "user_state": UserStateAVP,
    }
    optionals: dict[str,DiameterAVP]  = {}

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             MmeUserStateAVP.code,
                             MmeUserStateAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SgsnUserStateAVP(DiameterAVP, GroupedType):
    """Implementation of SGSN-User-State AVP in Section 7.3.113 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The SGSN-User-State AVP (AVP Code 1601) is of type Grouped.
    """
    code = SGSN_USER_STATE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
                    "user_state": UserStateAVP,
    }
    optionals: dict[str,DiameterAVP]  = {}

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             SgsnUserStateAVP.code,
                             SgsnUserStateAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EpsUserStateAVP(DiameterAVP, GroupedType):
    """Implementation of EPS-User-State AVP in Section 7.3.110 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The EPS-User-State AVP (AVP Code 1495) is of type Grouped.
    """
    code = EPS_USER_STATE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory: dict[str,DiameterAVP]  = {}
    optionals = {
        "mme_user_state": MmeUserStateAVP,
        "sgsn_user_state": SgsnUserStateAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             EpsUserStateAVP.code,
                             EpsUserStateAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class CellGlobalIdentityAVP(DiameterAVP, CellIdentityType):
    """Implementation of Cell-Global-Identity AVP in Section 7.3.119 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The E-UTRAN-Cell-Global-Identity AVP (AVP Code 1604) is of type OctetString.
    """
    code = CELL_GLOBAL_IDENTITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             CellGlobalIdentityAVP.code,
                             CellGlobalIdentityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        CellIdentityType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class TrackingAreaIdentityAVP(DiameterAVP, CellIdentityType):
    """Implementation Tracking-Area-Identity AVP in Section 7.3.118 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The Tracking-Area-Identity AVP (AVP Code 1603) is of type OctetString.
    """
    
    """Section 7.3.118"""
    code = TRACKING_AREA_IDENTITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             TrackingAreaIdentityAVP.code,
                             TrackingAreaIdentityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        CellIdentityType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EUtranCellGlobalIdentityAVP(DiameterAVP, CellIdentityType):
    """Implementation of E-UTRAN-Cell-Global-Identity AVP in Section 7.3.117 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The E-UTRAN-Cell-Global-Identity AVP (AVP Code 1602) is of type OctetString.
    """
    code = EUTRAN_CELL_GLOBAL_IDENTITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             EUtranCellGlobalIdentityAVP.code,
                             EUtranCellGlobalIdentityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        CellIdentityType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


    def decode(self) -> tuple[str,str,str,str]:
        vals = self.decode_mncmcc()
        return vals[0], vals[1], self.decode_tbcd(self.data[3:5]), self.decode_tbcd(self.data[5:])


class AgeOfLocationInformationAVP(DiameterAVP, Unsigned32Type):
    """Implementation of Age-Of-Location-Information AVP in Section 7.3.126 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The MME-Location-Information AVP (AVP Code 1611) is of type Unsigned32.
    """
    code = AGE_OF_LOCATION_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             AgeOfLocationInformationAVP.code,
                             AgeOfLocationInformationAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        Unsigned32Type.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


    def decode(self) -> int:
        intval = convert_from_4_bytes(self.data)
        return intval


class MmeLocationInformationAVP(DiameterAVP, GroupedType):
    """Implementation of MME-Location-Information AVP in Section 7.3.115 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The MME-Location-Information AVP (AVP Code 1600) is of type Grouped.
    """
    code = MME_LOCATION_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
    
    mandatory = {
            "e_utran_cell_global_identity": EUtranCellGlobalIdentityAVP,
            "tracking_area_identity": TrackingAreaIdentityAVP,
            "age_of_location_information": AgeOfLocationInformationAVP,
    }
    optionals: dict[str,DiameterAVP]  = {}

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             MmeLocationInformationAVP.code,
                             MmeLocationInformationAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class LocationAreaIdentityAVP(DiameterAVP, CellIdentityType):
    """Implementation of Location-Area-Identity AVP in Section 7.3.121 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The Location-Area-Identity AVP (AVP Code 1606) is of type OctetString.
    """
    code = LOCATION_AREA_IDENTITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
    
    def __init__(self, data):
        DiameterAVP.__init__(self,
                             LocationAreaIdentityAVP.code,
                             LocationAreaIdentityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        CellIdentityType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class ServiceAreaIdentityAVP(DiameterAVP, CellIdentityType):
    """Implementation of Service-Area-Identity AVP in Section 7.3.122 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The Service-Area-Identity AVP (AVP Code 1607) is of type OctetString.
    """
    code = SERVICE_AREA_IDENTITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
    
    def __init__(self, data):
        DiameterAVP.__init__(self,
                             ServiceAreaIdentityAVP.code,
                             ServiceAreaIdentityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        CellIdentityType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class RoutingAreaIdentityAVP(DiameterAVP, CellIdentityType):
    """Implementation of Routing-Area-Identity AVP in Section 7.3.120 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The Routing-Area-Identity AVP (AVP Code 1605) is of type OctetString.
    """
    code = ROUTING_AREA_IDENTITY_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
    
    def __init__(self, data):
        DiameterAVP.__init__(self,
                             RoutingAreaIdentityAVP.code,
                             RoutingAreaIdentityAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        CellIdentityType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class SgsnLocationInformationAVP(DiameterAVP, GroupedType):
    """Implementation of SGSN-Location-Information AVP in Section 7.3.116 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The SGSN-Location-Information AVP (AVP Code 1601) is of type Grouped.
    """
    """Section 7.3.116"""
    code = SGSN_LOCATION_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
    
    mandatory = {
            "cell_global_identity": CellGlobalIdentityAVP,
            "location_area_identity": LocationAreaIdentityAVP,
            "service_area_identity": ServiceAreaIdentityAVP,
            "routing_area_identity": RoutingAreaIdentityAVP,
            "age_of_location_information": AgeOfLocationInformationAVP,
    }
    optionals: dict[str,DiameterAVP]  = {}

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             SgsnLocationInformationAVP.code,
                             SgsnLocationInformationAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class EpsLocationInformationAVP(DiameterAVP, GroupedType):
    """Implementation of EPS-Location-Information AVP in Section 7.3.111 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The EPS-User-State AVP (AVP Code 1496) is of type Grouped.
    """
    code = EPS_LOCATION_INFORMATION_AVP_CODE
    vendor_id = VENDOR_ID_3GPP
    
    mandatory = {
            "mme_location_information": MmeLocationInformationAVP,
    }
    optionals = {
            "sgsn_location_information": SgsnLocationInformationAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             EpsLocationInformationAVP.code,
                             EpsLocationInformationAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class TimeZoneAVP(DiameterAVP, UTF8StringType):
    """Implementation of Time-Zone AVP in Section 7.3.163
    of ETSI TS 129 272 V15.10.0 (2020-01).

    The Time-Zone AVP (AVP Code 1642) is of type UTF8String.
    """
    code = TIME_ZONE_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, 
                             TimeZoneAVP.code,
                             TimeZoneAVP.vendor_id)
        DiameterAVP.set_mandatory_bit(self, True)
        UTF8StringType.__init__(self, data=data)


class DaylightSavingTimeAVP(DiameterAVP,EnumeratedType):
    """Implementation of Daylight-Saving-Type AVP in Section 7.3.164 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The Daylight-Saving-Type AVP (AVP Code 1650) is of type Enumerated.
    """
    code =  DAYLIGHT_SAVING_TIME_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    values = [
        DAYLIGHT_SAVING_TIME_NO_ADJUSTMENT,
        DAYLIGHT_SAVING_TIME_PLUS_ONE_HOUR_ADJUSTMENT,
        DAYLIGHT_SAVING_TIME_PLUS_TWO_HOURS_ADJUSTMENT,
    ]

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             DaylightSavingTimeAVP.code,
                             DaylightSavingTimeAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        EnumeratedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)


class LocalTimeZoneAVP(DiameterAVP, GroupedType):
    """Implementation of Local-Time-Zone AVP in Section 7.3.156 of 
    ETSI TS 129 272 V16.3.0 (2018-07).

    The EPS-User-State AVP (AVP Code 1649) is of type Grouped.
    """
    code = LOCAL_TIME_ZONE_AVP_CODE
    vendor_id = VENDOR_ID_3GPP

    mandatory = {
            "time_zone": TimeZoneAVP,
            "daylight_saving_time": DaylightSavingTimeAVP,
    }
    optionals = {
    }

    def __init__(self, data):
        DiameterAVP.__init__(self,
                             LocalTimeZoneAVP.code,
                             LocalTimeZoneAVP.vendor_id)
        DiameterAVP.set_vendor_id_bit(self, True)
        GroupedType.__init__(self, data=data, vendor_id=VENDOR_ID_3GPP)

