import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "geopy"])

from geopy.geocoders import Nominatim

#%pip install geopy
#from geopy.geocoders import Nominatim
#geolocator = Nominatim(user_agent="claim_lat_long", timeout=5, scheme='https')
