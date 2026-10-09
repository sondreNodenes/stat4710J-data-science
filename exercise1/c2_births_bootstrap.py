"""
C2. births.csv: mean difference + stratified bootstrap CI.

Delta = mean(birth weight | non-smoker) - mean(birth weight | smoker)

Stratified bootstrap: resample each group *separately* (with replacement,
same size as that group), so the smoker/non-smoker split in each
resample matches the original data. Repeat 2000 times to build up a
distribution of Delta, then read off the 2.5th and 97.5th percentiles
for a 95% CI.
"""
from pathlib import Path

import numpy as np
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "births.csv")

# Column names in the file use dots, e.g. "Maternal.Smoker" / "Birth.Weight"
smoker_col = "Maternal.Smoker"
weight_col = "Birth.Weight"

smoker = df.loc[df[smoker_col] == True, weight_col].to_numpy()
non_smoker = df.loc[df[smoker_col] == False, weight_col].to_numpy()

# (a) observed difference in means
delta_observed = non_smoker.mean() - smoker.mean()
print(f"n(non-smoker) = {len(non_smoker)}, n(smoker) = {len(smoker)}")
print(f"Delta (non-smoker - smoker) = {delta_observed:.4f}")

# (b) stratified bootstrap
rng = np.random.default_rng(1111)
n_boot = 2000
boot_deltas = np.empty(n_boot)

for i in range(n_boot):
    smoker_resample = rng.choice(smoker, size=len(smoker), replace=True)
    non_smoker_resample = rng.choice(non_smoker, size=len(non_smoker), replace=True)
    boot_deltas[i] = non_smoker_resample.mean() - smoker_resample.mean()

ci_low, ci_high = np.percentile(boot_deltas, [2.5, 97.5])
print(f"95% percentile CI for Delta: ({ci_low:.4f}, {ci_high:.4f})")
