#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="piss",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'enum34',
    ],
    author="Minsu(Eric) Kim",
    author_email="k09089@naver.com",
    description="Python packet parser in simple structure type",
    license="GPLv2",
    keywords="pickle,packet,pcap,packet structure",
    url="https://github.com/BetaS/pypiss",
    long_description=open("README.md").read(),
    classifiers=['License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                 'Programming Language :: Python',
                 'Operating System :: POSIX',
                 'Programming Language :: Python :: 2.7'],

)