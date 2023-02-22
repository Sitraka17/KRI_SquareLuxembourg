import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mydfdata = [('France', 30), ('Holland', 55), ('Germany',99), ('Others', 43)]

mydf = pd.DataFrame(mydfdata, columns=['thing', 'count'])

mydf

mydf.plot(kind='hist', bins=50,
                     title='Distribution of View Count',
                     figsize=(15, 5))