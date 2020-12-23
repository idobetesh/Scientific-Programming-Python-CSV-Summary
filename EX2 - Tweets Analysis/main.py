import numpy as np
import re
import csv

web = re.compile(r'(https?:{1}\/{2}(www\.|[a-zA-Z])+\.com)')
# https?:{1}\/{2}(www\.|[a-zA-Z]+)+\.com

btc = re.compile(r'#bitcoin|#btc')


def summary(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if btc.search(dict(row)['text'].lower()) is not None:
                print("===========================", dict(row)['text'])
            if web.search(dict(row)['text']) is not None:
                print("******************",dict(row)['text'])
            

summary("t.csv")
# summary("tweets_small_data.csv")
