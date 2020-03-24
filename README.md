# [WIP] MicroPython MPU-6886 I2C driver

The MPU-6886 is a 6-axis motion tracking device that combines a 3-axis gyroscope and a 3-axis accelerometer.

## Usage

Simple test with never ending loop.

```python
import utime
from machine import I2C, Pin
from mpu6886 import MPU6886

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU6886(i2c)

print("MPU6886 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.temperature)

    utime.sleep_ms(1000)
```

By default the library returns 3-tuple of X, Y, Z axis values for acceleration and gyroscope. Default units are `m/s^2`, `rad/s` and `°C`. It is possible to also get acceleration values in `g` and gyro values `deg/s`. See the example below.

```python
import utime
from machine import I2C, Pin
from mpu6886 import MPU6886, SF_G, SF_DEG_S

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor2 = MPU6886(i2c, accel_sf=SF_G, gyro_sf=SF_DEG_S)

print("MPU6886 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.temperature)

    utime.sleep_ms(1000)
```

More realistic example usage with timer. If you get `OSError: 26` or `i2c driver install error` after soft reboot do a hard reboot.

```python
import micropython
from machine import I2C, Pin, Timer
from mpu6886 import MPU6886

micropython.alloc_emergency_exception_buf(100)

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU6886(i2c)

def read_sensor(timer):
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.temperature)

print("MPU6886 id: " + hex(sensor.whoami))

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_sensor)
```

## Gyro Calibration

TODO

## License

The MIT License (MIT). Please see [License File](LICENSE.txt) for more information.