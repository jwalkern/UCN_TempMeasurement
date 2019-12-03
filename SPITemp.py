from time import sleep
import spidev


def read_ADC(ADC, channel, vref):
    """
    Aflæser ADCen og returnerer resultatet
    """

    # skriv her koden der er nødvendig for at læse fra den angivne kanal 'channel' og reference spænding
    svar = ADC.xfer2([1,0b11000000, 0])
    return ((svar[1]&3) << 8)+svar[2] # returner den læsete værdi


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

    while True:
        data = read_ADC(adc,0,0)
        print(data)  # tilføj manglende argumenter

        sleep(0.5)
except KeyboardInterrupt:
    exit()

