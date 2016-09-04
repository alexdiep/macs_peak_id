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
      classifiers=[
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
],
      include_package_data=True,
      zip_safe=False
)