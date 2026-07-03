import numpy as np
import pandas as pd

confirmed = pd.read_csv('datasets/time_series_covid19_confirmed_global.csv') ### data in wide format
death = pd.read_csv('datasets/time_series_covid19_deaths_global.csv') ### data in wide format