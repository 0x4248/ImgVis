# ImgVis
# Visualize images with graphs
# Github: https://www.github.com/0x4248/ImgVis
# Licence: GNU General Public License v3.0
# By: 0x4248

python = python3
pip = pip3

all: update_pip install_requirements build

build:
	$(python) setup.py sdist bdist_wheel

update_pip:
	$(pip) install --upgrade pip

install_requirements:
	$(pip) install -r requirements.txt
	$(pip) install --user --upgrade setuptools

clean:
	rm -rf build dist ImgVis.egg-info

help:
	@echo "Makefile for ImgVis"
	@echo "Usage: make [target]"
	@echo "all: update_pip install_requirements build"
	@echo "build: Build the package"
	@echo "update_pip: Update pip"
	@echo "install_requirements: Install requirements"
	@echo "clean: Clean the build files"

.PHONY: all build update_pip install_requirements clean