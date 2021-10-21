from .base import *

env_name = os.getenv('venv', 'local')

if env_name == 'development':
    from .development import *
elif env_name == 'production':
    from .production import *
else:
    from .development import *