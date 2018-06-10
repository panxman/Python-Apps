import requests
import pandas


url = 'https://maps.googleapis.com/maps/api/geocode/json'


# Getting lattitude and longitude from Google's Geocode
def getLatLng(address):
    params = {'sensor': 'false', 'address': address}
    r = requests.get(url, params=params)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    return location


# Adding Lat and Lng columns in the dataframe
def updateDF(data):
    df = pandas.DataFrame(data)
    lat = []
    lng = []
    addr = ""
    if 'Address' in df.columns:
        addr = "Address"
    else:
        addr = "address"
    for index, row in df.iterrows():
        try:
            location = getLatLng(row[addr])
            # Add values to the lists
            lat.append(location['lat'])
            lng.append(location['lng'])
        except:  # noqa: E722
            lat.append("error")
            lng.append("error")
    # Add the two columns in the DataFrame
    df['Latitude'] = lat
    df['Longitude'] = lng
    return df
