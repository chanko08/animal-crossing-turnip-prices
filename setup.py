import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="animal-crossing-turnip-prices-chanko08",
    version="0.0.3",
    author="Alex Bechanko",
    author_email="chanko08@gmail.com",
    description="Animal Crossing New Horizons turnip price predictor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chanko08/animal-crossing-turnip-prices",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)