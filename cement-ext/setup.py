
from setuptools import setup, find_packages
import sys, os

setup(name='@package@.ext.@ext_module@',
    version='@version@',
    description="@ext_module.capitalize@ Framework Extension for Cement",
    long_description="@ext_module.capitalize@ Framework Extension for Cement",
    classifiers=[], 
    keywords='',
    author='@creator@',
    author_email='@email@',
    url='@url@',
    license='@license@',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="",
    namespace_packages=[
        "@package@",
        "@package@.ext",
        ],
    )
