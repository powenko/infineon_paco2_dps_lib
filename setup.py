from setuptools import setup, find_packages

setup(
    name='infineon_paco2_dps_lib',
    version='0.1.0',
    description='Library for interfacing with Infineon PA_CO2 and DPS sensors',
    author='Powen Ko',
    author_email='powenkoads@gmail.com',
    url='https://github.com/powenko/infineon_paco2_dps_lib',
    packages=find_packages(),
    install_requires=[
        'smbus2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
