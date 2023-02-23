import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)







#y = np.array([35, 25, 25, 15])
#plt.pie(y)
#plt.show() 
#st.pie_chart(y) C DE LA MERDEEEEEEEEEEEEEE

#mydfdata = [('France', 30), ('Holland', 55), ('Germany',99), ('Others', 43)]
#mydf = pd.DataFrame(mydfdata, columns=['thing', 'count'])
#mydf
#mydf.plot(kind='hist', bins=50,
#                     title='Distribution of View Count',
#                     figsize=(15, 5))