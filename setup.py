from setuptools import setup, find_packages

setup(
      name='macs_peak_id',
      version='0.1',
      description='Mac_peak_id analyzes *.bed and target.fa files from HOMER.',
      url='http://github.com/alexdiep/macs_peak_id',

      author='Alex Diep',
      author_email='alexdiep2501@gmail.com',
      
      license='MIT',
      
      packages=find_packages(),
      install_requires=['pandas', 'biopython'],
      
      entry_points={
            'console_scripts': 
                  ['macs_peak_id = macs_peak_id.macs_peak_id:main']
      },
      
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
      ],

       zip_safe=False,
)
