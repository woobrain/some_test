import numpy as np
import pandas as pd

df=pd.DataFrame(pd.read_excel(r'C:\Users\Administrator\Desktop\四川picc\助贷险流程测试数据\保费匹配表.xlsx',sheet_name='匹配表'))
print(df['汇总表'][:1:])