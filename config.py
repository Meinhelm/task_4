from dotenv import load_dotenv
import os
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
URL_Sport = os.getenv("URL_Sport")
URL_Science = os.getenv("URL_Science")
URL_Political = os.getenv("URL_Political")
URL_Weather = os.getenv("URL_Weather")
URL_All= os.getenv("URL_All")