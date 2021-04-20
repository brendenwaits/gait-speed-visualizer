'''
This script posts dummy data values to the api for testing
'''

import requests
import random
import json

from datetime import datetime, timedelta

random.seed(datetime.now())
url = "http://localhost:8000/api/gaitmeasurements/"

for i in range(100):
    speed = round(random.uniform(.7, 1.5), 2)
    date = (datetime.now() - timedelta(days=i)).isoformat()

    x = requests.post(url, data={"speed": speed, "date": date})
    print(x)

print("Done")
