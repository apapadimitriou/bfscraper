from setuptools import setup

setup(name='bfscraper',
      version='0.1',
      description='Scrape Betfair price data for Australian horse racing',
      url='https://github.com/apapadimitriou/bfscraper',
      author='Antony Papadimitriou',
      author_email='antony.papadimitriou@icloud.com',
      license='MIT',
      packages=['bfscraper'],
      install_requires=['pandas', 'datetime'],
      zip_safe=False)