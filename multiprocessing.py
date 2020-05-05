import re
import os
import time
from multiprocessing import Pool
from multiprocessing import Process


def ngrams(string, n=3):
    string = re.sub(r'[),./(]|\s\\n', r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


def dummyFunc(series, masterDict):
    
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

    masterDict[series] = feat[:20]


from multiprocessing import Process, Manager

if __name__ == '__main__':
    manager = Manager()
    
    d = manager.dict()

    jobs = []
    for i in range(df.shape[1]):
        p = Process(target=dummyFunc, args=(df.columns[i], d))
        jobs.append(p)
        p.start()

    for i in range(df.shape[1]):
        jobs[i].join()

    print("master", d)
