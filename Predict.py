#-----------Import Libraries-----------------------------------------------------------#
import streamlit as st
import joblib
import numpy as np
from numpy import random 
import time 
import pandas as pd
import cufflinks
import plotly.express as px
from streamlit.script_runner import StopException
#-----------Title/Header---------------------------------------------------------------#
st.set_page_config(page_title = "Bodyfat Percentage Calculator", page_icon = 'https://store-images.s-microsoft.com/image/apps.59154.13510798882997587.2b08aa2f-aa3f-4d80-a325-a658dbc1145a.2829662d-e5e1-4fdd-bd00-29895e686f94', layout="wide") 
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.title("Bodyfat Percentage Prediction")
st.write("""### We need some information to predict your Bodyfat Percentage""") 
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #7454DB;">
  <a class="navbar-brand" target="_blank">Youssef Sultan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Bodyfat Percentage Calculator<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/youssefsultan/" target="_blank">LinkedIn</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/YoussefSultan" target="_blank">GitHub</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
#--------------------------------------------------------------------------------------#
#-----------Load Comparison DataFrame/Model/Assign variables---------------------------# 
def load_model():
	with open('cat.pkl', 'rb') as file:
		data = joblib.load(file)
	return data
data = load_model()
a = {"model": data}
regressor = a["model"] 
df = pd.read_csv("plotfunction.csv")
dfe = pd.read_csv("empty.csv")
dfr = pd.read_csv("randomsample.csv") 
e = 0 
#--------------------------------------------------------------------------------------#
#-----------Define BodyFat Graph Functions---------------------------------------------#
def PlotbyWeight(Weight): #All Weight Classes
    fig = px.scatter_3d(df, x='BodyFat', y='Height', z='Age', color='Weight', title="Bodyfat % compared to others in all weight classes")
    with c1: 
        return st.plotly_chart(fig) 
def PlotbyWeight2(Weight): # Your Specific Weight Class Entered

    fig2 = px.scatter_3d(q, x='BodyFat', y='Height', z='Age', color='Weight', title=f"Bodyfat % compared to others in weight class of {txt}")
    
    with c1: 
        return st.plotly_chart(fig2) 
def PlotbyWeightE(e): # Empty Default Graph at Start

    fig2 = px.scatter_3d(dfe, x='BodyFat', y='Height', z='Age', color='Weight', title="Enter some values to see some results!")
    
    with c1: 
        return st.plotly_chart(fig2) 
#-----------Set Columns/Assign Inputs--------------------------------------------------#

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    all = st.button("Show all values")
with c3:
    calc = st.button("Calculate Your BodyFat Percentage") 
with c5: 
    rand = st.button("Try a random sample")
with c4:
    reset = st.button("Reset")
if all:
  PlotbyWeight(2)
  with c3:  
    Weight = st.number_input("Enter your Weight (Weight)")
    Height = st.number_input("Enter your Height (in)") 
    Neck = st.number_input("Enter your Neck measurement (cm)")
    Chest = st.number_input("Enter your Chest measurement (cm)") 
  with c4:    
    Hip = st.number_input("Enter your Hip measurement (cm)")
    Thigh = st.number_input("Enter your Thigh measurement (cm)")
    Knee = st.number_input("Enter your Knee measurement (cm)") 
    Ankle = st.number_input("Enter your Ankle measurement (cm)")
    Age = st.slider("Choose your age", 16, 81) 
  with c5: 
    Biceps = st.number_input("Enter your Biceps measurement (cm)")
    Forearm = st.number_input("Enter your Forearm measurement (cm)")
    Wrist = st.number_input("Enter your Wrist measurement (cm)")
    Abdomen = st.number_input("Enter your Waist measurement (cm)")   
