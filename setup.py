from setuptools import setup, find_packages

setup(
    name='Continuous-bandit',
    version='0.1.0',
    url='https://github.com/y-mitsui/continuous_bandit',
    packages=find_packages(),
    description='Bayesian optimizetion using gaussian process that optimized by cuda',
    install_requires=[
        "numpy >= 1.9.0",
        "scipy >= 0.14.0",
        "scikit-learn >= 0.18rc1",
    ],
)
