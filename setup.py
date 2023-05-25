from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hubspot_integration/__init__.py
from hubspot_integration import __version__ as version

setup(
	name="hubspot_integration",
	version=version,
	description="Hubspot Integration",
	author="Xurpas Inc.",
	author_email="andy@xurpas.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
