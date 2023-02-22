import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generate_data():
    data = {
        'Apples': 10,
        'Bananas': 20,
        'Oranges': 30,
        'Pears': 40,
    }
    return data

def main():
    st.title('Fruit Count')
    st.write('This pie chart shows the count of some fruits.')

    data = generate_data()
    labels = list(data.keys())
    values = list(data.values())
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
