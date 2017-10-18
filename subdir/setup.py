from setuptools import setup

setup(name='sample',
      version='0.1',
      description='Sample pypi package in a sub directory',
      url='https://github.com/snyk-fixtures/python-pypi-package-sample-subdir',
      author='anon',
      author_email='anon@example.com',
      license='MIT',
      packages=['sample'],
      zip_safe=False)
