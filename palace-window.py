import asyncio
import requests
import time

from pywizlight import wizlight, PilotBuilder
#from datetime import datetime

async def do_palace_window():
    # Set up a standard light with IP from file
    ip_file = open('palace-window-config/ip.txt','r')
    ip = ip_file.read()
    ip_file.close()
    light = wizlight(ip)
    
    # Set bulb defaults
    # await light.turn_on(PilotBuilder(brightness = 255))

    # Get a weather forecast from a city from file
    city_file = open('palace-window-config/city.txt','r')
    city = city_file.read()
    city_file.close()
    weather_num = get_weather(city,'icon_num')
    print(weather_num)
    weather_temperature = get_weather(city,'temperature')
    print(weather_temperature)

    # Set bulb color
    color = get_bulb_color(weather_num, weather_temperature)

    # Turn on bulb with color
    await light.turn_on(color)

def get_bulb_color(weather_num, weather_temperature):
    weather_num = int(weather_num)
    weather_temperature = float(weather_temperature)
    fallback_color = PilotBuilder(rgb = (255, 0, 0))
    moon = PilotBuilder(rgb = (0, 0, 255))
    sunny = PilotBuilder(rgb = (255, 150, 0))
    cloudy = PilotBuilder(rgb = (150, 175, 175))
    rain = PilotBuilder(rgb = (0, 200, 255))
    snow = PilotBuilder(rgb = (150, 175, 255))
    # Not available
    if weather_num == 1: 
        color = fallback_color
    # Sunny
    elif weather_num == 2: 
        color = sunny
    # Mostly sunny
    elif weather_num == 3: 
        color = sunny
    # Partly sunny
    elif weather_num == 4: 
        color = sunny
    # Mostly cloudy
    elif weather_num == 5: 
        color = cloudy
    # Cloudy
    elif weather_num == 6: 
        color = cloudy
    # Overcast
    elif weather_num == 7: 
        color = cloudy
    # Overcast with low clouds
    elif weather_num == 8: 
        color = cloudy
    # Fog
    elif weather_num == 9: 
        color = cloudy
    # Light rain
    elif weather_num == 10: 
        color = cloudy
    # Rain
    elif weather_num == 11: 
        color = rain
    # Possible rain
    elif weather_num == 12: 
        color = rain
    # Rain shower
    elif weather_num == 13: 
        color = rain
    # Thunderstorm
    elif weather_num == 14: 
        color = rain
    # Local thunderstorms
    elif weather_num == 15: 
        color = rain
    # Light snow
    elif weather_num == 16: 
        color = snow
    # Snow
    elif weather_num == 17: 
        color = snow
    # Possible snow
    elif weather_num == 18: 
        color = snow
    # Snow shower
    elif weather_num == 19: 
        color = snow
    # Rain and snow
    elif weather_num == 20: 
        color = rain
    # Possible rain and snow
    elif weather_num == 21: 
        color = rain
    # Rain and snow
    elif weather_num == 22: 
        color = rain
    # Freezing rain
    elif weather_num == 23: 
        color = rain
    # Possible freezing rain
    elif weather_num == 24: 
        color = rain
    # Hail
    elif weather_num == 25: 
        color = snow
    # Clear (night)
    elif weather_num == 26: 
        color = moon
    # Mostly clear (night)
    elif weather_num == 27: 
        color = moon
    # Partly clear (night)
    elif weather_num == 28: 
        color = moon
    # Mostly cloudy (night)
    elif weather_num == 29: 
        color = moon
    # Cloudy (night)
    elif weather_num == 30: 
        color = moon
    # Overcast with low clouds (night)
    elif weather_num == 31: 
        color = moon
    # Rain shower (night)
    elif weather_num == 32: 
        color = moon
    # Local thunderstorms (night)
    elif weather_num == 33: 
        color = moon
    # Snow shower (night)
    elif weather_num == 34: 
        color = moon
    # Rain and snow (night)
    elif weather_num == 35: 
        color = moon
    # Possible freezing rain (night)
    elif weather_num == 36: 
        color = moon
    else:
        color = fallback_color
    # color = fallback_color
    return color

def get_weather(city,type): 
    key_file = open('palace-window-config/key.txt','r')
    key = key_file.read()
    key_file.close()
    parameters = {
        'key': key,
        'place_id': city,
        'sections': 'current',
        'language': 'en',
        'units': 'metric'
    }
    url = "https://www.meteosource.com/api/v1/free/point"
    data = requests.get(url, parameters).json()
    return format(data['current'][type]) 

while True:
    try:
        asyncio.run(do_palace_window())
        time.sleep(1800)
    except:
        time.sleep(60)
