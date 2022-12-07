import re
import pandas as pd

pinout = pd.read_csv("data/pinout.csv")

for index, row in pinout.iterrows():
    pin_name = row["Name"]
    alternate_function = row["Signal"]
    alt_functions = list(row[4:])

    if not re.search(r"^P[A-H]\d\d?$", pin_name): continue 

    if alt_functions.find(alternate_function):
        print(f"Pin {pin_name}(GPIO{pin_name[1]}, GPIO_Pin::PIN_{pin_name[2:]}, {af})")
    else:
        print(f"Pin {pin_name}(GPIO{pin_name[1]}, GPIO_Pin::PIN_{pin_name[2:]})")

