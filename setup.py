from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    licence = f.read()


setup(name="systeminfo",
      version="0.1",
      description="Prints basic system information.",
      long_description=readme,
      url="https://github.com/MartinC20xx/systeminfo.git",
      author="Martin Casey",
      author_email="martin.casey@ucdconnect.ie",
      licence=licence,
      packages=["systeminfo"],
      entry_points={
          "console_scripts":['comp30670_systeminfo=systeminfo.main:main']})