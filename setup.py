#! -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pdutils',  # 应用名
    version='0.1.0',  # 版本号
    # packages=['pdutils'],  # 包括在安装包内的 Python 包
    packages=find_packages(),
    install_requires=["pandas", "numpy"]
)
