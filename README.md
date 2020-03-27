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

Gyro drift can be improved with calibration. Calibration calculates and sets offsets which adjust the sensor values in rest to be close to zero on all axises.

The calibration function takes two parameters: `count` is the number of samples to collect and `delay` is the delay in millisecods between the samples. With the default values of `256` and `0` calibration takes only a second. While calibration function is running the sensor should be perfectly stable. Do not touch or move it.

```python
from machine import I2C, Pin
from mpu6886 import MPU6886

i2c = I2C(scl=Pin(22), sda=Pin(21))

sensor = MPU6886(i2c)
offset = sensor.calibrate(count=256, delay=0)
```

After finishing the `calibrate()` method also returns a tuple for `offset`. Like before you could store this value somewhere and pass it to the MPU6886 constructor in the future. Below example only illustrates how to use the constructor.


```python
from machine import I2C, Pin
from mpu6886 import MPU6886

i2c = I2C(scl=Pin(22), sda=Pin(21))

sensor = MPU6886(i2c, offset=(0.1139419, -0.08501822, -0.2589432))
```

## License

The MIT License (MIT). Please see [License File](LICENSE.txt) for more information.