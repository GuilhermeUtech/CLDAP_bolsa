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
objeto['attributes']['a'].setComponentByName('type', '143 165 162 162 145 156 164 124 151 155 145')
objeto['attributes']['a']['vals'].extend(['062 060 062 060 064 061 060 061 061 061 063 060 056 060 132'])

#subschemaSubentry
objeto['attributes']['b'].setComponentByName('type', '163 165 142 163 143 150 145 155 141 123 165 142 145 156 164 162 171')
objeto['attributes']['b']['vals'].extend(['103 116 075 101 147 147 162 145 147 141 164 145 054 103 116 075 123 143 150 145 155 141 054 103 116 075 103 157 156 146 151 147 165 162 141 164 151 157 156 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162'])

#dsServiceName
objeto['attributes']['c'].setComponentByName('type', '144 163 123 145 162 166 151 143 145 116 141 155 145')
objeto['attributes']['c']['vals'].extend(['103 116 075 116 124 104 123 040 123 145 164 164 151 156 147 163 054 103 116 075 104 103 055 060 061 055 103 103 124 054 103 116 075 123 145 162 166 145 162 163 054 103 116 075 103 103 124 054 103 116 075 123 151 164 145 163 054 103 116 075 103 157 156 146 151 147 165 162 141 164 151 157 156 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162 015 012'])

#namingContexts
objeto['attributes']['d'].setComponentByName('type', '156 141 155 151 156 147 103 157 156 164 145 170 164 163')
objeto['attributes']['d']['vals'].extend(['104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162', '103 116 075 103 157 156 146 151 147 165 162 141 164 151 157 156 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162', '103 116 075 123 143 150 145 155 141 054 103 116 075 103 157 156 146 151 147 165 162 141 164 151 157 156 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162', '104 103 075 104 157 155 141 151 156 104 156 163 132 157 156 145 163 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162', '104 103 075 106 157 162 145 163 164 104 156 163 132 157 156 145 163 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162 015 012'])


#defaultNamingContext
objeto['attributes']['e'].setComponentByName('type', '144 145 146 141 165 154 164 116 141 155 151 156 147 103 157 156 164 145 170 164')
objeto['attributes']['e']['vals'].extend(['104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162'])

#schemaNamingContext
objeto['attributes']['f'].setComponentByName('type', '163 143 150 145 155 141 116 141 155 151 156 147 103 157 156 164 145 170 164')
objeto['attributes']['f']['vals'].extend(['103 116 075 123 143 150 145 155 141 054 103 116 075 103 157 156 146 151 147 165 162 141 164 151 157 156 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162'])

#configurationNamingContext
objeto['attributes']['g'].setComponentByName('type', '143 157 156 146 151 147 165 162 141 164 151 157 156 116 141 155 151 156 147 103 157 156 164 145 170 164')
objeto['attributes']['g']['vals'].extend(['103 116 075 103 157 156 146 151 147 165 162 141 164 151 157 156 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162'])

#rootDomainNamingContext
objeto['attributes']['h'].setComponentByName('type', '162 157 157 164 104 157 155 141 151 156 116 141 155 151 156 147 103 157 156 164 145 170 164')
objeto['attributes']['h']['vals'].extend(['162 157 157 164 104 157 155 141 151 156 116 141 155 151 156 147 103 157 156 164 145 170 164'])

#supportedLDAPVersion
objeto['attributes']['i'].setComponentByName('type', '163 165 160 160 157 162 164 145 144 114 104 101 120 126 145 162 163 151 157 156')
objeto['attributes']['i']['vals'].extend(['063', '062'])

#supportedLDAPPolicies
objeto['attributes']['j'].setComponentByName('type', '163 165 160 160 157 162 164 145 144 114 104 101 120 120 157 154 151 143 151 145 163')
objeto['attributes']['j']['vals'].extend(['115 141 170 120 157 157 154 124 150 162 145 141 144 163', '115 141 170 120 145 162 143 145 156 164 104 151 162 123 171 156 143 122 145 161 165 145 163 164 163', '115 141 170 104 141 164 141 147 162 141 155 122 145 143 166', '115 141 170 122 145 143 145 151 166 145 102 165 146 146 145 162', '111 156 151 164 122 145 143 166 124 151 155 145 157 165 164', '115 141 170 103 157 156 156 145 143 164 151 157 156 163', '115 141 170 103 157 156 156 111 144 154 145 124 151 155 145', '115 141 170 120 141 147 145 123 151 172 145', '115 141 170 102 141 164 143 150 122 145 164 165 162 156 115 145 163 163 141 147 145 163', '115 141 170 121 165 145 162 171 104 165 162 141 164 151 157 156', '115 141 170 124 145 155 160 124 141 142 154 145 123 151 172 145', '115 141 170 122 145 163 165 154 164 123 145 164 123 151 172 145', '115 151 156 122 145 163 165 154 164 123 145 164 163', '115 141 170 122 145 163 165 154 164 123 145 164 163 120 145 162 103 157 156 156', '115 141 170 116 157 164 151 146 151 143 141 164 151 157 156 120 145 162 103 157 156 156', '115 141 170 126 141 154 122 141 156 147 145', '115 141 170 126 141 154 122 141 156 147 145 124 162 141 156 163 151 164 151 166 145', '124 150 162 145 141 144 115 145 155 157 162 171 114 151 155 151 164', '123 171 163 164 145 155 115 145 155 157 162 171 114 151 155 151 164 120 145 162 143 145 156 164'])

