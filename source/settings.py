import os

from dotenv import load_dotenv


load_dotenv()

JELLYSEERR_URL = f"{os.getenv('JELLYSEERR_URL')}:{os.getenv('JELLYSEERR_PORT')}/api/v1/"