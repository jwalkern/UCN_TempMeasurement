import requests


def thingSpeakTransfer(temp1, temp2, time):
    """
   Her forklarer vi hvad den her funktion gør
   """
    try:
        writeKey = "EBUYTMJKFLG4934Z"
        channelID = 917419
        url = f"https://api.thingspeak.com/channels/{channelID}/bulk_update.json"
        created_at = time
        field1 = temp1
        field2 = temp2

        data = {
            "write_api_key": writeKey,
            "updates": [{
                "created_at": created_at,
                "field1": field1,
                "field2": field2
            }]}

        response = requests.post(url, json=data)
        status = response.status_code

    except:
        print("ThingSpeak transfer failed.")
        print(f"Status code: {status}")