from setuptools import setup

setup(
    name='mriqc',
    packages=['mriqc'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-Restful',
        'Flask-PyMongo'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
