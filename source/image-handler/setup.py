# coding: utf-8

from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

tests_require = [
    'mock',
    'pytest'
]

setup(
    name='image_handler',
    version='2.0',
    description='AWS Serverless Image Handler',
    author='Ian Hartz',
    license='ASL',
    zip_safe=False,
    test_suite = 'tests',
    packages=['image_handler'],
    package_dir={'image_handler': '.'},
    include_package_data=True,
    package_data={
            '': ['*.conf'],
    },
    install_requires=[
        'botocore==1.8',
        'tornado_botocore==0',
        'requests_unixsocket>=0.1.5',
        'thumbor>=6.2.1',
        'tc_aws==6.0.3',
        'opencv-python==3.2.0.6'
    ],
    dependency_links=[
        'git+https://github.com/timshingyu/tornado-botocore.git@master#egg=tornado-botocore-0'
    ],
    extras_require={
            'tests': tests_require,
        },
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)
