import py2exe
from distutils.core import setup

import sys
sys.setrecursionlimit(5000)

# these .py modules will be converted to .pyo and included in the .exe
sys.argv.append("py2exe")
sys.argv.append("-q")

setup(
  name='src',
  packages=['src', 'src.Misc', 'src.ProblemSpecifications', 'src.Readers', 'src.Writers'],
  package_dir={'src': '', 'src.Misc': 'Misc', 'src.ProblemSpecifications': 'ProblemSpecifications', 'src.Readers': 'Readers', 'src.Writers': 'Writers'},
  package_data={'project': ['Misc/*', 'ProblemsSpecifications/*', 'Readers/*', 'Writers/*']},
  options = {"py2exe": {"compressed": 1,
                        "optimize": 2,
                        "ascii": 1,
                        "bundle_files": 1}},
  zipfile = None,
  console = [{"script": 'Main.py'}],
  exclude = ['os']
)
