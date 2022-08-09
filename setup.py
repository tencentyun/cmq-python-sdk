#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='tcmq-python3-sdk',
    version="1.0",
    description='Tencent Cloud SDK for TCMQ API 2.0 running in python3',
    author='Tencent Cloud TCMQ Team',
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
