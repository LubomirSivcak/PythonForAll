import matplotlib.pyplot as plt
import numpy as np

print("arange", np.arange(1.1,10,2.1))
print("linspace", np.linspace(1.1,10,4))
print("",np.array([[1,2], [4,5]]))

import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df.head())