#!/usr/bin/python3
"""ISS Tracking using python"""

# import(*always at top) request
import requests
import reverse_geocoder as rg
import datetime

# define URL
ISSLOCATION = 'http://api.open-notify.org/iss-now.json'

def main():
    """runtime code"""

    # call api
    currentpos = requests.get(ISSLOCATION)
    #print(currentpos)

    # translate json into python lists/dictionary
    viewable = currentpos.json()
    #print(viewable)

    lon = viewable['iss_position']['longitude']
    #print(lon)
    lat = viewable['iss_position']['latitude']
    #print(lat)
    time = viewable['timestamp']
    time = datetime.datetime.fromtimestamp(time)
    
    coords_truple = (lat, lon)
    result = rg.search(coords_truple, verbose=False)
    city = result[0]['name']
    country = result[0]['cc']

    print(f'''
    CURRENT LOCATION OF THE ISS: 
    Timestamp: {time}
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}
    ''')

    #for lon in viewable['iss_position']:
    #    print("Lon:", lon['longitude'])

if __name__ == "__main__":
    main()