# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in branding/__init__.py
from branding import __version__ as version

setup(
	name='branding',
	version=version,
	description='ERPNext branding',
	author='Bhavesh Maheshwari',
	author_email='maheshwaribhavesh95863@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