else: 
  if rand:
    w, h, n, c, hi, th, kn, an, bi, fo, wr, ag, wa = dfr.sample().values.tolist()[0]  
    with c3:  
        Weight = st.number_input("Enter your Weight (Weight)", value=w)
        Height = st.number_input("Enter your Height (in)", value=h)
        Neck = st.number_input("Enter your Neck measurement (cm)", value=n)
        Chest = st.number_input("Enter your Chest measurement (cm)", value=c) 
    with c4:    
        Hip = st.number_input("Enter your Hip measurement (cm)", value=hi)
        Thigh = st.number_input("Enter your Thigh measurement (cm)", value=th)
        Knee = st.number_input("Enter your Knee measurement (cm)", value=kn) 
        Ankle = st.number_input("Enter your Ankle measurement (cm)", value=an)
        Age = st.slider("Choose your age", 16, 81, value=int(ag)) 
    with c5: 
        Biceps = st.number_input("Enter your Biceps measurement (cm)", value=bi)
        Forearm = st.number_input("Enter your Forearm measurement (cm)", value=fo)
        Wrist = st.number_input("Enter your Wrist measurement (cm)", value=wr)
        Abdomen = st.number_input("Enter your Waist measurement (cm)", value=wa)
    X = np.array([[Weight/Abdomen, Height/Abdomen, Neck/Abdomen, Chest/Abdomen, Hip/Abdomen, Thigh/Abdomen, Knee/Abdomen, Ankle/Abdomen, Biceps/Abdomen, Forearm/Abdomen, Wrist/Abdomen, Age, Abdomen]])
    X = X.astype(float)  
    percent = regressor.predict(X)
    progress_bar = st.progress(0)
    status_text = st.empty()
    if (Weight >= 125) & (Weight <= 145): 
      q = df[(df.Weight >= 125) & (df.Weight <= 145)]
      txt = "125-145"
    elif (Weight > 145) & (Weight <= 165):
      q = df[(df.Weight > 145) & (df.Weight <= 165)]
      txt = "145-165"
    elif (Weight > 165) & (Weight <= 190):
      q = df[(df.Weight > 165) & (df.Weight <= 190)]
      txt = "165-190"
    elif (Weight > 190) & (Weight <= 210): 
      q = df[(df.Weight > 190) & (df.Weight <= 210)]
      txt = "190-210"
    elif (Weight > 210) & (Weight <= 230):
      q = df[(df.Weight > 210) & (df.Weight <= 230)]
      txt = "210-230"
    elif (Weight > 230) & (Weight <= 250):
      q = df[(df.Weight > 230) & (df.Weight <= 250)]
      txt = "230-250"
    elif (Weight > 250) & (Weight <= 270): 
      q = df[(df.Weight > 250) & (df.Weight <= 270)] 
      txt = "250-270"
    PlotbyWeight2(Weight)
    for i in range(100):
      progress_bar.progress(i + 1) 
      new_rows = np.random.randn(0,15)
      status_text.text(f"Estimated Bodyfat percentage: {percent[0]:.2f}%")
      time.sleep(0.00001)   
  else:
    with c3:  
        Weight = st.number_input("Enter your Weight (Weight)")
        Height = st.number_input("Enter your Height (in)") 
        Neck = st.number_input("Enter your Neck measurement (cm)")
        Chest = st.number_input("Enter your Chest measurement (cm)") 
    with c4:    
        Hip = st.number_input("Enter your Hip measurement (cm)")
        Thigh = st.number_input("Enter your Thigh measurement (cm)")
        Knee = st.number_input("Enter your Knee measurement (cm)") 
        Ankle = st.number_input("Enter your Ankle measurement (cm)")
        Age = st.slider("Choose your age", 16, 81) 
    with c5: 
        Biceps = st.number_input("Enter your Biceps measurement (cm)")
        Forearm = st.number_input("Enter your Forearm measurement (cm)")
        Wrist = st.number_input("Enter your Wrist measurement (cm)")
        Abdomen = st.number_input("Enter your Waist measurement (cm)")
    if (Weight >= 125) & (Weight <= 145): 
      q = df[(df.Weight >= 125) & (df.Weight <= 145)]
      txt = "125-145"
    elif (Weight > 145) & (Weight <= 165):
      q = df[(df.Weight > 145) & (df.Weight <= 165)]
      txt = "145-165"
    elif (Weight > 165) & (Weight <= 190):
      q = df[(df.Weight > 165) & (df.Weight <= 190)]
      txt = "165-190"
    elif (Weight > 190) & (Weight <= 210): 
      q = df[(df.Weight > 190) & (df.Weight <= 210)]
      txt = "190-210"
    elif (Weight > 210) & (Weight <= 230):
      q = df[(df.Weight > 210) & (df.Weight <= 230)]
      txt = "210-230"
    elif (Weight > 230) & (Weight <= 250):
      q = df[(df.Weight > 230) & (df.Weight <= 250)]
      txt = "230-250"
    elif (Weight > 250) & (Weight <= 270): 
      q = df[(df.Weight > 250) & (df.Weight <= 270)] 
      txt = "250-270" 
    if calc:
      if Weight == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      elif Height == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      elif Neck == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      elif Chest == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      elif Hip == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      elif Thigh == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1)
      elif Knee == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      elif Ankle == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      elif Age == 0: 
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1)   
      elif Biceps == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1)
      elif Forearm == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1)
      elif Wrist == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1)
      elif Abdomen == 0:
        st.warning('Please Enter A Value Greater Than 0')
        PlotbyWeightE(1) 
      else:
 
        X = np.array([[Weight/Abdomen, Height/Abdomen, Neck/Abdomen, Chest/Abdomen, Hip/Abdomen, Thigh/Abdomen, Knee/Abdomen, Ankle/Abdomen, Biceps/Abdomen, Forearm/Abdomen, Wrist/Abdomen, Age, Abdomen]])
        X = X.astype(float)   
        percent = regressor.predict(X)
        progress_bar = st.progress(0)
        status_text = st.empty()
        PlotbyWeight2(Weight)
        for i in range(100):
          progress_bar.progress(i + 1)
          new_rows = np.random.randn(0,15)
          status_text.text(f"Estimated Bodyfat percentage: {percent[0]:.2f}%")
          time.sleep(0.00001)
    elif all:
      X = np.array([[Weight/Abdomen, Height/Abdomen, Neck/Abdomen, Chest/Abdomen, Hip/Abdomen, Thigh/Abdomen, Knee/Abdomen, Ankle/Abdomen, Biceps/Abdomen, Forearm/Abdomen, Wrist/Abdomen, Age, Abdomen]])
      X = X.astype(float)
      PlotbyWeight(1)
      percent = regressor.predict(X)
      progress_bar = st.progress(100)
      status_text = st.empty()
      new_rows = np.random.randn(0,15)
      status_text.text(f"Estimated Bodyfat percentage: {percent[0]:.2f}%")
      time.sleep(0.00000)   
    else:
      PlotbyWeightE(1)

