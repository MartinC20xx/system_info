from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Prints basic system information.",
      url="",
      author="Martin Casey",
      author_email="martin.casey@ucdconnect.ie",
      licence="GPL3",
      packages=["systeminfo"],
      entry_points={
          "console_scripts":['comp30670_systeminfo=systeminfo.main:main']})