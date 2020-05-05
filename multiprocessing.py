import re
import os
import time
from multiprocessing import Pool


def ngrams(string, n=3):
    string = re.sub(r'[),./(]|\s\\n', r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


def dummyFunc(series):
    corrSum = 0
    feat = ""
    if df[series].dtypes in ("int64", "float64"):
        for colName in df.columns:
            if df[colName].dtypes in ("int64", "float64"):
                corr = df[series].corr(df[colName])
                corrSum += corr
    else:
        for string in df[series]:
            feat = ngrams(string)
            
    return corrSum, feat


start1 = time.time()
list(map(dummyFunc, df.columns))
end1 = time.time()
print(end1 - start1)


start = time.time()
with Pool(processes = os.cpu_count()-1) as pool:
    pool.map(dummyFunc, df.columns)
end = time.time()
print(end - start)
