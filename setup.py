#! -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='archer_nlp',  # 应用名
    version='0.1.1',  # 版本号
    description='archer nlp',
    url='https://github.com/beybin/archer_nlp',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=["pandas", "numpy"]
)
