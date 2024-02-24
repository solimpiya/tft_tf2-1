import io
import os

from setuptools import setup, find_packages


install_requires = [
    'keras >= 2.3.0',
    'numpy>=1.17.4',
    'pandas>=0.25.3',
    'scikit-learn>=0.22',
    'tensorflow-probability>=0.8.0',
    'wget>=3.2',
    'pyunpack>=0.1.2',
    'patool>=1.12'
]

setup(
    name="tft_tf2",
    version='0.1',
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=install_requires,
)
