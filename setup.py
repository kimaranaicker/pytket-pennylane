# Copyright 2018-2020 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

with open("pennylane/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")

requirements = [
    "numpy",
    "scipy",
    "networkx",
    "autograd",
    "toml",
    "appdirs",
    "semantic_version==2.6",
]

info = {
    'name': 'PennyLane',
    'version': version,
    'maintainer': 'Xanadu Inc.',
    'maintainer_email': 'software@xanadu.ai',
    'url': 'https://github.com/XanaduAI/pennylane',
    'license': 'Apache License 2.0',
    'packages': find_packages(where="."),
    'entry_points': {
        'pennylane.plugins': [
            'default.qubit = pennylane.plugins:DefaultQubit',
            'default.gaussian = pennylane.plugins:DefaultGaussian',
            'default.qubit.tf = pennylane.plugins.default_qubit_tf:DefaultQubitTF',
            'default.tensor = pennylane.beta.plugins.default_tensor:DefaultTensor',
            'default.tensor.tf = pennylane.beta.plugins.default_tensor_tf:DefaultTensorTF',
            ],
        },
    'description': 'PennyLane is a Python quantum machine learning library by Xanadu Inc.',
    'long_description': open('README.rst').read(),
    'provides': ["pennylane"],
    'install_requires': requirements,
    'command_options': {
        'build_sphinx': {
            'version': ('setup.py', version),
            'release': ('setup.py', version)}}
}

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
    "Topic :: Scientific/Engineering :: Physics"
]

setup(classifiers=classifiers, **(info))
devices_list ="pytket.mydevice = pytket_device:pytketDevice"
setup(entry_points={'pennylane.plugins': devices_list})