# -*- coding: utf-8 -*-
"""
Este es un archivo temporal.
"""
###############################################################################
# Bibliotecas
###############################################################################
import sys
!{sys.executable} -m pip install pygam
import numpy             as np
import pandas            as pd 
import matplotlib.pyplot as plt; #%matplotlib inline
#import seaborn           as sns; sns.set()

from sklearn.ensemble         import RandomForestClassifier
from sklearn.metrics          import accuracy_score
from sklearn.model_selection  import KFold, GridSearchCV

from scipy.stats import norm, t as tstudent

import pygam
from   pygam          import LinearGAM, s, f
from   pygam.datasets import wage

import warnings
warnings.filterwarnings("ignore")

X, y = wage()
gam = LinearGAM( s(0) + s(1) + f(2) ).fit(X, y)
gam.summary()


gam = LinearGAM( s(0, n_splines=5) + s(1) + f(2) ).fit(X, y)
gam.summary()