import requests
import pandas as pd
import sklearn.datasets as ds

d = ds.load_iris(as_frame=True)

r = requests.post("http://127.0.0.1:5000/computemean/",json = d.data.to_json(orient = "index"))

print(r.text)