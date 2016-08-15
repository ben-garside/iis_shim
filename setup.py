"""
IIS_Shim
-----------
python IIS_Shim
Link
`````
* Source
  https://github.com/abusaidm/
"""
from distutils.core import setup

version = "0.1.2"

setup(
    name="iis_shim",
    version=version,
    author="Mohamed Abusaid",
    author_email="m.abusaid<at>yahoo<dot>com",
    packages=[
        "iis_shim"
        ],
    include_package_data=True,
    url="http://github.com/abusaidm/iis_shim/packages/{}/".format(version),

    # license="LICENSE.txt",
    description="iis_shim",
    # long_description=open("README.txt").read() or just """ lots of text here too""",
    # Dependent packages (distributions)
    install_requires=[
    ],
)