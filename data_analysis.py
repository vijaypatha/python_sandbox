#Needed Library

import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import zscore
#Visualization Libraries
import matplotlib as mp
import seaborn as sb
#Algorithmic libraries 
#scikit-learn as sc
#statsmodels

#upload data
df = pd.read_csv("x",encoding = "ISO-8859-1")
df['mcid'].astype(str)
df.set_index('asin')
df_cplfPU_ex_ads = (df.cplf_ex_ads / df.units)
df.insert(2,"cplfpu",df_cplfPU_ex_ads)
df_cplf_ex_ads_zscore = (df.cplfpu - df.cplfpu.mean())/df.cplfpu.std()
df.insert(2, "cplfpu_zscore", df_cplf_ex_ads_zscore) 
df_cplf_ex_ads_zscore = (df.cplfpu - df.cplfpu.mean())/df.cplfpu.std()
df.insert(2, "cplfpu_zscore", df_cplf_ex_ads_zscore) 
df_neg_cplf_ex_ads_zscore = (df.cplf_ex_ads - df.cplf_ex_ads.mean())/df.cplf_ex_ads.std()
df.insert(2, "df_neg_cplf_ex_ads_zscore", df_neg_cplf_ex_ads_zscore) 
high_negativeCPLF = df.loc[df['cplfpu_zscore'] < -10]
