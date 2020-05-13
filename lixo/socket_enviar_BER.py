import socket

PORT = 389
HOST = '10.60.1.19' #host qualquer
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)


arquivo = open('saida.txt', 'r')
#utilizar saida_pcp.txt para o arquivo copiado do pcap

msg = arquivo.read()
arquivo.close()


#print(msg)

udp.sendto(msg, dest)
udp.close()
