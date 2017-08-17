from w1thermsensor import W1ThermSensor
  
sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()
print(temperature_in_celsius)

