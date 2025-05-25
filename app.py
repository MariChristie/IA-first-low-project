import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)


st.title("Predicting the cost of a pizza")
st.divider()

diametro = st.number_input("Type the diameter of a pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"The cost of the pizza within a diameter of {diametro:.2f} is of R${preco_previsto:.2f}.")