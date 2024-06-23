
#Importing all libraries 
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


#Markdown for the header
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.1/css/mdb.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)
st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
st.markdown("""""", unsafe_allow_html=True)



hide_streamlit_style = """
            <style>
                header{visibility:hidden;}
                .main {
                    margin-top: -20px;
                    padding-top:10px;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #800020;">
    <a class="navbar-brand" href="#"  target="_blank">FootBall  Performance Predictor</a>  
    </nav>
""",
    unsafe_allow_html=True,
)

filename = "trained_model.sav"



# A function to ask the user for inputs  for the various fields 
def process():
    st.write("Enter the player's attribute to predict their overall performance")
    col1,col2 = st.columns(2)
    with col1:
        # Input fields for user to enter data
        dribbling = st.text_input('Dribbling points')
        defending = st.text_input('Defending points')
        physic = st.text_input('Physic points')

    with col2:
        passing = st.text_input('Passing points')
        shooting = st.text_input('Shooting points')
        pace = st.text_input('Pace points')
        #loading the model from the file location .
    load = pickle.load(open(filename,'rb'))
    
    if st.button("Play"):
        input=_data=[[dribbling,defending,physic,passing,shooting,pace]]
        predict = load.predict(input)
        #the output prediction.
        st.write("overall score")
        st.markdown(f"<div class='col-md-6 card alert alert-success' style='color:black:width:70px:align-icontent:center'>{predict[0]}</div> ",unsafe_allow_html=True)
    
process()