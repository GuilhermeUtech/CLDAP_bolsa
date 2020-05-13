#!/usr/bin/env python
import threading
import time
from datetime import datetime

data_e_hora_atuais = datetime.now()
highestCommitted = 0

class ThreadOne(threading.Thread):
    def run(self):
        while(1):
            data_e_hora_atuais = datetime.now()
            data_em_texto = '{}{}{}{}{}{}.0Z'.format(data_e_hora_atuais.year,data_e_hora_atuais.month,data_e_hora_atuais.day,data_e_hora_atuais.hour, data_e_hora_atuais.minute, data_e_hora_atuais.second)
            data_e_hora_atuais = data_em_texto
            print(data_e_hora_atuais)
            time.sleep(750) #15 minutos#
            
thingOne = ThreadOne()
thingOne.start()

dominioA = "test"
dominioB = "udesc"
dominioC = "br"

class Cldap():

    def __init__(self):
        self.payload = gerarPayload()

    
    def gerarPayload(self):
        highestCommitted = highestCommitted + 1
        if(highestCommitted > 10000):
            highestCommitted = 0
            return msg = """searchResEntry
                objectName: 
                attributes: unknown number of items
                    PartialAttributeList item currentTime
                        type: currentTime
                        vals: 1 item
                            AttributeValue: """+data_e_hora_atuais+"""
                    PartialAttributeList item subschemaSubentry
                        type: subschemaSubentry
                        vals: 1 item
                            AttributeValue: CN=Aggregate,CN=Schema,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item dsServiceName
                        type: dsServiceName
                        vals: 1 item
                            AttributeValue: CN=NTDS Settings,CN=DC-01-CCT,CN=Servers,CN=CCT,CN=Sites,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item namingContexts
                        type: namingContexts
                        vals: 5 items
                            AttributeValue: DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: CN=Schema,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: DC=DomainDnsZones,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: DC=ForestDnsZones,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item defaultNamingContext
                        type: defaultNamingContext
                        vals: 1 item
                            AttributeValue: DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item schemaNamingContext
                        type: schemaNamingContext
                        vals: 1 item
                            AttributeValue: CN=Schema,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item configurationNamingContext
                        type: configurationNamingContext
                        vals: 1 item
                            AttributeValue: CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item rootDomainNamingContext
                        type: rootDomainNamingContext
                        vals: 1 item
                            AttributeValue: DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item supportedControl
                        type: supportedControl
                        vals: unknown number of items
                            OID: 1.2.840.113556.1.4.319 (pagedResultsControl)
                            OID: 1.2.840.113556.1.4.801 (LDAP_SERVER_SD_FLAGS_OID)
                            OID: 1.2.840.113556.1.4.473 (sortKeyList)
                            OID: 1.2.840.113556.1.4.528 (LDAP_SERVER_NOTIFICATION_OID)
                            OID: 1.2.840.113556.1.4.417 (LDAP_SERVER_SHOW_DELETED_OID)
                            OID: 1.2.840.113556.1.4.619 (LDAP_SERVER_LAZY_COMMIT_OID)
                            OID: 1.2.840.113556.1.4.841 (dirsync)
                            OID: 1.2.840.113556.1.4.529 (LDAP_SERVER_EXTENDED_DN_OID)
                            OID: 1.2.840.113556.1.4.805 (LDAP_SERVER_TREE_DELETE_OID)
                            OID: 1.2.840.113556.1.4.521 (LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID)
                            OID: 1.2.840.113556.1.4.970 (None)
                            OID: 1.2.840.113556.1.4.1338 (LDAP_SERVER_VERIFY_NAME_OID)
                            OID: 1.2.840.113556.1.4.474 (sortResult)
                            OID: 1.2.840.113556.1.4.1339 (LDAP_SERVER_DOMAIN_SCOPE_OID)
                            OID: 1.2.840.113556.1.4.1340 (LDAP_SERVER_SEARCH_OPTIONS_OID)
                            OID: 1.2.840.113556.1.4.1413 (LDAP_SERVER_PERMISSIVE_MODIFY_OID)
                            OID: 2.16.840.1.113730.3.4.9 (VLV Request LDAPv3 control)
                            OID: 2.16.840.1.113730.3.4.10 (VLV Response LDAPv3 control)
                            OID: 1.2.840.113556.1.4.1504 (LDAP_SERVER_ASQ_OID)
                            OID: 1.2.840.113556.1.4.1852 (LDAP_SERVER_QUOTA_CONTROL_OID)
                            OID: 1.2.840.113556.1.4.802 (LDAP_SERVER_RANGE_OPTION_OID)
                            OID: 1.2.840.113556.1.4.1907 (LDAP_SERVER_SHUTDOWN_NOTIFY_OID)
                            OID: 1.2.840.113556.1.4.1948 (LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID)
                            OID: 1.2.840.113556.1.4.1974 (ISO assigned OIDs, USA.113556.1.4.1974)
                            OID: 1.2.840.113556.1.4.1341 (ISO assigned OIDs, USA.113556.1.4.1341)
                    OID: 1.2.840.113556.1.4.2026 (ISO assigned OIDs, USA.113556.1.4.2026)
                            OID: 1.2.840.113556.1.4.2064 (ISO assigned OIDs, USA.113556.1.4.2064)
                            OID: 1.2.840.113556.1.4.2065 (ISO assigned OIDs, USA.113556.1.4.2065)
                            OID: 1.2.840.113556.1.4.2066 (ISO assigned OIDs, USA.113556.1.4.2066)
                            OID: 1.2.840.113556.1.4.2090 (ISO assigned OIDs, USA.113556.1.4.2090)
                            OID: 1.2.840.113556.1.4.2205 (ISO assigned OIDs, USA.113556.1.4.2205)
                            OID: 1.2.840.113556.1.4.2204 (ISO assigned OIDs, USA.113556.1.4.2204)
                            OID: 1.2.840.113556.1.4.2206 (ISO assigned OIDs, USA.113556.1.4.2206)
                            OID: 1.2.840.113556.1.4.2211 (ISO assigned OIDs, USA.113556.1.4.2211)
                            OID: 1.2.840.113556.1.4.2239 (ISO assigned OIDs, USA.113556.1.4.2239)
                            OID: 1.2.840.113556.1.4.2255 (ISO assigned OIDs, USA.113556.1.4.2255)
                            OID: 1.2.840.113556.1.4.2256 (ISO assigned OIDs, USA.113556.1.4.2256)
                        PartialAttributeList item supportedLDAPVersion
                            type: supportedLDAPVersion
                            vals: 2 items
                                AttributeValue: 3
                                AttributeValue: 2
                        PartialAttributeList item supportedLDAPPolicies
                            type: supportedLDAPPolicies
                            vals: 19 items
                                AttributeValue: MaxPoolThreads
                                AttributeValue: MaxPercentDirSyncRequests
                                AttributeValue: MaxDatagramRecv
                                AttributeValue: MaxReceiveBuffer
                                AttributeValue: InitRecvTimeout
                                AttributeValue: MaxConnections
                                AttributeValue: MaxConnIdleTime
                                AttributeValue: MaxPageSize
                                AttributeValue: MaxBatchReturnMessages
                                AttributeValue: MaxQueryDuration
                                AttributeValue: MaxTempTableSize
                                AttributeValue: MaxResultSetSize
                                AttributeValue: MinResultSets
                                AttributeValue: MaxResultSetsPerConn
                                AttributeValue: MaxNotificationPerConn
                                AttributeValue: MaxValRange
                                AttributeValue: MaxValRangeTransitive
                                AttributeValue: ThreadMemoryLimit
                                AttributeValue: SystemMemoryLimitPercent
                        PartialAttributeList item highestCommittedUSN
                            type: highestCommittedUSN
                            vals: 1 item
                                AttributeValue: """+highestCommitted+"""
                        PartialAttributeList item supportedSASLMechanisms
                            type: supportedSASLMechanisms
                            vals: 4 items
                                AttributeValue: GSSAPI
                                AttributeValue: GSS-SPNEGO
                                AttributeValue: EXTERNAL
                                AttributeValue: DIGEST-MD5
                        PartialAttributeList item dnsHostName
                            type: dnsHostName
                            vals: 1 item
                                AttributeValue: TESTE-01-TESTE.corp.udesc.br
                        PartialAttributeList item ldapServiceName
                            type: ldapServiceName
                            vals: 1 item
                                AttributeValue: corp.udesc.br:teste-01-teste$@CORP.UDESC.BR
                        PartialAttributeList item serverName
                            type: serverName
                            vals: 1 item
                                AttributeValue: CN=TESTE-01-TESTE,CN=Servers,CN=CCT,CN=Sites,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB""",DC="""+dominioC+"""
                        PartialAttributeList item supportedCapabilities
                            type: supportedCapabilities
                            vals: 6 items
                                OID: 1.2.840.113556.1.4.800 (LDAP_CAP_ACTIVE_DIRECTORY_OID)
                                OID: 1.2.840.113556.1.4.1670 (LDAP_CAP_ACTIVE_DIRECTORY_V51_OID)
                                OID: 1.2.840.113556.1.4.1791 (LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID)
                                OID: 1.2.840.113556.1.4.1935 (ISO assigned OIDs, USA.113556.1.4.1935)
                                OID: 1.2.840.113556.1.4.2080 (ISO assigned OIDs, USA.113556.1.4.2080)
                                OID: 1.2.840.113556.1.4.2237 (ISO assigned OIDs, USA.113556.1.4.2237)
                        PartialAttributeList item isSynchronized
                            type: isSynchronized
                            vals: 1 item
                                AttributeValue: TRUE
                        PartialAttributeList item isGlobalCatalogReady
                            type: isGlobalCatalogReady
                            vals: 1 item
                                AttributeValue: TRUE
                        PartialAttributeList item domainFunctionality
                            type: domainFunctionality
                            vals: 1 item
                                AttributeValue: 6
                        PartialAttributeList item forestFunctionality
                            type: forestFunctionality
                            vals: 1 item
                                AttributeValue: 6
                        PartialAttributeList item domainControllerFunctionality
                            type: domainControllerFunctionality
                            vals: 1 item
                                AttributeValue: 6""".encode('ascii')
        else:
            return msg = """searchResEntry
                objectName: 
                attributes: unknown number of items
                    PartialAttributeList item currentTime
                        type: currentTime
                        vals: 1 item
                            AttributeValue: """+data_e_hora_atuais+"""
                    PartialAttributeList item subschemaSubentry
                        type: subschemaSubentry
                        vals: 1 item
                            AttributeValue: CN=Aggregate,CN=Schema,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item dsServiceName
                        type: dsServiceName
                        vals: 1 item
                            AttributeValue: CN=NTDS Settings,CN=DC-01-CCT,CN=Servers,CN=CCT,CN=Sites,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item namingContexts
                        type: namingContexts
                        vals: 5 items
                            AttributeValue: DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: CN=Schema,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: DC=DomainDnsZones,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                            AttributeValue: DC=ForestDnsZones,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item defaultNamingContext
                        type: defaultNamingContext
                        vals: 1 item
                            AttributeValue: DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item schemaNamingContext
                        type: schemaNamingContext
                        vals: 1 item
                            AttributeValue: CN=Schema,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item configurationNamingContext
                        type: configurationNamingContext
                        vals: 1 item
                            AttributeValue: CN=Configuration,DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item rootDomainNamingContext
                        type: rootDomainNamingContext
                        vals: 1 item
                            AttributeValue: DC="""+dominioA+""",DC="""+dominioB+""",DC="""+dominioC+"""
                    PartialAttributeList item supportedControl
                        type: supportedControl
                        vals: unknown number of items
                            OID: 1.2.840.113556.1.4.319 (pagedResultsControl)
                            OID: 1.2.840.113556.1.4.801 (LDAP_SERVER_SD_FLAGS_OID)
                            OID: 1.2.840.113556.1.4.473 (sortKeyList)
                            OID: 1.2.840.113556.1.4.528 (LDAP_SERVER_NOTIFICATION_OID)
                            OID: 1.2.840.113556.1.4.417 (LDAP_SERVER_SHOW_DELETED_OID)
                            OID: 1.2.840.113556.1.4.619 (LDAP_SERVER_LAZY_COMMIT_OID)
                            OID: 1.2.840.113556.1.4.841 (dirsync)
                            OID: 1.2.840.113556.1.4.529 (LDAP_SERVER_EXTENDED_DN_OID)
                            OID: 1.2.840.113556.1.4.805 (LDAP_SERVER_TREE_DELETE_OID)
                            OID: 1.2.840.113556.1.4.521 (LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID)
                            OID: 1.2.840.113556.1.4.970 (None)
                            OID: 1.2.840.113556.1.4.1338 (LDAP_SERVER_VERIFY_NAME_OID)
                            OID: 1.2.840.113556.1.4.474 (sortResult)
                            OID: 1.2.840.113556.1.4.1339 (LDAP_SERVER_DOMAIN_SCOPE_OID)
                            OID: 1.2.840.113556.1.4.1340 (LDAP_SERVER_SEARCH_OPTIONS_OID)
                            OID: 1.2.840.113556.1.4.1413 (LDAP_SERVER_PERMISSIVE_MODIFY_OID)
                            OID: 2.16.840.1.113730.3.4.9 (VLV Request LDAPv3 control)
                            OID: 2.16.840.1.113730.3.4.10 (VLV Response LDAPv3 control)
                            OID: 1.2.840.113556.1.4.1504 (LDAP_SERVER_ASQ_OID)
                            OID: 1.2.840.113556.1.4.1852 (LDAP_SERVER_QUOTA_CONTROL_OID)
                            OID: 1.2.840.113556.1.4.802 (LDAP_SERVER_RANGE_OPTION_OID)
                            OID: 1.2.840.113556.1.4.1907 (LDAP_SERVER_SHUTDOWN_NOTIFY_OID)
                            OID: 1.2.840.113556.1.4.1948 (LDAP_SERVER_RANGE_RETRIEVAL_NOERR_OID)
                            OID: 1.2.840.113556.1.4.1974 (ISO assigned OIDs, USA.113556.1.4.1974)
                            OID: 1.2.840.113556.1.4.1341 (ISO assigned OIDs, USA.113556.1.4.1341)
                    OID: 1.2.840.113556.1.4.2026 (ISO assigned OIDs, USA.113556.1.4.2026)
                            OID: 1.2.840.113556.1.4.2064 (ISO assigned OIDs, USA.113556.1.4.2064)
                            OID: 1.2.840.113556.1.4.2065 (ISO assigned OIDs, USA.113556.1.4.2065)
                            OID: 1.2.840.113556.1.4.2066 (ISO assigned OIDs, USA.113556.1.4.2066)
                            OID: 1.2.840.113556.1.4.2090 (ISO assigned OIDs, USA.113556.1.4.2090)
                            OID: 1.2.840.113556.1.4.2205 (ISO assigned OIDs, USA.113556.1.4.2205)
                            OID: 1.2.840.113556.1.4.2204 (ISO assigned OIDs, USA.113556.1.4.2204)
                            OID: 1.2.840.113556.1.4.2206 (ISO assigned OIDs, USA.113556.1.4.2206)
                            OID: 1.2.840.113556.1.4.2211 (ISO assigned OIDs, USA.113556.1.4.2211)
                            OID: 1.2.840.113556.1.4.2239 (ISO assigned OIDs, USA.113556.1.4.2239)
                            OID: 1.2.840.113556.1.4.2255 (ISO assigned OIDs, USA.113556.1.4.2255)
                            OID: 1.2.840.113556.1.4.2256 (ISO assigned OIDs, USA.113556.1.4.2256)
                        PartialAttributeList item supportedLDAPVersion
                            type: supportedLDAPVersion
                            vals: 2 items
                                AttributeValue: 3
                                AttributeValue: 2
                        PartialAttributeList item supportedLDAPPolicies
                            type: supportedLDAPPolicies
                            vals: 19 items
                                AttributeValue: MaxPoolThreads
                                AttributeValue: MaxPercentDirSyncRequests
                                AttributeValue: MaxDatagramRecv
                                AttributeValue: MaxReceiveBuffer
                                AttributeValue: InitRecvTimeout
                                AttributeValue: MaxConnections
                                AttributeValue: MaxConnIdleTime
                                AttributeValue: MaxPageSize
                                AttributeValue: MaxBatchReturnMessages
                                AttributeValue: MaxQueryDuration
                                AttributeValue: MaxTempTableSize
                                AttributeValue: MaxResultSetSize
                                AttributeValue: MinResultSets
                                AttributeValue: MaxResultSetsPerConn
                                AttributeValue: MaxNotificationPerConn
                                AttributeValue: MaxValRange
                                AttributeValue: MaxValRangeTransitive
                                AttributeValue: ThreadMemoryLimit
                                AttributeValue: SystemMemoryLimitPercent
                        PartialAttributeList item highestCommittedUSN
                            type: highestCommittedUSN
                            vals: 1 item
                                AttributeValue: """+highestCommitted+"""
                        PartialAttributeList item supportedSASLMechanisms
                            type: supportedSASLMechanisms
                            vals: 4 items
                                AttributeValue: GSSAPI
                                AttributeValue: GSS-SPNEGO
                                AttributeValue: EXTERNAL
                                AttributeValue: DIGEST-MD5
                        PartialAttributeList item dnsHostName
                            type: dnsHostName
                            vals: 1 item
                                AttributeValue: TESTE-01-TESTE.corp.udesc.br
                        PartialAttributeList item ldapServiceName
                            type: ldapServiceName
                            vals: 1 item
                                AttributeValue: corp.udesc.br:teste-01-teste$@CORP.UDESC.BR
                        PartialAttributeList item serverName
                            type: serverName
                            vals: 1 item
                                AttributeValue: CN=TESTE-01-TESTE,CN=Servers,CN=CCT,CN=Sites,CN=Configuration,DC="""+dominioA+""",DC="""+dominioB""",DC="""+dominioC+"""
                        PartialAttributeList item supportedCapabilities
                            type: supportedCapabilities
                            vals: 6 items
                                OID: 1.2.840.113556.1.4.800 (LDAP_CAP_ACTIVE_DIRECTORY_OID)
                                OID: 1.2.840.113556.1.4.1670 (LDAP_CAP_ACTIVE_DIRECTORY_V51_OID)
                                OID: 1.2.840.113556.1.4.1791 (LDAP_CAP_ACTIVE_DIRECTORY_LDAP_INTEG_OID)
                                OID: 1.2.840.113556.1.4.1935 (ISO assigned OIDs, USA.113556.1.4.1935)
                                OID: 1.2.840.113556.1.4.2080 (ISO assigned OIDs, USA.113556.1.4.2080)
                                OID: 1.2.840.113556.1.4.2237 (ISO assigned OIDs, USA.113556.1.4.2237)
                        PartialAttributeList item isSynchronized
                            type: isSynchronized
                            vals: 1 item
                                AttributeValue: TRUE
                        PartialAttributeList item isGlobalCatalogReady
                            type: isGlobalCatalogReady
                            vals: 1 item
                                AttributeValue: TRUE
                        PartialAttributeList item domainFunctionality
                            type: domainFunctionality
                            vals: 1 item
                                AttributeValue: 6
                        PartialAttributeList item forestFunctionality
                            type: forestFunctionality
                            vals: 1 item
                                AttributeValue: 6
                        PartialAttributeList item domainControllerFunctionality
                            type: domainControllerFunctionality
                            vals: 1 item
                                AttributeValue: 6""".encode('ascii')

                    

    
    
    async def render_get(self, request):
        msg = aiocoap.Message(code=aiocoap.CONTENT, payload=self.payload)
        msg.opt.content_format = 40 # application/link-format
        return msg
    
    def run(self):

        if(self.payload in self.geststatus):
            return self.response
        else:
            return self.error

def main():
   
if __name__ == "__main__":
    main()