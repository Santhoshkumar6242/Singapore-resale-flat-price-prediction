import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image

# Function for map the town.
def town_mapping(town_map):
    if town_map == 'ANG MO KIO':
        town_1 = int(0)
    elif town_map == 'BEDOK':
        town_1 = int(1)
    elif town_map == 'BISHAN':
        town_1 = int(2)
    elif town_map == 'BUKIT BATOK':
        town_1 = int(3)
    elif town_map == 'BUKIT MERAH':
        town_1 = int(4)
    elif town_map == 'BUKIT PANJANG':
        town_1 = int(5)
    elif town_map == 'BUKIT TIMAH':
        town_1 = int(6)
    elif town_map == 'CENTRAL AREA':
        town_1 = int(7)
    elif town_map == 'CHOA CHU KANG':
        town_1 = int(8)
    elif town_map == 'CLEMENTI':
        town_1 = int(9)
    elif town_map == 'GEYLANG':
        town_1 = int(10)

    elif town_map == 'HOUGANG':
        town_1 = int(11)
    elif town_map == 'JURONG EAST':
        town_1 = int(12)
    elif town_map == 'JURONG WEST':
        town_1 = int(13)
    elif town_map == 'KALLANG/WHAMPOA':
        town_1 = int(14)
    elif town_map == 'MARINE PARADE':
        town_1 = int(15)
    elif town_map == 'PASIR RIS':
        town_1 = int(16)
    elif town_map == 'PUNGGOL':
        town_1 = int(17)
    elif town_map == 'QUEENSTOWN':
        town_1 = int(18)
    elif town_map == 'SEMBAWANG':
        town_1 = int(19)
    elif town_map == 'SENGKANG':
        town_1 = int(20)

    elif town_map == 'SERANGOON':
        town_1 = int(21)
    elif town_map == 'TAMPINES':
        town_1 = int(22)
    elif town_map == 'TOA PAYOH':
        town_1 = int(23)
    elif town_map == 'WOODLANDS':
        town_1 = int(24)
    elif town_map == 'YISHUN':
        town_1 = int(25)

        return town_1

# Function for map the flat type.
    
def flat_type_mapping(flt_type):

    
    if flt_type == '3 ROOM':
        flat_type_1 = int(2)
    elif flt_type == '4 ROOM':
        flat_type_1 = int(3)
    if flt_type == '5 ROOM':
        flat_type_1 = int(4)
    if flt_type == '2 ROOM':
        flat_type_1 = int(1)
    if flt_type == 'EXECUTIVE':
        flat_type_1 = int(5)
    if flt_type == '1 ROOM':
        flat_type_1 = int(0)
    if flt_type == 'MULTI-GENERATION':
        flat_type_1 = int(6)

        return flat_type_1
    
# Function for map the flat model.    
def flat_model_mapping(fl_m):

    if fl_m == 'Improved':
        flat_model_1= int(5)
    elif fl_m == 'New Generation':
        flat_model_1= int(12)
        
    elif fl_m == 'Model A':
        flat_model_1= int(8)
    elif fl_m == 'Standard':
        flat_model_1= int(17)
    elif fl_m == 'Simplified':
        flat_model_1= int(16)
    elif fl_m == 'Premium Apartment':
        flat_model_1= int(13)
    elif fl_m == 'Maisonette':
        flat_model_1= int(7)

    elif fl_m == 'Apartment':
        flat_model_1= int(3)
    elif fl_m == 'Model A2':
        flat_model_1= int(10)
    elif fl_m == 'Type S1':
        flat_model_1= int(19)
    elif fl_m == 'Type S2':
        flat_model_1= int(20)
    elif fl_m == 'Adjoined flat':
        flat_model_1= int(2)

    elif fl_m == 'Terrace':
        flat_model_1= int(18)
    elif fl_m == 'DBSS':
        flat_model_1= int(4)
    elif fl_m == 'Model A-Maisonette':
        flat_model_1= int(9)
    elif fl_m == 'Premium Maisonette':
        flat_model_1= int(15)
    elif fl_m == 'Multi Generation':
        flat_model_1= int(11)

    elif fl_m == 'Premium Apartment Loft':
        flat_model_1= int(14)
    elif fl_m == 'Improved-Maisonette':
        flat_model_1= int(6)
    elif fl_m == '2-room':
        flat_model_1= int(0)
    elif fl_m == '3Gen':
        flat_model_1= int(1)

    return flat_model_1

