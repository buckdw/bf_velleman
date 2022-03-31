from setuptools import setup
from setuptools import find_packages
 
VERSION = '1.0.0'
DESCRIPTION = 'Velleman library'
LONG_DESCRIPTION = 'A package that provides API for Velleman LED display'
 
# Setting up
setup(
    name="bf_velleman",
    version=VERSION,
    author="""
        Diederick de Buck
        """,
    author_email="""
        diederick.de.buck@blue-fez.com
        """,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    python_requires='>=3.0',
    install_requires=[],
    keywords=['python', 'REST API', 'Velleman', 'LED', 'display'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    license_files = ('LICENSE.txt'),
    options=({'bdist_wheel':{'universal':True}})
)