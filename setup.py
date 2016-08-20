#!/usr/bin/env python

from setuptools import setup


requirements = [
    'discord.py==0.11.0'
]


setup(
    name='discord-gather',
    version='0.1',
    description='A gather bot for Discord',
    author='Mac Chapman',
    author_email='mac@veryhappythings.co.uk',
    url='https://github.com/veryhappythings/discord-gather',
    packages=['gather'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'discord-gather = gather.main:main',
        ]
    }
)
