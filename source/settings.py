import os
import pathlib

from dotenv import load_dotenv

root = pathlib.Path(__file__).parent.parent
print(root)
try:
    load_dotenv(root / ".local.env")

except FileNotFoundError:
    load_dotenv(root / ".env")


JELLYSEERR_URL = f"{os.getenv('JELLYSEERR_URL')}:{os.getenv('JELLYSEERR_PORT')}/api/v1/"
