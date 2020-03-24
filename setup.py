import sys
sys.path.pop(0)
from setuptools import setup
from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="micropython-mpu6886",
    py_modules=["mpu6886"],
    version="0.1.0",
    description="MicroPython I2C driver for MPU6886 6-axis motion tracking device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="accelerometer, gyro, micropython, i2c",
    url="https://github.com/tuupola/micropython-mpu6886",
    author="Mika Tuupola",
    author_email="tuupola@appelsiini.net",
    maintainer="Mika Tuupola",
    maintainer_email="tuupola@appelsiini.net",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
