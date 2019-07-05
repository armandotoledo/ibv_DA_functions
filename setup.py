from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='DA_Functions',
    url='https://github.com/armandotoledo/ibv_da_functions',
    author='Armando Toledo',
    author_email='armando.toledo.v@hotmail.com',
    # Needed to actually package something
    packages=['da_functions'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Basic tools/functions for ibvogt Data Analytics',
    # long_description=open('README.txt').read(),
)
