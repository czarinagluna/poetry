import streamlit as st
import pandas as pd
from streamlit_image_select import image_select
from search import show_search

st.title('Poems')

data = pd.read_csv('poems_data.csv')
file_paths = data['file_path'].tolist()

page = st.sidebar.selectbox("Poems", ("Gallery", "Search"))

if page=="Gallery":
    col1, col2 = st.columns(2)

    img = image_select(
        label="Pick a poem",
        images=file_paths,
        use_container_width=False,
        return_value="index"
    )

    idx = img

    col1.image(data.loc[idx, 'file_path'])

if page=="Search":
    show_search()