from pyicloud import PyiCloudService
api = PyiCloudService('ruchitp2000@gmail.com','Shru@1224')



def fetchCoordinates():
    api.data
    api.devices


    device = api.devices[0]
    print(device)
    location = device.location()
    print(location)

    # extract lattitude
    lat = location['latitude']

    # extract longitude
    lon = location['longitude']

    coordinates = [lat,lon]
    print(coordinates)

    return coordinates