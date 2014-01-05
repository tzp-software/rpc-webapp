try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name':'rockpaperscissors',
    'version':'1.0.0',
    'install_requires':['Flask'],
        }
setup(**config)
