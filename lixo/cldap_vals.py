from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful
from pyasn1.codec.ber.encoder import encode
from pyasn1.debug import hexdump

class SearchResultEntry(univ.Sequence):
    pass


SearchResultEntry.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 4))

SearchResultEntry.componentType = namedtype.NamedTypes(
    namedtype.NamedType('objectName', univ.OctetString()),

    namedtype.NamedType('attributes', univ.SequenceOf(componentType=univ.Sequence(componentType=namedtype.NamedTypes(
        namedtype.NamedType('type', univ.OctetString()),
        namedtype.NamedType('vals', univ.SetOf(componentType=univ.OctetString()))
    ))
    ))
)

objeto = SearchResultEntry()

#Inserindo todos os valores para testar agora.
objeto['objectName'] = "" 

#currentTime
objeto['attributes']['a'].setComponentByName('type', 'currentTime')
objeto['attributes']['a']['vals'].extend(['20191021194909.0Z'])

#subschemaSubentry
objeto['attributes']['b'].setComponentByName('type', 'subschemaSubentry')
objeto['attributes']['b']['vals'].extend(['CN=Aggregate,CN=Schema,CN=Configuration,DC=teste,DC=udesc,DC=br'])

#dsServiceName
objeto['attributes']['c'].setComponentByName('type', 'dsServiceName')
objeto['attributes']['c']['vals'].extend(['CN=NTDS Settings,CN=DC-01-CCT,CN=Servers,CN=CCT,CN=Sites,CN=Configuration,DC=teste,DC=udesc,DC=br'])

#namingContexts
objeto['attributes']['d'].setComponentByName('type', 'namingContexts')
objeto['attributes']['d']['vals'].extend(['DC=teste,DC=udesc,DC=br','CN=Configuration,DC=teste,DC=udesc,DC=br','CN=Schema,CN=Configuration,DC=teste,DC=udesc,DC=br','DC=DomainDnsZones,DC=teste,DC=udesc,DC=br','DC=ForestDnsZones,DC=teste,DC=udesc,DC=br'])

#defaultNamingContext
objeto['attributes']['e'].setComponentByName('type', 'defaultNamingContext')
objeto['attributes']['e']['vals'].extend(['DC=teste,DC=udesc,DC=br'])

#schemaNamingContext
objeto['attributes']['f'].setComponentByName('type', 'schemaNamingContext')
objeto['attributes']['f']['vals'].extend(['CN=Schema,CN=Configuration,DC=teste,DC=udesc,DC=br'])

#configurationNamingContext
objeto['attributes']['g'].setComponentByName('type', 'configurationNamingContex')
objeto['attributes']['g']['vals'].extend(['CN=Configuration,DC=teste,DC=udesc,DC=br'])

#rootDomainNamingContext
objeto['attributes']['h'].setComponentByName('type', 'rootDomainNamingContext')
objeto['attributes']['h']['vals'].extend(['DC=teste,DC=udesc,DC=br'])

#supportedLDAPVersion
objeto['attributes']['i'].setComponentByName('type', 'supportedLDAPVersion')
objeto['attributes']['i']['vals'].extend(['3', '2'])

#supportedLDAPPolicies
objeto['attributes']['j'].setComponentByName('type', 'supportedLDAPPolicies')
objeto['attributes']['j']['vals'].extend(['MaxPoolThreads','MaxPercentDirSyncRequests', 'MaxDatagramRecv', 'MaxReceiveBuffer', 'InitRecvTimeout', 'MaxConnections', 'MaxConnIdleTime', 'MaxPageSize', 'MaxBatchReturnMessages', 'MaxQueryDuration', 'MaxTempTableSize', 'MaxResultSetSize', 'MinResultSets', 'MaxResultSetsPerConn', 'MaxNotificationPerConn', 'MaxValRange', 'MaxValRangeTransitive', 'ThreadMemoryLimit', 'SystemMemoryLimitPercent'])

#highestCommittedUSN
objeto['attributes']['k'].setComponentByName('type', 'highestCommittedUSN')
objeto['attributes']['k']['vals'].extend(['2020'])

#supportedSASLMechanisms
objeto['attributes']['l'].setComponentByName('type', 'supportedSASLMechanisms')
objeto['attributes']['l']['vals'].extend(['GSSAPI', 'GSS-SPNEGO', 'EXTERNAL', 'DIGEST-MD5'])

#dnsHostName
objeto['attributes']['m'].setComponentByName('type', 'dnsHostName')
objeto['attributes']['m']['vals'].extend(['TESTE-01-TESTE.corp.udesc.br'])

#ldapServiceName
objeto['attributes']['n'].setComponentByName('type', 'ldapServiceName')
objeto['attributes']['n']['vals'].extend(['corp.udesc.br:teste-01-teste$@CORP.UDESC.BR'])

#serverName
objeto['attributes']['o'].setComponentByName('type', 'serverName')
objeto['attributes']['o']['vals'].extend(['CN=TESTE-01TESTE,CN=Servers,CN=CCT,CN=Sites,CN=Configuration,DC=teste,DC=udesc,DC=br'])

#isSynchronized
objeto['attributes']['p'].setComponentByName('type', 'isSynchronized')
objeto['attributes']['p']['vals'].extend(['TRUE'])

#isGlobalCatalogReady
objeto['attributes']['q'].setComponentByName('type', 'isGlobalCatalogReady')
objeto['attributes']['q']['vals'].extend(['TRUE'])

#domainFunctionality
objeto['attributes']['r'].setComponentByName('type', 'domainFunctionality')
objeto['attributes']['r']['vals'].extend(['6'])

#forestFunctionality
objeto['attributes']['s'].setComponentByName('type', 'forestFunctionality')
objeto['attributes']['s']['vals'].extend(['6'])

#domainControllerFunctionality
objeto['attributes']['t'].setComponentByName('type', 'domainControllerFunctionality')
objeto['attributes']['t']['vals'].extend(['6'])


print(objeto['objectName'])
print(objeto['attributes']['a'])
print(objeto['attributes']['b'])
print(objeto['attributes']['c'])
print(objeto['attributes']['d'])
print(objeto['attributes']['e'])
print(objeto['attributes']['f'])
print(objeto['attributes']['g'])
print(objeto['attributes']['h'])
print(objeto['attributes']['i'])
print(objeto['attributes']['j'])
print(objeto['attributes']['k'])
print(objeto['attributes']['l'])
print(objeto['attributes']['m'])
print(objeto['attributes']['n'])
print(objeto['attributes']['o'])
print(objeto['attributes']['p'])
print(objeto['attributes']['q'])
print(objeto['attributes']['r'])
print(objeto['attributes']['s'])
print(objeto['attributes']['t'])

f = open("saida.txt", "w")

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']

for i in range(0,19):
    if i == 0:
        sub = encode(objeto['objectName'])
        print(hexdump(sub))
        f.write(hexdump(sub))
    
    sub = encode(objeto['attributes'][a[i]])
    print(hexdump(sub))
    f.write(hexdump(sub))
