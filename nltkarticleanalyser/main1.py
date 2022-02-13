from Api_test import *
from LanguageProcessor import *

coinname = input('Enter Coin name')

print(informationgather(coinname)[0][0])

for i in range(5):
    title = [informationgather(coinname)[0][i]]
    desc= informationgather(coinname)[1][i]
    sentimentanalysis(title, desc)

