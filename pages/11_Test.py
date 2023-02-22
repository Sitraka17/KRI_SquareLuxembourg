import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    np.random.seed(0)
    data = np.random.randn(10, 5).cumsum(axis=0)
    df = pd.DataFrame(data, columns=['Risk 1', 'Risk 2', 'Risk 3', 'Risk 4', 'Risk 5'])
    return df

def main():
    st.title('Possible Risks Evolutions')
    st.write('This graph shows the possible evolutions of different risks over time.')
    
    df = generate_data()
    st.line_chart(df)

if __name__ == '__main__':
    main()

