from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from fnmatch import fnmatch


__all__ = []

for mod_file in os.listdir(os.path.dirname(__file__)):
    if not fnmatch(mod_file, '*.py'):
        continue
    mod_name = mod_file[:-3]
    pkg = __import__(__name__, globals(), locals(), [mod_name])
    mod = getattr(pkg, mod_name)

    exported_names = getattr(mod, '__all__', [])
    for name in exported_names:
        setattr(pkg, name, getattr(mod, name))
    __all__ += exported_names
