
from setuptools import setup, find_packages
import sys, os

VERSION = '@version'

setup(name='@module@.core',
    version=VERSION,
    description="@description",
    long_description="@description",
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
        ],
    setup_requires=[
        ],
    entry_points="""
    """,
    namespace_packages=[
        '@module@',
        '@module@.hub',
        '@module@.cli',
        '@module@.cli.bootstrap',
        '@module@.cli.controllers',
        '@module@.lib',
        ],
    )
