# -*- coding: utf-8 -*-
"""
    bromelia.proxy
    ~~~~~~~~~~~~~~

    This module contains the BaseMessages class necessary to instantiate
    the DiameterAssociation class. It allows define the set of base messages
    of Diameter protocol which will be used in a specific connection. Besides
    that, it allows to customize the base messages content as per RFC 6733.

    :copyright: (c) 2020-present Henrique Marques Ribeiro.
    :license: MIT, see LICENSE for more details.
"""

from .constants import *
from .avps import AuthApplicationIdAVP
from .avps import VendorIdAVP
from .avps import VendorSpecificApplicationIdAVP
from .messages import CapabilitiesExchangeAnswer
from .messages import CapabilitiesExchangeRequest
from .messages import DeviceWatchdogAnswer
from .messages import DeviceWatchdogRequest
from .messages import DisconnectPeerAnswer
from .messages import DisconnectPeerRequest

class BaseMessages:
    def __init__(self, cer, cea, dwr, dwa, dpr, dpa):
        self.cer = cer
        self.cea = cea
        self.dwr = dwr
        self.dwa = dwa
        self.dpr = dpr
        self.dpa = dpa


class DiameterBaseProxy:
    def __init__(self, connection):
        self.connection = connection


    def get_default_messages(self):
        return BaseMessages(cer=DiameterBaseProxy.load_cer(self.connection),
                            cea=DiameterBaseProxy.load_cea(self.connection), 
                            dwr=DiameterBaseProxy.load_dwr(self.connection), 
                            dwa=DiameterBaseProxy.load_dwa(self.connection), 
                            dpr=DiameterBaseProxy.load_dpr(self.connection), 
                            dpa=DiameterBaseProxy.load_dpa(self.connection))


    def get_custom_messages(self, msgs):
        base = dict()
        for msg in msgs:
            if isinstance(msg, CapabilitiesExchangeRequest):
                base.update({"cer": msg})
            elif isinstance(msg, CapabilitiesExchangeAnswer):
                base.update({"cea": msg})
            elif isinstance(msg, DeviceWatchdogRequest):
                base.update({"dwr": msg})
            elif isinstance(msg, DeviceWatchdogAnswer):
                base.update({"dwa": msg})
            elif isinstance(msg, DisconnectPeerRequest):
                base.update({"dpr": msg})
            elif isinstance(msg, DisconnectPeerAnswer):
                base.update({"dpa": msg})

        for key in base.keys():
            if key == "cer":
                base.update({"cer": DiameterBaseProxy.load_cer(self.connection)})
            elif key == "cea":
                base.update({"cea": DiameterBaseProxy.load_cea(self.connection)})
            elif key == "dwr":
                base.update({"dwr": DiameterBaseProxy.load_dwr(self.connection)})
            elif key == "dwa":
                base.update({"dwa": DiameterBaseProxy.load_dwa(self.connection)})
            elif key == "dpr":
                base.update({"dpr": DiameterBaseProxy.load_dpr(self.connection)})
            elif key == "dpa":
                base.update({"dpa": DiameterBaseProxy.load_dpa(self.connection)})
        
        return BaseMessages(**base)


    @staticmethod
    def load_cer(connection):
        if isinstance(connection.application_ids, dict):
            application = connection.application_ids
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
                    "auth_application_id": application["app_id"]
            }
            cer = CapabilitiesExchangeRequest(**avps)

        elif isinstance(connection.application_ids, list):
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
            }
            cer = CapabilitiesExchangeRequest(**avps)

            applications = connection.application_ids
            for application in applications:
                vendor_id_avp = VendorIdAVP(application["vendor_id"])
                auth_app_id_avp = AuthApplicationIdAVP(application["app_id"])

                avp = VendorSpecificApplicationIdAVP([
                                                        vendor_id_avp, 
                                                        auth_app_id_avp
                ])

                cer.append(avp)

        return cer

    @staticmethod
    def load_cea(connection):
        if isinstance(connection.application_ids, dict):
            application = connection.application_ids
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
                    "auth_application_id": application["app_id"],
            }
            cea = CapabilitiesExchangeAnswer(**avps)

        elif isinstance(connection.application_ids, list):
            avps = {
                    "origin_host": connection.local_node.host_name,
                    "origin_realm": connection.local_node.realm,
                    "host_ip_address": connection.local_node.ip_address,
                    "vendor_id": VENDOR_ID_DEFAULT,
            }
            cea = CapabilitiesExchangeAnswer(**avps)

            applications = connection.application_ids
            for application in applications:
                vendor_id_avp = VendorIdAVP(application["vendor_id"])
                auth_app_id_avp = AuthApplicationIdAVP(application["app_id"])

                avp = VendorSpecificApplicationIdAVP([
                                                        vendor_id_avp, 
                                                        auth_app_id_avp
                ])

                cea.append(avp)

        return cea


    @staticmethod
    def load_dwr(connection):
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }            
        return DeviceWatchdogRequest(**avps)


    @staticmethod
    def load_dwa(connection):
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }
        return DeviceWatchdogAnswer(**avps)


    @staticmethod
    def load_dpr(connection):
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }            
        return DisconnectPeerRequest(**avps)


    @staticmethod
    def load_dpa(connection):
        avps = {
                "origin_host": connection.local_node.host_name,
                "origin_realm": connection.local_node.realm,
        }
        return DisconnectPeerAnswer(**avps)
