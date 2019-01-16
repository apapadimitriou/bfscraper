import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bfscraper",
    version="0.3.2",
    author="Antony Papadimitriou",
    author_email="antony.papadimitriou@icloud.com",
    description="Scrapes Betfair price data for Australian horse racing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apapadimitriou/bfscraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)