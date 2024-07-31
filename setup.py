from __future__ import print_function

from setuptools import setup, find_packages


setup(name='pyweaving2',
      version='0.0.1',
      description='Python Weaving Tools',
      long_description='',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.10',
          'Topic :: Multimedia :: Graphics',
      ],
      keywords='weaving handweaving wif draft pattern',
      url='https://github.com/jan-harm/pyweaving2',
      author='Jan Harm de Boer',
      author_email='jhthuis@gmail.com',
      install_requires=[
          'Pillow>=10.0.0',      # Provides PIL
     ],
      license='MIT',
      packages=find_packages(),
      test_suite='pytest.collector',
      tests_require=['pytest'],
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [console_scripts]
      pyweaving = pyweaving2.cmd:main
      """)
