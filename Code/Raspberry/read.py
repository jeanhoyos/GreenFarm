#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Test du port série
import serial
test_string = "Je teste le port série 1 2 3 4 5"
port_list = ["/dev/ttyAMC0", "/dev/ttyAMA0", "/dev/ttyS0", "/dev/ttyS0",]
for port in port_list:
  try:
    serialPort = serial.Serial(port, 9600, timeout = 2)
    print "Port Série ", port, " ouvert pour le test :"
    #bytes_sent = serialPort.write(test_string)
    #print "Envoyé ", bytes_sent, " octets"
    data = serialPort.readline
    print  dat
  except IOError:
    print "Erreur sur ", port, "\n"
#JEan 