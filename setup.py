#!/usr/bin/env python

import os
from setuptools import setup, find_packages

setup(
    name='qcloud-cmq-sdk-py3',
    version=0.1,
    description='Tencent Cloud SDK for CMQ API 2.0 running in python3',
    author='Tencent Cloud CMQ Team',
    url='https://github.com/tencentyun/cmq-python-sdk/tree/python3',
    maintainer_email="yorkxyzhang@tencent.com",
    scripts=[],
    packages=find_packages(),
    license="Apache License 2.0",
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
