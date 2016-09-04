from setuptools import setup

setup(
      name='macs_peak_id',
      version='0.1',
      description='Small script to relate target and gene peaks.',
      long_description='README.md',
      url='http://github.com/alexdiep/macs_peak_id',
      author='Alex Diep',
      author_email='alexdiep2501@gmail.com',
      license='MIT',
      packages=['macs_peak_id'],
      install_requires=['pandas'],
      entry_points={
            'console_scripts': ['macs_peak_id=macs_peak_id.cli:main']
      },
      include_package_data=True,
      zip_safe=False
)