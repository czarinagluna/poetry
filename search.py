import streamlit as st
import pandas as pd
import spacy
from tqdm import tqdm
from rank_bm25 import BM25Okapi

data = pd.read_csv('poems_data.csv')
file_paths = data['file_path'].tolist()

nlp = spacy.load('en_core_web_sm')

tokenized_text = [] 

for doc in tqdm(nlp.pipe(data['text'].fillna('').str.lower().values, disable=['tagger', 'parser', 'ner'])):
    tokenized = [token.text for token in doc if token.is_alpha]
    tokenized_text.append(tokenized)

bm25 = BM25Okapi(tokenized_text)

def search_poem(query, n=3):
    tokenized_query = query.lower().split(' ')
    
    results = bm25.get_top_n(tokenized_query, data['file_path'], n)
    results_list = [poem for poem in results]
    return results_list


def show_search():
    search_word = st.text_input('Search a poem', '')

    if search_word != '':
            results = search_poem(search_word)
            first_poem = results[0]
            st.image(first_poem)

            second_result = st.expander('Other')
            second_result.image(results[1])

            third_result = st.expander('More')
            third_result.image(results[2])