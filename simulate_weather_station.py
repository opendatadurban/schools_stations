'''
Script to test website interface
'''

import datetime,requests,json
from time import sleep
import time
'''
press = 0
temperature = 0
humidity = 0
pm10 = 0
pm25 = 0
my_location = 'test'
myname = 'WS101'
for i in range(5):
    press_time = time.time()
    temp_time = time.time()
    dust_time = time.time()
    #POSSIBLE ERROR: temp_time used as name for humidity time

    print 'talking to server'
    # post to the village
    payload = {'press':press,'press_time':press_time,'temp': temperature,'temp_time':temp_time,'humid':humidity,'temp_time':temp_time,'pm_10':pm10,'dust_time':dust_time,'pm_25':pm25,'dust_time':dust_time,'loc':my_location,'device_ID':myname}
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    try:
        postad = "http://citizen-sensors.herokuapp.com/data"
        r = requests.post(postad, data=json.dumps(payload),headers=headers)
        print postad
    except Exception as e:
        print "Server not listening to me - no one ever listens to me!!!"

    press += 1
    temperature += 1
    humidity += 1
    pm10 += 1
    pm25 += 1
    time.sleep(10)
'''
press = 0
temperature = 0
humidity = 0
windspeed = 0
winddir = 0
gas = 0

pm10 = 0
pm25 = 0
my_location = 'test'
myname = 'WS101'

for i in range(5):
    press_time = time.time()
    temp_time = time.time()
    dust_time = time.time()
    winddir_time = time.time()
    windspeed_time = time.time()
    gas_time = time.time()

    #original
    #payload = {'temp': temperature,'temp_time':temp_time,'humid':humidity,'temp_time':temp_time,'wind_speed':windspeed,'winds_time':windspeed_time,'wind_dir':winddir,'windd_time':winddir_time,'gas':gas,'gas_time':gas_time,'pm_10':pm10,'dust_time':dust_time,'pm_25':pm25,'dust_time':dust_time,'device_ID':myname}

    #new
    #payload = {'temp': temperature,'temp_time':temp_time,'humid':humidity,'temp_time':temp_time,'pm_10':pm10,'dust_time':dust_time,'pm_25':pm25,'dust_time':dust_time,'device_ID':myname}

    payload = {'press':'NaN','press_time':'NaN','temp': temperature,'temp_time':temp_time,'humid':humidity,'temp_time':temp_time,'pm_10':pm10,'dust_time':dust_time,'pm_25':pm25,'dust_time':dust_time,'loc':my_location,'device_ID':myname}

    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    try:
        postad = "http://citizen-sensors.herokuapp.com/data"
        r = requests.post(postad, data=json.dumps(payload),headers=headers)
        print postad
    
    except Exception as e:
        print "Server not listening to me - no one ever listens to me!!!"

    press += 1
    temperature += 1
    humidity += 1
    pm10 += 1
    pm25 += 1
    time.sleep(1)
    windspeed =0
    winddir = 0
    gas = 0



