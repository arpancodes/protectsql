from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='protectsql',
    version='0.0.1',
    author="Arpan Abhishek",
    author_email="arpanforbusiness@gmail.com",
    description="A small package to track SQL injection in flask app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arpancodes/protectsql",
    project_urls={
        "Bug Tracker": "https://github.com/arpancodes/protectsql/issues",
    },
    py_modules=['protectsql'],
    install_requires=[
        'Click',
        'Flask',
        'pyre-check',
    ],
    package_dir={"": "."},
    entry_points={
        'console_scripts': [
            'protectsql = protectsql.commands:protectsql',
        ],
    },
)
