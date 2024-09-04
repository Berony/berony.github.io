import pandas as pd
import time

#def 로 정의 되는 Const 값
TARGET_FILE = lambda : "WIPS_Sample.xlsx"
TARGET_SHEET_INDEX = lambda : 0

pre = time.time()
exl = pd.read_excel(TARGET_FILE())
aff = time.time()
print(f"Time : {aff - pre}")

# exl.replace(",","[$C]",regex=True)
# print(f"replaced , to [$C]")

exl.to_csv("WIPS_Sample.csv", encoding='utf-8-sig',index=False)