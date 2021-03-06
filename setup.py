import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="spip2",
    version="0.0.1",
    description="Wrapper of Python's pip",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sebbu2/spip2",
    author="sebbu",
    author_email="sebbu@yahoo.fr",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["spip2"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "spip2=spip2.__main__:main",
        ]
    },
)

