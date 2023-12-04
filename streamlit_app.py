import streamlit
import pandas
import snowflake.connector
streamlit.title("🥣 My Parents New Healty Dinner")
streamlit.header("🥗 Breakfast menu")
streamlit.text("🐔 Omega 3 and blakberry oamlet")
streamlit.text("🥑 kale,Spnish and Rocket Smoothe")
streamlit.text("🍞Hard-boiled Free-Range Egg")

streamlit.header("Build your own fruit smoothie")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response)


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
