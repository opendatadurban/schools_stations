import time
from time import sleep
import aqi

def dust_helper():
    pm25 = []
    pm10=[]
    print 'turning system on'
    aqi.cmd_set_sleep(0)
    aqi.cmd_set_mode(1)
    time.sleep(10)
    for t in range(15):
        values = aqi.cmd_query_data()
        try:
            pm25.append(values[0])
            pm10.append(values[1])
        except:
            print 'bubkiss'

        time.sleep(2)
    print 'turning system off'
    aqi.cmd_set_mode(0)
    aqi.cmd_set_sleep()
    return pm10,pm25

if __name__=="__main__":
    for i in range(5):
        time.sleep(2)
        pm_10,pm25 = dust_helper()
        print pm_10
