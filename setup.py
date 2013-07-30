from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='rhessysworkflows',
      version='1.1',
      description='Libraries and command-line scripts for performing RHESSys data preparation workflows.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Topic :: Scientific/Engineering :: GIS'        
      ],
      url='https://github.com/selimnairb/RHESSysWorkflows',
      author='Brian Miles',
      author_email='brian_miles@unc.edu',
      license='BSD',
      packages=['rhessysworkflows',
                'rhessysworkflows.tests'
                ],
      install_requires=[
        'ecohydrolib==1.1'
      ],
      scripts=['bin/CreateFlowtable.py',
               'bin/CreateGRASSLocationFromDEM.py',
               'bin/CreateWorldfile.py',
               'bin/DelineateWatershed.py',
               'bin/GenerateBaseStationMap.py',
               'bin/GenerateCustomSoilDefinitions.py',
               'bin/GenerateLandcoverMaps.py',
               'bin/GeneratePatchMap.py',
               'bin/GenerateSoilTextureMap.py',
               'bin/GenerateWorldTemplate.py',
               'bin/ImportClimateData.py',
               'bin/ImportRasterMapIntoGRASS.py',
               'bin/ImportRHESSysSource.py',
               'bin/RegisterCustomSoilReclassRules.py',
               'bin/RegisterLandcoverReclassRules.py',
               'bin/RunLAIRead.py'
      ],
      data_files=[('rhessysworkflows/etc/NLCD2006', ['etc/NLCD2006/impervious.rule',
                           'etc/NLCD2006/landuse.rule',
                           'etc/NLCD2006/road.rule',
                           'etc/NLCD2006/stratum.rule'] )
                  ],
                 
      zip_safe=False)
