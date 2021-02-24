#!/usr/bin/env python

from setuptools import setup

setup(
    name='isa-rwval',
    version='0.10.10',
    packages=['isatools',
              'isatools.errors'
              ],
    package_data={'isatools': [],
                  '': ['LICENSE.txt', 'README.md']},
    description='Metadata tracking tools help to manage an increasingly '
                'diverse set of life science, environmental and biomedical '
                'experiments',
    author='ISA Infrastructure Team',
    author_email='isatools@googlegroups.com',
    url='https://github.com/ISA-tools/isa-rwval',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        ],
    install_requires=[
        'networkx==2.5'
    ],
    extras_require={
        'viz': ['matplotlib'],
        'tables': ['pandas', 'numpy']
    },
    test_suite='tests'
)
