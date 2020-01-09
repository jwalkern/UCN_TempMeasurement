import json
import time


def templogging(temp_room, temp_target):
    # Create empty dictionary and adds data into Field1 and Field2.
    SensorData = {}
    SensorData['TimeStamp'] = time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime())
    SensorData['Field1'] = round(temp_room, 1)
    SensorData['Field2'] = round(temp_target, 1)
    return SensorData


def jsonlogging(SensorData):
    # Adds data to the file object, if the file doesn't exist, then it's created.
    filNavn = "bulk_update.json"
    with open(filNavn, "a") as filObject:
        json.dump(SensorData, filObject, )
        #filObject.write('\n')


