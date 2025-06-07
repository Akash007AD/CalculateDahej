import streamlit as st
import pandas as pd
import numpy as np
import joblib
import random

# Load model, scaler, and feature list
model = joblib.load("dahej_model_multi.pkl")
scaler = joblib.load("dahej_scaler_multi.pkl")
features = joblib.load("dahej_feature_names_multi.pkl")

st.set_page_config(page_title="Dahej Calculator 😂", page_icon="💰")
st.title("💸 Calculate My Dahej 💸")
st.write("**Apne bhavishya ke sasural se milne wali 💰daulat💰 ka andaaza lagayein!**\n\n_Thodi masti, thoda science_ 🤓")

# Input form
with st.form("input_form"):
    col1, col2 = st.columns(2)

    age = col1.slider("Age", 22, 40, 28)
    height = col2.slider("Height (cm)", 150, 200, 170)

    skin_tone = col1.selectbox("Skin Tone", ["Fair", "Wheatish", "Dark"])
    beard_rating = col2.slider("Beard Style Rating", 1, 10, 5)

    marital_status = col1.selectbox("Marital Status", ["Single", "Ready to Mingle", "Waiting for Arranged"])
    horoscope = col2.radio("Kundli match hui?", [0, 1], format_func=lambda x: "Haan" if x else "Nahi")

    edu = col1.selectbox("Education Level", ["12th Pass", "B.Tech", "MBA", "PhD"])
    job = col2.selectbox("Job", ["Unemployed", "Software Dev", "Doctor", "IAS"])

    income = col1.number_input("Monthly Income (₹)", min_value=10000, max_value=300000, value=50000, step=1000)
    location = col2.selectbox("Work Location", ["Village", "Tier 2 City", "Bangalore", "Abroad"])

    properties = col1.slider("Properties Owned", 0, 5, 1)
    vehicles = col2.slider("Vehicles Owned", 0, 3, 1)

    family_wealth = col1.selectbox("Family Wealth", ["Low", "Medium", "High"])
    parent_job = col2.selectbox("Father's Occupation", ["Farmer", "Govt Job", "Business"])

    insta_followers = col1.number_input("Instagram Followers", min_value=0, value=5000, step=100)
    verified = col2.radio("Blue Tick on Insta?", [0, 1], format_func=lambda x: "Haan" if x else "Nahi")

    cooking = col1.radio("Khaana banana aata hai?", [0, 1], format_func=lambda x: "Haan" if x else "Nahi")
    pet_lover = col2.radio("Pet Lover?", [0, 1], format_func=lambda x: "Haan" if x else "Nahi")

    submitted = st.form_submit_button("📲 Calculate Dahej!")

# Category-to-number mapping
mapping = {
    "Skin_Tone": {"Fair": 2, "Wheatish": 1, "Dark": 0},
    "Marital_Status": {"Single": 2, "Ready to Mingle": 1, "Waiting for Arranged": 0},
    "Education_Level": {"12th Pass": 0, "B.Tech": 1, "MBA": 2, "PhD": 3},
    "Job_Title": {"Unemployed": 0, "Software Dev": 1, "Doctor": 2, "IAS": 3},
    "Work_Location": {"Village": 0, "Tier 2 City": 1, "Bangalore": 2, "Abroad": 3},
    "Family_Wealth": {"Low": 0, "Medium": 1, "High": 2},
    "Parents_Job": {"Farmer": 0, "Govt Job": 1, "Business": 2}
}

# Suggestion logic
def get_suggestion(value, options):
    for limit, suggestion in options:
        if value <= limit:
            return suggestion
    return options[-1][1]

car_suggestions = [
    (50000, "Ab beta Gari bhi chahiye tumhe 😂"),
    (100000, "Used Maruti 800 👴"),
    (200000, "Second-hand Alto 🚗"),
    (400000, "Used Swift or i10 😎"),
    (600000, "New WagonR or i20 💼"),
    (1000000, "Honda City or SUV 💎"),
    (2000000, "Fortuner with bodyguards 🕴️")
]

bike_suggestions = [
    (20000, "Chetak Scooter 🛞"),
    (50000, "Hero Splendor 👴"),
    (80000, "Bajaj Pulsar 💥"),
    (120000, "Royal Enfield Bullet 🏍️"),
    (200000, "Yamaha R15 🔥"),
    (500000, "Harley Davidson 😱")
]

