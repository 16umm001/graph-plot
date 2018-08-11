from setuptools import find_packages, setup 
with open("README.rst", "r") as fobj:
    long_description = fobj.read()
setup(name = 'plot-graph',
    version = '0.1',
    description = "PLot graph",
    long_description = "Plot graph between two numbers. just enter the x and y values to get your desired graph",
    platforms = ["Linux","MacOS","Windows"],
    author="Adarsh Pathak",
    author_email="adarshp199877@gmail.com",
    url="https://github.com/adarshp199877/graph-plot",
    license = "MIT",
    packages=find_packages()
)