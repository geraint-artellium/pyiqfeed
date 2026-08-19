# coding=utf-8
"""Install pyiqfeed into your library path."""

from setuptools import setup

setup(
    name='pyiqfeed',
    version='1.0',
    description='Handles connections to IQFeed, the market data feed by DTN',
    url='https://github.com/akapur/pyiqfeed',
    author='Ashwin Kapur, Geraint Harker',
    author_email='ashwin.kapur@gmail.com, geraint@artellium.ai',
    license='GPL v2',
    packages=['pyiqfeed'],
    zip_safe=False, install_requires=['numpy'])
