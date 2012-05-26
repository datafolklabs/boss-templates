
from setuptools import setup, find_packages
import sys, os

VERSION = '@version@'

setup(name='@module@.devtools',
    version=VERSION,
    description="@description@",
    long_description="@description@",
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
        "@module@.core",
        "@module@.cli",
        "cement2",
        ],
    setup_requires=[
        ],
    entry_points="""
    """,
    namespace_packages=[
        '@module@',
        '@module@.cli',
        '@module@.cli.bootstrap',
        '@module@.cli.controllers',
        ],
    )
