from setuptools import setup

setup(
    name='dad',
    version='1.0.0',
    packages=['dad', 'dad.logging', 'dad.sensors', 'dad.sensors.iio', 'dad.sensors.gpio'],
    url='https://github.com/BrendenDielissen-uofc/UofC-DAD',
    license='',
    author='brenden.dielissen',
    author_email='brenden.dielissen@ucalgary.ca',
    description='Project DAD package', install_requires=['overrides', 'iio']
)
