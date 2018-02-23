from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()



setup(name="systeminfo",
      version="0.1",
      description="Prints basic system information.",
      long_description=readme,
      url="https://github.com/MartinC20xx/systeminfo.git",
      author="Martin Casey",
      author_email="martin.casey@ucdconnect.ie",
      licence="GPL3",
      packages=find_packages(exclude=('tests', 'docs')),
      entry_points={
          "console_scripts":['comp30670_systeminfo=systeminfo.main:main']})