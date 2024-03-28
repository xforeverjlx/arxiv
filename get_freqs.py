import json
from collections import Counter

import numpy as np
import pandas as pd

json_file = "train_minor_cats_full.json"
output_file_prefix = "train_minor_"

cats = {}
idx = 0
chunksize = 10 ** 4
prime_freqs = Counter({})
major_freqs = Counter({})
abs_cat_freqs = Counter({})

for chunk in pd.read_json(json_file, lines=True, chunksize=chunksize):
  prime_freqs = prime_freqs + Counter(dict(chunk['prime_category'].value_counts()))
  major_freqs = major_freqs + Counter(dict(chunk['major_category'].value_counts()))
  wrds = chunk['abs_categories'].str.split()
  abs_cat_freqs = abs_cat_freqs + Counter(dict(pd.Series([word for sublist in wrds for word in sublist]).value_counts()))
  print(idx)
  idx += 1

prime_freqs = dict(prime_freqs)
major_freqs = dict(major_freqs)
abs_cat_freqs = dict(abs_cat_freqs)

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

for t in ['prime', 'major', 'abs_cat']:
  with open("freqs/"+output_file_prefix+t+".txt", "w") as f:
    exec("f.write(json.dumps({}_freqs, cls=NpEncoder))".format(t))