from setuptools import setup
import versioneer

#Dependancy lists maintained here and in tox.ini
sp_install_requires = [
#  'stomp.py==6.0.0'
]
sp_tests_require = [
  'nose==1.3.7',
  'python_Testing_Utilities==0.1.5'
]

all_require = sp_install_requires + sp_tests_require

setup(name='EllucianEthosPythonClient',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Python package which provides Ellucian Ethos Client',
      url='https://https://github.com/rmetcalf9/EllucainEthosPythonClient',
      author='Robert Metcalf',
      author_email='rmetcalf9@googlemail.com',
      license='MIT',
      packages=['EllucainEthosPythonClient'],
      zip_safe=False,
      install_requires=sp_install_requires,
      tests_require=sp_tests_require,
      include_package_data=True)
