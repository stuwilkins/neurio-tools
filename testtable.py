import lxml.html
from urllib.request import urlopen
import numpy as np
import math

html = urlopen("http://192.168.1.7/both_tables.html")
html = html.read()
markup = lxml.html.fromstring(html)

tbl = []
rows = markup.cssselect("tr")
for row in rows:
  tbl.append(list())
  for td in row.cssselect("td"):
    tbl[-1].append(td.text_content())

sensors = ['active_power','reactive_power','voltage']
channels = ['power','energy_imported','energy_exported','reactive_power','voltage']

sensor_readings = []
for t in tbl[2:6]:
    sensor_readings.append(dict(zip(sensors, [float(x) for x in t[1:]])))

for sr in sensor_readings:
    angle = math.atan2(sr['reactive_power'], sr['active_power']) * 180 / math.pi
    sr['phase_angle'] = angle
    apwr = math.sqrt(math.pow(sr['reactive_power'], 2) + math.pow(sr['active_power'], 2))
    sr['apparent_power'] = apwr
    try:
        I = apwr / sr['voltage']
    except ZeroDivisionError:
        sr['current'] = 0.0
    else:
        sr['current'] = I

channel_readings = []
for t in tbl[8:11]:
    channel_readings.append(dict(zip(channels, [float(x) for x in t[1:]])))

print(sensor_readings)
print(channel_readings)

