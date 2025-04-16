class TemperatureOutOfRangeError(Exception):
    def __init__(self, temp):
        super().__init__(f"Temperature {temp}°C is out of range! Must be between -50 and 50.")

def set_temperature(temp):
    if temp < -50 or temp > 50:
        raise TemperatureOutOfRangeError(temp)
    print(f"Temperature set to {temp}°C")

try:
    set_temperature(100)
except TemperatureOutOfRangeError as e:
    print("Temperature error:", e)
