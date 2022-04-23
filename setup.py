from setuptools import setup


packages = [
    'pynpawn',
    'pynpawn.Mouse',
    'pynpawn.GUI',
]

readme = ''
with open('README.md') as f:
    readme = f.read()
setup(name='pynpawn',
      author='Xvaz_royal',
      url='https://github.com/Xvazroyal/pynpawn',
     
      version= 1.0,
      packages=packages,
      license='MIT',
      description='best tool you need for basic development',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      
      python_requires='3.10.2',
     
)