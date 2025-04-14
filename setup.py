from setuptools import setup

setup(name='bil_name',
      version='0.0.1',
      description='Converts a 64-bit hex string to a human-readable "adj_name" name',
      url='https://github.com/blueirislabs/bil_name',
      author='Neal Jackson',
      author_email='neal@blueirislabs.com',
      license='Other/Proprietary License',
      packages=['bil_name'],
      package_data={'': ['adjs.txt', 'nouns.txt']},
      include_package_data=True,
      zip_safe=False)
