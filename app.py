import streamlit as st
import pickle


model = pickle.load(open("model.pkl", "rb"))

st.title("House Price Prediction")
ms_subclass = st.number_input("MS SubClass")

ms_zoning = st.number_input("MS Zoning")

lot_area = st.number_input("Lot Area")

neighborhood = st.number_input("Neighborhood")

overall_qual = st.number_input("Overall Qual")

year_built = st.number_input("Year Built")

gr_liv_area = st.number_input("Gr Liv Area")

bsmt_full_bath = st.number_input("Bsmt Full Bath")

full_bath = st.number_input("Full Bath")

bedroom = st.number_input("Bedroom AbvGr")

garage_cars = st.number_input("Garage Cars")

garage_area = st.number_input("Garage Area")
if st.button("Predict Price"):

    prediction = model.predict([[
        ms_subclass,
        ms_zoning,
        lot_area,
        neighborhood,
        overall_qual,
        year_built,
        gr_liv_area,
        bsmt_full_bath,
        full_bath,
        bedroom,
        garage_cars,
        garage_area
    ]])

   st.success(f"🏠 Predicted House Price: ₹ {prediction[0]:,.0f}")