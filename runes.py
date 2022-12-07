import re
import pandas as pd

runes = open("data/common-ioc.ioc")

for line in runes.readlines():
    print(line)