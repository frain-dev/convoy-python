"""Setup script for realpython-reader"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="convoy-python",
    version="0.2.0",
    description="Python SDK for Convoy",
    url="https://github.com/frain-dev/convoy-python",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Frain Inc.",
    author_email="info@frain.dev",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["convoy", ".convoy/client", ".convoy/api", ".convoy/utils"],
    include_package_data=True,
    install_requires=["requests"],
)