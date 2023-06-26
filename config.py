from dotenv import load_dotenv

from os import environ
from os.path import (
    join, abspath, dirname
)

"""PATHs"""

ROOT = abspath(dirname(__file__))
CONFIG = join(ROOT, "config", ".env")
RESOURCES = join(ROOT, "resources")
USERS = join(RESOURCES, "user", "userId.json")
COGS = join(ROOT, "cogs")





"""For Discord Bot"""

load_dotenv(CONFIG)

TOKEN = environ["token"]
COLOR = 0x0