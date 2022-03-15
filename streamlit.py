import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import webbrowser

#st.text("Context")
loaded_model = pickle.load(open('trained_model.sav','rb'))

def farmer_prediction(input):
    numpy_array = np.asarray(input)
    input = numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input)
    return prediction
  



read = st.sidebar.radio("Navigation",["Home","Crop Prediction","Disease Prediction","Weather Prediction","About us"])

if read=="Home":
    
    col1,col2=st.columns(2)
    
    with col1:
        st.title("FARMER FRIEND")
        st.success("Farming looks mighty easy when your plow is a pencil and you’re a thousand miles from the cornfield")
        st.success("“The farmer has to be an optimist or he wouldn’t still be a farmer.” – Will Rogers")
        
    with col2:
        image6 = Image.open('farmer3.jpg')
        st.image(image6, caption='')
    
    st.write("1.Seeds:Unfortunately, good quality seeds are out of reach of the majority of farmers, especially small and marginal farmersmainly because of exorbitant prices of better seeds.")
    st.write("2.Manures, Fertilizers and Biocides:Indian soils have been used for growing crops over thousands of years without caring much for replenishing.This has led to depletion and exhaustion of soils resulting in their low productivity")
    st.write("3.Lack of mechanisation: In spite of the large scale mechanisation of agriculture in some parts of the country, most of the agricultural operations in larger parts are carried on by human hand using simple and conventional tools and implements like woodenplough, sickle, etc.In spite of the large scale mechanisation of agriculture in some parts of the country, most of theagricultural operations in larger parts are carried on by human hand using simple and conventional tools and implementslike wooden plough, sickle, etc.")
    st.write("4.Agricultural Marketing:the farmers have to depend upon local traders and middlemen for the disposal of their farm produce which is sold at throw-away price.")
    st.write("5.Poor Storage Facilities:In rural areas, storage facilities are either insufficient or completely absent.")
    st.write("6.Government Schemes are yet to reach Small Farmers:most of such welfare programs and subsidies announced by both the central and state governments are yet to reach poor farmers, while big/wealthy landlords are hugely benefited.")
    
    image = Image.open('farmer.jpg')
    st.image(image, caption='')
    
    
if read=="Crop Prediction":
    
    
    
    col1,col2=st.columns(2)
    
    with col1:
        st.title("Farmer Friend:")
        st.info("“Agriculture is our wisest pursuit, because it will in the end contribute most to real wealth, good morals, and happiness.” – Thomas Jefferson")
        
        
    with col2:
        image6 = Image.open('f1.jpg')
        st.image(image6, caption='')
    
    
    
    
    
    
    #N,P,K,temperature,humidity,ph,rainfall
    
    col1,col2=st.columns(2)
    with col1:
        N = st.slider("NITROGEN",min_value=0,max_value=140,value=50,step=1)
        P = st.slider("PHASPHORAS",min_value=0,max_value=145,value=50,step=1)
        
    with col2:
        K = st.slider("POTESISUM",min_value=0,max_value=205,value=100,step=1)
        Ph = st.slider("PH VALUE",min_value=0,max_value=7,value=4,step=1)
       
    
    
    
    
    
    
    
    
    
    
   

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("temperature.")
        T = st.number_input("TEMPERATURE")

    with col2:
        st.header("humidity")
        H = st.number_input("humidity")
    with col3:
        st.header("Rainfall")
        Rain = st.number_input("Rainfall")
        
    output =''
    
    if st.button('test result'):
        output = str(farmer_prediction([N,P,K,T,H,Ph,Rain]))
        
    st.success(output)




    

if read=="Disease Prediction":
    st.header("DISEASE PREDICTION")
    st.info("UPCOMING....")
    st.write("Detection and identification of diseases in crops could be realized via both direct and indirect methods. Direct detection of diseases includes molecular and serological methods that could be used for high-throughput analysis when large numbers of samples need to be analyzed. In these methods, the disease causing pathogens such as bacteria, fungi and viruses are directly detected to provide accurate identification of the disease/pathogen. On the other hand, indirect methods identify the plant diseases through various parameters such as morphological change, temperature change, transpiration rate change and volatile organic compounds released by infected plants.")
    col1,col2=st.columns(2)
    
    with col1:
        image5 = Image.open('disease1.jpg')
        st.image(image5, caption='')
        
        
    with col2:
        image6 = Image.open('disease2.jpg')
        st.image(image6, caption='')
    
    
if read=="Weather Prediction":
    url = 'https://mausam.imd.gov.in/'

   # if st.button('Open browser'):
    webbrowser.open_new_tab(url)   
    st.header("Weather Prediction")
    col1,col2=st.columns(2)
    with col1:
       st.success("Weather In Agriculture: Accuracy Promotes Success")
       st.info("The importance of weather forecasting in agriculture reveals why farmers are so keen to get the most accurate and knowledgeable information. With multiple open-access public sources, it may seem that they can effortlessly get weather data for agriculture from any of them. However, seasoned farmland owners tend to trust reliable providers, and the main reason is the data precision that significantly helps them boost profit while reducing costs.")
        
        
    with col2:
        image7 = Image.open('weather.jpeg')
        st.image(image7, caption='')
        image8 = Image.open('weather2.jpg')
        st.image(image8, caption='')
    
    
    
    
    
    
    
if read=="About us":
    st.header("ABOUT US:")
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        st.success("TEAM LEAD")
        image2 = Image.open('shekhar.jpg')
        st.image(image2, caption='SHEKHAR CHANDEL')
        st.info("->Univ Roll No: 301402218078")
    
    with col2:
        st.error("NOTE TAKER")
        image4 = Image.open('ritika.jpg')
        st.image(image4, caption='RITIKA SAXENA')
        st.info("->Univ Roll No: 301402218070")
        
    with col3:
        st.success(" PROCEDURAL")
        image3 = Image.open('rashi.jpg')
        st.image(image3, caption='RASHI SEN')
        st.info("->Univ Roll No: 301402218072")
     
    with col4:
        st.error("CONTENT WRITER")
        image = Image.open('akansha.jpg')
        st.image(image, caption='AKANKSHA SRIVASTAVA')
        st.info("->Univ Roll No: 301402218097")
         
    
        
        

    
    
    
    
   
   
   
    
    
  
  
  




