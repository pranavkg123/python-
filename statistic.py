# -*- coding: utf-8 -*-
"""statistic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e5_-8BZCJzHnVpDJ1_dVcCutJdQ9fLh6
"""

import numpy as np
from scipy import stats

before = np.array([78, 82, 85, 90, 76, 80, 78, 74])
after = np.array([85, 84, 88, 92, 79, 82, 81, 78])
mean_diff = np.mean(after - before)
t_stat, p_value = stats.ttest_1samp(after - before, 0)

print(f"Mean Difference: {mean_diff}")
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in test scores.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in test scores.")



import numpy as np
from scipy import stats
before_bmi = np.array([30.5, 32.1, 28.7, 29.9, 31.4, 30.2, 29.1, 28.4, 32.5, 30.8])
after_bmi = np.array([30.2, 32.0, 28.5, 29.8, 31.2, 30.1, 29.0, 28.3, 32.4, 30.7])
mean_diff = np.mean(after_bmi - before_bmi)
t_stat, p_value = stats.ttest_1samp(after_bmi - before_bmi, 0)
print(f"Mean Difference: {mean_diff}")
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in BMI.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in BMI.")