import json

import matplotlib.pyplot as plt

for split in ["train", 'test']:
  for cat_type in ["major", "minor"]:
    for data in ['prime','major', 'abs_cat']:
      my_dict = json.load(open("freqs/"+"_".join([split, cat_type, data])+".txt"))
      sorted_dict = dict(sorted(my_dict.items()))
      exec('{} = sorted_dict'.format("_".join([split, cat_type, data])))
      x, y = sorted_dict.keys(), sorted_dict.values()
      plt.figure(figsize=(40,15))
      plt.xticks(rotation=90)
      plt.bar(x, y)
      plt.savefig("freq_figs/"+"_".join([split, cat_type, data])+".png")

