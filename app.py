import streamlit as st
from model import get_laptop_names, get_laptop_index, recommend_laptops_by_index

# Page config
st.set_page_config(page_title="Laptop Recommender", layout="centered")
st.title("💻 Laptop Recommender System")

# Dropdown for laptop selection
laptop_list = get_laptop_names()
selected_laptop = st.selectbox("Select a Laptop Model", laptop_list)

# Recommend button
if st.button("Recommend"):
    try:
        index = get_laptop_index(selected_laptop)
        recommendations = recommend_laptops_by_index(index)
        
        st.subheader("Recommended Laptops:")
        st.dataframe(recommendations.reset_index(drop=True))
    except Exception as e:
        st.error(f"Oops! Something went wrong:\n{e}")
