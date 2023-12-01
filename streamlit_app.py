import streamlit
import pandas
streamlit.title("🥣 My Parents New Healty Dinner")
streamlit.header("🥗 Breakfast menu")
streamlit.text("🐔 Omega 3 and blakberry oamlet")
streamlit.text("🥑 kale,Spnish and Rocket Smoothe")
streamlit.text("🍞Hard-boiled Free-Range Egg")

streamlit.header("Build your own fruit smoothie")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
