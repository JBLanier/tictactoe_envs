from setuptools import setup

setup(
   name='tictactoe',
   version='1.0',
   description='tictactoe RL envs',
   author='J.B. Lanier',
   author_email='johnblanier@gmail.com',
   packages=['tictactoe'],  #same as name
   install_requires=['numpy', 'scipy', 'dill', 'spacetimerl'], #external packages as dependencies
)