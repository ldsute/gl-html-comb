from setuptools import setup


def readme():
      with open('README.md') as f:
            return f.read()


setup(name='glhtmlcomb',
      version='0.1',
      description='Combiner/composer/styler for GL HTML files',
      long_description=readme(),
      url='https://github.com/ldsute/glhtmlcomb',
      author='ldsute',
      author_email='ldsute@gmail.com',
      packages=['glhtmlcomb'],
      entry_points={
            'console_scripts': ['glhtmlcomb-joke=glhtmlcomb.command_line:main'],
      },
      install_requires=[
            'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)

