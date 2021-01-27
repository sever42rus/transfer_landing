from .base import *

try:
    from .local import *
except ModuleNotFoundError:
    print('No local settings found')
