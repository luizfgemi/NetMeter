# modules/__init__.py

from .auth import auth, setup_initial_user, verify_password
from .config import db_path
from .db import cursor, create_tables
