import streamlit as st
import pandas as pd
import pickle
from sklearn.datasets import load_diabetes
# Load the pickled model


st.title('Diabetes Prediction App')

model_lr = pickle.load(open('models/model_lr.pkl', 'rb'))
model_en = pickle.load(open('models/model_elastic.pkl', 'rb'))
model_ridge = pickle.load(open('models/model_ridge.pkl', 'rb'))

#load the dataset
diab = load_diabetes()

X = pd.DataFrame(diab.data, columns=diab.feature_names)

user_input  = {}

for col in X.columns:
    user_input[col] = st.slider(col,X[col].min(),X[col].max())

df = pd.DataFrame(user_input,index=[0])

st.write(df)

models = {
    'Linear Regression': model_lr,
    'Elastic Net': model_en,
    'Ridge': model_ridge
}

selected_model = st.selectbox('Select Model',('Linear Regression','Elastic Net','Ridge'))
st.write(f'You selected {selected_model}')

if st.button('Predict'):
    pred_lr = models[selected_model].predict(df)[0]
    st.write(f"Predicted gulcose level is {pred_lr}")



