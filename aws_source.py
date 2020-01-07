# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:35:16 2019

@authors:
    Christian Hansen,
    Kasper Griebel Mogensen,
    Birita Mortensen, 
    Jan Nielsen,
    Mikkel Vardinghus.
"""

##############################################################################
"""
To do:
    - thingspeak funktion skal have en time-funktion
    - trigger funktion skal kigges på
    - sms funktion skal have ny bruger
    - skriv kommentarer
    - hvor skal der hardcodes variabler?
"""
##############################################################################

import aws_functions as aws

# Variabler for kommunikation med ADC over SPI.
vref = 5
roomTempChannel = 0b10110000
pipeTempChannel = 0b11000000

# Variabler for afsending af data til ThingSpeak.
channelID       = 917419
writeKey        = 'EBUYTMJKFLG4934Z'

# Variabler for afsending af e-mail alarm
smtpHost        = 'smtp.gmail.com'
smtpPort        = 465
sMail           = 'avwasp.inc@gmail.com'
sPass           = 'vand12345'
rMail           = '1080488@ucn.dk'

# Variabler for afsending af sms alarm
accountSID      = 'Default'
authToken       = 'Default'
messageBody     = 'Default' 
sNum            = 'Default'
rNum            = 'Default' # Nummeret skal være verified på Twilio.


# PROGRAM KODE STARTER HER

running = True
MCP3008 = aws.initADC(1)

while running:
    
    roomTemp  = round(aws.readADC(MCP3008,roomTempChannel,vref),1)
    pipeTemp  = round(aws.readADC(MCP3008,pipeTempChannel,vref),1)
    print(roomTemp)
    print(pipeTemp)
    
    aws.thingSpeakTransfer(channelID, writeKey, roomTemp, pipeTemp)
    
    trigger = aws.checkTempState(roomTemp, pipeTemp)
    
    if trigger:
        aws.AlarmEmail(smtpHost, smtpPort, sMail, sPass, rMail)
        aws.SMSMsg(accountSID, authToken, messageBody, sNum, rNum)
