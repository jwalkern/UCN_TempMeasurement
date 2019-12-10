import json

def templogging(temp_room, temp_target):
    # Create empty dictionary and adds data into Field1 and Field2.
    SensorData = {}
    SensorData['Field1'] = temp_room
    SensorData['Field2'] = temp_target
    return SensorData

def jsonlogging(SensorData):
    # Adds data to the file object, if the file doesn't exist, then it's created.
    filNavn = "tempdata.json"
    with open(filNavn, "a") as filObject:
        json.dump(SensorData, filObject,)
        filObject.write('\n')
