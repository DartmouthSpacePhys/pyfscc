import os
from distutils.core import setup

if os.name == 'nt':
    requirements = ['serial', 'win32']
else:
    requirements = ['serial']

setup(name='pyfscc',
      version='2.0.0',
      py_modules=['fscc'],
      requires=requirements,
      )