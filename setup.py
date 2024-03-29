from setuptools import setup, find_packages

setup(
    name='MyPackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'my_script = my_package.main:main',
        ]
    },
)