# Function for price prediction.
def price_predict(year,town,flat_type,flr_area_sqm,flat_model,stry_start,stry_end,re_les_year,re_les_month,les_coms_dt):

    year_1 = int(year)
    town_1 = town_mapping(town)
    flat_type_1 = flat_type_mapping(flat_type)
    flr_area_sqm_1 = int(flr_area_sqm)
    flat_model_1 = flat_model_mapping(flat_model)
    stry_start_1=np.log(int(stry_start))
    stry_end_1=np.log(int(stry_end))
    re_les_year_1=int(re_les_year)
    re_les_month_1=int(re_les_month)
    les_coms_dt_1=int(les_coms_dt)

    with open("ResaleFlatPricesPrediction_model_1.pkl","rb") as f1:
     regg_model=pickle.load(f1)

    user_data=np.array([[year_1,town_1,flat_type_1,flr_area_sqm_1,flat_model_1,
                         stry_start_1,stry_end_1,re_les_year_1,re_les_month_1,les_coms_dt_1]])
    y_pred_1=regg_model.predict(user_data)
    resale_price=np.exp(y_pred_1[0])

    return round(resale_price)



# Streamlit page
st.set_page_config(layout='wide')


st.title('Singapore Resale Flat Resale Price Prediction')
st.write(' ')

with st.sidebar:

    select = option_menu("Main menu", ['Home', 'Price Prediction', 'About'])

if select == 'Home':
    img=Image.open(r"C:\Users\Santhosh\Desktop\CapstoneProject\Capstone\Resale price prediction\1_b_LyTntm37G9NmbB-EUWvg.jpg")
    st.image(img)

    st.write('''Singapore flats, also known as Housing and Development
            Board (HDB) flats, are public housing units built and managed
            by the Housing and Development Board of Singapore.
            These flats play a significant role in providing affordable
            housing to the residents of Singapore.
            Here are some key points about Singapore flats:''')
    
    st.header(":green[Government Initiative:]")
    st.write(''' The construction and management of Singapore flats are 
            part of the government's comprehensive public housing program.
            The Housing and Development Board (HDB) is the main government 
            body responsible for this program.''')
    
    st.header(":green[Affordability:]")
    st.write('''Singapore flats are designed to be affordable for the majority
            of Singaporean residents. The government provides various schemes 
            and subsidies to make homeownership more accessible to citizens.''')

    st.header(":green[Renovation Restrictions:]")
    st.write('''Residents of Singapore flats are subject to certain restrictions 
            when it comes to renovating their units. This is to maintain the 
            uniformity and structural integrity of the buildings.''')
    
    st.header(":green[Resale Market]")
    st.write('''There is an active resale market for Singapore flats, where owners
            can sell their units to other eligible buyers. The resale price of a 
            flat is influenced by factors such as location, size, age, and lease
            remaining.''') 
    
if select == 'Price Prediction':
    col1,col2=st.columns(2)
    
    with col1:

        year= st.selectbox("Select the Year",["2015", "2016", "2017", "2018", "2019", "2020", "2021",
                            "2022", "2023", "2024"])
        
        town= st.selectbox("Select the Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        
        flat_type= st.selectbox("Select the Flat Type", ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
                                                        'MULTI-GENERATION'])
        
        flr_area_sqm= st.number_input("Enter the Value of Floor Area sqm (Min: 31 / Max: 280")

        flat_model= st.selectbox("Select the Flat Model", ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
                                                        'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
                                                        'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
                                                        'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen'])

    with col2:

        stry_start= st.number_input("Enter the Value of Storey Start")

        stry_end= st.number_input("Enter the Value of Storey End")

        re_les_year= st.number_input("Enter the Value of Remaining Lease Year (Min: 42 / Max: 97)")

        re_les_month= st.number_input("Enter the Value of Remaining Lease Month (Min: 0 / Max: 11)")
        
        les_coms_dt= st.selectbox("Select the Lease_Commence_Date", [str(i) for i in range(1966,2023)])

        button= st.button("Predict the Price", use_container_width= True)

    if button:
        
        pre_price= price_predict(year, town, flat_type, flr_area_sqm, flat_model,
                        stry_start, stry_end, re_les_year, re_les_month, les_coms_dt)

        st.write("## :red[**The Predicted Price is :**]",pre_price)

if select == 'About':
    st.header(":blue[Data Collection and Preprocessing:]")
    st.write("Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date. Preprocess the data to clean and structure it for machine learning.")

    st.header(":blue[Feature Engineering:]")
    st.write("Extract relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date. Create any additional features that may enhance prediction accuracy.")
    
    st.header(":blue[Model Selection and Training:]")
    st.write("Choose an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests). Train the model on the historical data, using a portion of the dataset for training.")

    st.header(":blue[Model Evaluation:]")
    st.write("Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) and R2 Score.")

    st.header(":blue[Streamlit Web Application:]")
    st.write("Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.). Utilize the trained machine learning model to predict the resale price based on user inputs.")

    st.header(":blue[Deployment on Render:]")
    st.write("Deploy the Streamlit application on the Render platform to make it accessible to users over the internet.")
    
    st.header(":blue[Testing and Validation:]")
    st.write("Thoroughly test the deployed application to ensure it functions correctly and provides accurate predictions.")

