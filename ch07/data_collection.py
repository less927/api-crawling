import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_KEY = os.getenv('SEOUL_API_KEY')
print(SERVICE_KEY)
