from ..._internal_utils import convert_to_4_bytes


#: Diameter AVPs
LOW_BALANCE_INDICATION_AVP_CODE = convert_to_4_bytes(2020)
REMAINING_BALANCE_AVP_CODE = convert_to_4_bytes(2021)
LCS_FORMAT_INDICATOR_AVP_CODE = convert_to_4_bytes(1237)
LCS_NAME_STRING_AVP_CODE = convert_to_4_bytes(1238)
LCS_REQUESTED_ID_STIRNG_AVP_CODE = convert_to_4_bytes(1240)
LCS_CLIENT_TYPE_AVP_CODE = convert_to_4_bytes(1241)
LOCATION_ESTIMATE_AVP_CODE = convert_to_4_bytes(1242)

#: List of Low-Balance-Indication AVP values.
#: For more information, please refer to Section 7.2.97 of
#: ETSI TS 132 299 V14.3.0 (2017-04).
LOW_BALANCE_INDICATION_NOT_APPLICABLE = convert_to_4_bytes(0)
LOW_BALANCE_INDICATION_YES = convert_to_4_bytes(1)

#: List of LCS-Format-Indicator AVP values.
#: For more information, please refer to Section 7.2.88 of
#: ETSI TS 132 299 V15.3.0 (2018-06).
LCS_FORMAT_INDICATOR_LOGICAL_NAME = convert_to_4_bytes(0)
LCS_FORMAT_INDICATOR_EMAIL_ADDRESS = convert_to_4_bytes(1)
LCS_FORMAT_INDICATOR_MSISDN = convert_to_4_bytes(2)
LCS_FORMAT_INDICATOR_URL = convert_to_4_bytes(3)
LCS_FORMAT_INDICATOR_SIP_URL = convert_to_4_bytes(4)

#: List of LCS-Client-Type AVP values.
#: For more information, please refer to Section 7.2.86 of
#: ETSI TS 132 299 V15.3.0 (2018-06).
LCS_CLIENT_TYPE_EMERGENCY_SERVICES = convert_to_4_bytes(0)
LCS_CLIENT_TYPE_VALUE_ADDED_SERVICES = convert_to_4_bytes(1)
LCS_CLIENT_TYPE_PLMN_OPERATOR_SERVICES = convert_to_4_bytes(2)
LCS_CLIENT_TYPE_LAWFUL_INTERCEPT_SERVICES = convert_to_4_bytes(3)
