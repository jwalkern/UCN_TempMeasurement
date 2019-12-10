from time import sleep
from DataLogging import *
import spidev


def read_ADC(ADC, channel, vref):
    """
    Aflæser ADCen og returnerer resultatet
    """

    # skriv her koden der er nødvendig for at læse fra den angivne kanal 'channel' og reference spænding
    svar = ADC.xfer2([1,0b11000000, 0])
    return ((svar[1]&3) << 8)+svar[2] # returner den læsete værdi

def read_ADC2(ADC, channel, vref):
    """
    Aflæser ADCen og returnerer resultatet
    """

    # skriv her koden der er nødvendig for at læse fra den angivne kanal 'channel' og reference spænding
    svar = ADC.xfer2([1,0b10110000, 0])
    return ((svar[1]&3) << 8)+svar[2]

def init_ADC(SSn=0):
    """
    Initialiserer ADC chippen
    """

    # skriv kode her til at initialisere dit ADC object
    spi = spidev.SpiDev()
    spi.open(0,SSn)
    spi.max_speed_hz = 50000

    return spi # returner ADC object


try:
    adc = init_ADC(1)  # angiv det rigtige slave slect nummer
    adc2 = init_ADC(1)

    while True:
        value2 = read_ADC2(adc2, 0, 0)
        value = read_ADC(adc,0,0)
        volts2 = (value2*5)/1024
        volts = (value*5)/1024
        temp2 = volts2/ (10.0 / 1000)
        temp = volts/ (10.0 / 1000)
        print("Rør temp: %4d/1023 => %5.3f V => %4.1f Grader." % (value, volts, temp) + "Rum temp: %4d/1023 => %5.3f V => %4.1f Grader." %(value2, volts2, temp2))


        #Tester de nye logging funktioner
        templogging(temp, temp2)
        jsonlogging(templogging(temp, temp2))

        sleep(5)

except KeyboardInterrupt:
    exit()

