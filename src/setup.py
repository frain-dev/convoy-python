"""Setup script for realpython-reader"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent


# This call to setup() does all the work
setup(
    name="convoy",
    version="0.1.0",
    description="Python SDK for Convoy",
    url="https://github.com/frain-dev/convoy-python",
    author="Frain Inc.",
    author_email="info@frain.dev",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["api", "utils"],
    include_package_data=True,
)