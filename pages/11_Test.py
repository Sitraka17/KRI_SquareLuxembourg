import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))


import pandas as pd
data = {'Industry Code': ['A', 'C', 'D', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'Q'],
        'Industry Description': ['Agriculture, Forestry And Fishing', 'Manufacturing', 'Electricity, Gas, Steam And Air Conditioning Supply', 'Construction', 'Wholesale And Retail Trade; Repair Of Motor Vehicles And.', 'Transportation And Storage', 'Information And Communication', 'Financial And insurance Activities', 'Real Estate Activities', 'Professional, Scientific And Technical Activities', 'Administrative And Support Service Activities', 'Human Health And']}
df = pd.DataFrame(data)

print(df)





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