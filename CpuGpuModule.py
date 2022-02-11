import wmi


def getTemperature(arg):
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
    sensors = w.Sensor()

    for sensor in sensors:
        if arg == 'CPU' and sensor.Name == 'CPU Package' and sensor.SensorType == 'Temperature':
            return sensor.Value
        elif arg == 'GPU' and sensor.Name == 'GPU Temp' and sensor.SensorType == 'Temperature':
            return sensor.Value
