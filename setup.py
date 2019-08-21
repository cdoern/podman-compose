import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
except:
    readme = ''

version = '0.1.1'

setup(
    name='podman-compose',
    version=version,
    description="A script to run docker-compose.yml using podman",
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='podman, podman-compose',
    author='Muayyad Alsadi',
    author_email='alsadi@gmail.com',
    url='https://github.com/muayyad-alsadi/podman-compose',
    package_dir={'': '.'},
    py_modules=['podman_compose'],
    packages=find_packages(where='.'),
    entry_points={
        'console_scripts': [
            'podman-compose = podman_compose:main'
        ]
    },
    include_package_data=True,
    license='GPL-2.0-only',
    install_requires=[
        'pyyaml'
    ],
    # test_suite='tests',
    # tests_require=[
    #     'coverage',
    #     'pytest-cov',
    #     'pytest',
    #     'tox',
    # ]
)
