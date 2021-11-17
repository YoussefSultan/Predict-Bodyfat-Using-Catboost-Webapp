**Body Fat Percentage Predictor**, Gathers body attributes to make a prediction on your bodyfat percentage based on previous data of recorded participants utilizing hydrostatic weighing. Additionally, the model has been deployed end to end using Streamlit, for testing and further research for applicability. 

EDA: [BodyFat_Prediction.ipynb](https://github.com/YoussefSultan/Predict-Bodyfat-Using-Catboost-Webapp/blob/main/BodyFat_Prediction.ipynb)
Deployment: [Streamlit Webapp](https://share.streamlit.io/youssefsultan/predict-bodyfat-using-catboost-webapp/main/Predict.py)
Tableau Dashboard: [Tableau Public](https://public.tableau.com/views/BodyFatCompositioninMenfromHydrostaticWeighing/DashboardABD?:language=en-US&:display_count=n&:origin=viz_share_link) or [Download](https://github.com/YoussefSultan/Predict-Bodyfat-Using-Catboost-Webapp/blob/main/BF_Analysis_Dashboard_Tableau.twb)
- Variable correlation testing
- Variable distribution analysis 
- Outlier detection and feature engineering
- Model hyperparameter tuning and training


<p align="center">
    <a href="#readme">
        <a href="https://gyazo.com/88b28e70f4de7b10d52e370795170abf"><img src="https://i.gyazo.com/88b28e70f4de7b10d52e370795170abf.gif" alt="Image from Gyazo" width="1280"/></a>
    </a>
<a href="https://gyazo.com/38c2985365461bb75917678953a6afae"><img src="https://i.gyazo.com/38c2985365461bb75917678953a6afae.gif" alt="Image from Gyazo" width="720"/></a>



## Results

![](https://github.com/YoussefSultan/Predict-Bodyfat-Using-Catboost-Webapp/blob/main/download.png)
![](https://i.gyazo.com/269a6bf9e13ae867d1af39c63811cce1.png)
- Using various learning rates, tree depths and number of trees this model's accuracy shows a positive linear relationship
- Achieves a Mean Absolute Error of 134.66 with normal distribution comparing the prediction and actual values
- CatBoost was used simply due to speed and optimization in comparison to XGBoost or LightGBM