#highestCommittedUSN
objeto['attributes']['k'].setComponentByName('type', '150 151 147 150 145 163 164 103 157 155 155 151 164 164 145 144 125 123 116')
objeto['attributes']['k']['vals'].extend(['062 060 062 060'])

#supportedSASLMechanisms
objeto['attributes']['l'].setComponentByName('type', '163 165 160 160 157 162 164 145 144 123 101 123 114 115 145 143 150 141 156 151 163 155 163')
objeto['attributes']['l']['vals'].extend(['107 123 123 101 120 111', '107 123 123 055 123 120 116 105 107 117', '105 130 124 105 122 116 101 114', '104 111 107 105 123 124 055 115 104 065'])

#dnsHostName
objeto['attributes']['m'].setComponentByName('type', '144 156 163 110 157 163 164 116 141 155 145')
objeto['attributes']['m']['vals'].extend(['124 105 123 124 105 055 060 061 055 124 105 123 124 105 056 143 157 162 160 056 165 144 145 163 143 056 142 162'])

#ldapServiceName
objeto['attributes']['n'].setComponentByName('type', '154 144 141 160 123 145 162 166 151 143 145 116 141 155 145')
objeto['attributes']['n']['vals'].extend(['143 157 162 160 056 165 144 145 163 143 056 142 162 072 164 145 163 164 145 055 060 061 055 164 145 163 164 145 044 100 103 117 122 120 056 125 104 105 123 103 056 102 122'])

#serverName
objeto['attributes']['o'].setComponentByName('type', '163 145 162 166 145 162 116 141 155 145')
objeto['attributes']['o']['vals'].extend(['103 116 075 124 105 123 124 105 055 060 061 124 105 123 124 105 054 103 116 075 123 145 162 166 145 162 163 054 103 116 075 103 103 124 054 103 116 075 123 151 164 145 163 054 103 116 075 103 157 156 146 151 147 165 162 141 164 151 157 156 054 104 103 075 164 145 163 164 145 054 104 103 075 165 144 145 163 143 054 104 103 075 142 162'])

#isSynchronized
objeto['attributes']['p'].setComponentByName('type', '151 163 123 171 156 143 150 162 157 156 151 172 145 144')
objeto['attributes']['p']['vals'].extend(['124 122 125 105'])

#isGlobalCatalogReady
objeto['attributes']['q'].setComponentByName('type', '151 163 107 154 157 142 141 154 103 141 164 141 154 157 147 122 145 141 144 171')
objeto['attributes']['q']['vals'].extend(['124 122 125 105'])

#domainFunctionality
objeto['attributes']['r'].setComponentByName('type', '144 157 155 141 151 156 106 165 156 143 164 151 157 156 141 154 151 164 171')
objeto['attributes']['r']['vals'].extend(['066'])

#forestFunctionality
objeto['attributes']['s'].setComponentByName('type', '146 157 162 145 163 164 106 165 156 143 164 151 157 156 141 154 151 164 171')
objeto['attributes']['s']['vals'].extend(['066'])

#domainControllerFunctionality
objeto['attributes']['t'].setComponentByName('type', '144 157 155 141 151 156 103 157 156 164 162 157 154 154 145 162 106 165 156 143 164 151 157 156 141 154 151 164 171')
objeto['attributes']['t']['vals'].extend(['066'])


#print(objeto['objectName'])
#print(objeto['attributes']['a'])
#print(objeto['attributes']['b'])
#print(objeto['attributes']['c'])
#print(objeto['attributes']['d'])
#print(objeto['attributes']['e'])
#print(objeto['attributes']['f'])
#print(objeto['attributes']['g'])
#print(objeto['attributes']['h'])
#print(objeto['attributes']['i'])
#print(objeto['attributes']['j'])
#print(objeto['attributes']['k'])
#print(objeto['attributes']['l'])
#print(objeto['attributes']['m'])
#print(objeto['attributes']['n'])
#print(objeto['attributes']['o'])
#print(objeto['attributes']['p'])
#print(objeto['attributes']['q'])
#print(objeto['attributes']['r'])
#print(objeto['attributes']['s'])
#print(objeto['attributes']['t'])

f = open("saida.txt", "w")

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']

for i in range(0,19):
    sub = encode(objeto['attributes'][a[i]])
    print(hexdump(sub))
    f.write(hexdump(sub))