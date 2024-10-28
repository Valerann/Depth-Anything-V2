from setuptools import setup, find_packages
import os

# collect requirements from requirements.txt
lib_dir = os.path.dirname(os.path.realpath(__file__))
requirements_path = lib_dir + "/requirements.txt"
install_requires = []
if os.path.isfile(requirements_path):
    with open(requirements_path) as f:
        install_requires = f.read().splitlines()

# remove comments
_install_requires = []
for req in install_requires:
    idx = req.find("#")
    if idx == -1:
        _install_requires.append(req)
    else:
        req = req[:idx]
        if req:
            _install_requires.append(req)
install_requires = _install_requires

setup(
    name='depth_anything_v2',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/DepthAnything/Depth-Anything-V2',
    license='Apache-2.0 license',
    author='apple',
    author_email='',
    description='',
    install_requires=install_requires
)
