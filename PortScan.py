#!/usr/bin/python2.7

import socket,sys

if len(sys.argv) < 4:
	print "Modo de uso: ./PortScan.py 192.168.0.1 1 25"
else:
	ini = int(sys.argv[2])
	fim = int(sys.argv[3])+1

	for porta in range (ini,fim):
		meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if meusocket.connect_ex((sys.argv[1],porta)) == 0:
			print "Porta %s - status [ABERTA]" %porta
			meusocket.close()
		else:
			print "Porta %s - status [FECHADA]" %porta
			meusocket.close()
