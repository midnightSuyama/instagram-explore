from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import instagram_explore

requires = ['requests']

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

setup(
    name='instagram-explore',
    version=instagram_explore.__version__,
    description='instagram scrapping module',
    long_description=open('README.rst').read(),
    url='https://github.com/midnightSuyama/instagram-explore',
    author='midnightSuyama',
    author_email='midnightSuyama@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='instagram',
    packages=find_packages(exclude=['tests*']),
    install_requires=requires,
    tests_require=['pytest', 'six'],
    cmdclass={'test': PyTest}
)
