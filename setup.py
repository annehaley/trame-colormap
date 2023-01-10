from setuptools import setup

setup(
    name='colormapper',
    version='1.0.0',
    packages=['colormapper'],
    package_dir={'colormapper': 'trame'},
    package_data={'colormapper': ['build/*']},
    include_package_data=True,
)
