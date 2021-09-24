from setuptools import setup

setup(
    name='protectsql',
    version='0.0.1',
    py_modules=['protectsql'],
    install_requires=[
        'Click',
				'Flask',
				'pyre-check',
    ],
    entry_points={
        'console_scripts': [
            'protectsql = protectsql.commands:protectsql',
        ],
    },
)
