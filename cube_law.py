#!/usr/bin/python3
# Written by Manuel Pégourié-Gonnard in 2026. WTFPL2.

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

dataset = "big-single" if len(sys.argv) < 2 else sys.argv[1]

def to_seconds(time_str):
    t = pd.to_timedelta(time_str)
    return t.total_seconds()

df = pd.read_csv(f"{dataset}.csv", header=None)
n, t = df[0], df[1].apply(to_seconds)

# non-linear fit on actual data
def model(n, c, k):
    return c * n**k

(c_fit, k_fit), _ = curve_fit(model, n, t)
t_nl_fit = model(n, c_fit, k_fit)

# linear fit on the logs
a, b = np.polyfit(np.log(n), np.log(t), 1)
exp_b = np.exp(b)
t_lg_fit = exp_b * n**a

plt.loglog(n, t, marker="o", label=f"actual times")
plt.loglog(n, t_nl_fit, "--", label=f"non-linear fit: t = {c_fit:.2g} * n^{k_fit:.2f}")
plt.loglog(n, t_lg_fit, "--", label=f"log fit: t = {exp_b:.2g} * n^{a:.2f}")

ax = plt.gca()
ax.set_xticks(n)
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())
ax.get_xaxis().set_minor_formatter(plt.NullFormatter())
ax.set_yticks(t)
ax.get_yaxis().set_major_formatter(plt.ScalarFormatter())
ax.get_yaxis().set_minor_formatter(plt.NullFormatter())

plt.xlabel("cube size")
plt.ylabel("record time (seconds)")
plt.title(f"log-log time vs size ({dataset})")
plt.grid(True)
plt.legend()
plt.show()