furniture_suggestions = [
    (10000, "2 plastic chairs & 1 table 🪑"),
    (20000, "Sofa set (local) 🛋️"),
    (40000, "Double bed + cupboard 🛏️"),
    (70000, "Designer furniture from Pepperfry 💼"),
    (100000, "Italian modular furniture 😍")
]

foreign_trip_suggestions = [
    (50000, "Trip to Darjeeling 💑"),
    (100000, "Goa trip ...Maze kar lena🏖️"),
    (300000, "Thailand trip (all-inclusive 🛫)"),
    (700000, "Dubai honeymoon package 💑"),
    (1000000, "Europe 15-day tour 💶"),
    (1500000, "USA + Europe + Bali extravaganza ✈️")
]

property_suggestions = [
    (20000, "Khet mein ek jhopdi 🌾"),
    (50000, "Gaon mein ek plot jisme ghaas uga hai 🏡"),
    (1000000, "1BHK flat outskirts of Tier-3 city 🏠"),
    (3000000, "1BHK apartment in Tier-2 city 🏙️"),
    (6000000, "2BHK flat with balcony in Tier-1 city 🌇"),
    (10000000, "Land in prime location or duplex in suburbs 🏘️"),
    (20000000, "Bungalow with parking and angry uncle neighbor 🏡🚗"),
    (50000000, "Villa with garden, dog, and CCTV cameras 🐕🌴📹")
]

if submitted:
    input_dict = {
        "Age": age,
        "Height_cm": height,
        "Skin_Tone": mapping["Skin_Tone"][skin_tone],
        "Beard_Style_Rating": beard_rating,
        "Marital_Status": mapping["Marital_Status"][marital_status],
        "Horoscope_Match": horoscope,
        "Education_Level": mapping["Education_Level"][edu],
        "Job_Title": mapping["Job_Title"][job],
        "Monthly_Income": income,
        "Work_Location": mapping["Work_Location"][location],
        "Properties_Owned": properties,
        "Vehicles_Owned": vehicles,
        "Family_Wealth": mapping["Family_Wealth"][family_wealth],
        "Parents_Job": mapping["Parents_Job"][parent_job],
        "Instagram_Followers": insta_followers,
        "Verified": verified,
        "Cooking_Skills": cooking,
        "Pet_Lover": pet_lover
    }

    input_df = pd.DataFrame([input_dict])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    money, property_value, bike, car, furniture, gold_cash = prediction
    total = sum(prediction)

    # Logical suggestions
    car_name = get_suggestion(car, car_suggestions)
    bike_name = get_suggestion(bike, bike_suggestions)
    furniture_name = get_suggestion(furniture, furniture_suggestions)
    trip_name = get_suggestion(total, foreign_trip_suggestions)
    property_name = get_suggestion(property_value, property_suggestions)
    # Display
    st.success("💍 Estimated Dahej Breakdown:")
    st.markdown(f"- 💵 **Cash:** ₹{int(money):,}")
    st.markdown(f"- 🏠 **Property:**  →  **{property_name}**")
    st.markdown(f"- 🏍️ **Bike:** →  **{bike_name}**")
    st.markdown(f"- 🚗 **Car:** → **{car_name}**")
    st.markdown(f"- 🛋️ **Furniture:** →  **{furniture_name}**")
    st.markdown(f"- 💰 **Gold & Gifts:** ₹{int(gold_cash):,}")

    st.markdown(f"✈️ **Bonus Prediction:** _Shaadi ke baad honeymoon trip to_ **{trip_name}**")

    fun_comments = [
        "IAS ho? Helicopter le jaane ka plan hai kya? 🚁",
        "Software dev ho? Dahej mein GitHub stars bhi count ho rahe hain kya? 💻",
        "MBA kar liya? Lagta hai MBA fees ka return aa gaya! 💼",
        "PhD ho? Dulhan ko thesis sunani padegi kya? 📚",
        "Verified Insta? Shaadi reel viral hogi! 📸",
        "Beard 10? Dulhan ko dikh rahi hai Ranveer Singh! 🧔‍♂️",
        "Cooking nahi aata? Microwave aur Swiggy subscription pakka! 🍕",
        "Pet lover ho? Dahej mein cat bhi aayegi! 🐈",
        "Papa businessman hain? Dahej ke truck ready hain 🚚"
    ]

    st.info(f"🧠 **AI ki Advice:**\nTotal dahej: ₹{int(total):,} 💰\n\n{random.choice(fun_comments)}")
