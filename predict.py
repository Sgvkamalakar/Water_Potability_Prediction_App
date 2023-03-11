import gradio as gr
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 

df=pd.read_csv('../water_potability.csv')
for i in ['ph','Trihalomethanes','Sulfate']:
    missing1 = df.query('Potability == 0')[i][df[i].isna()].index
    df.loc[missing1,i] = df.query('Potability == 0')[i][df[i].notna()].mean()
    missing2 = df.query('Potability == 1')[i][df[i].isna()].index
    df.loc[missing2,i] = df.query('Potability == 1')[i][df[i].notna()].mean()
    
dataInp=df.drop('Potability',axis=1)
dataOp=df['Potability']
X_train,X_test,y_train,y_test=train_test_split(dataInp,dataOp,test_size=0.25,random_state=42)
model= RandomForestClassifier()
model.fit(X_train,y_train)


inputs = [
    gr.inputs.Number(label='ph', default=6.5),
    gr.inputs.Number(label='Hardness', default=1),
    gr.inputs.Number(label='Solids', default=500),
    gr.inputs.Number(label='Chloramines', default=4),
    gr.inputs.Number(label='Sulfate', default=250),
    gr.inputs.Number(label='Conductivity', default=800),
    gr.inputs.Number(label='Organic_Carbon', default=2),
    gr.inputs.Number(label='Trihalomethanes', default=80),
    gr.inputs.Number(label='Turbidity', default=5)
]

outputs = [
    gr.outputs.Label(label="Potability"),
    gr.outputs.Image(type='pil',label="Image")
]


def predict_water_quality(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_Carbon, Trihalomethanes, Turbidity):
    
    try:    
        data=pd.DataFrame({'ph':[ph],'Hardness':[Hardness],'Solids':[Solids],
                    'Chloramines':[Chloramines],'Sulfate':[Sulfate],'Conductivity':[Conductivity],
                    'Organic_carbon':[Organic_Carbon],'Trihalomethanes':[Trihalomethanes],'Turbidity':[Turbidity]})
        X_new=data[['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity']]
        prediction = model.predict(X_new)
        potable_water = Image.open("../Potable water.jpg")
        non_potable_water = Image.open("../Non potable water.jpg")
    
        if prediction== 1:
            image = potable_water
        else:
            image = non_potable_water
        if prediction==0:
            print('Non Potable water')
            return 'Non Potable water',image
        else:
            print('Potable water')
            return 'Potable water',image   
         
    except Exception as e:
        return (e)    

app = gr.Interface(fn=predict_water_quality,inputs=inputs, outputs=outputs,description='Water quality is a crucial aspect of public health, and the potability of water samples is a significant concern for people worldwide. Predicting whether a water sample is potable or not is a critical task that can be accomplished through the use of machine learning techniques. \n One approach to predicting water potability is to use a Random Forest Classifier model. The model can take in various features of the water sample, such as pH, hardness, solid content, turbidity, sulfate content, trihalomethanes, conductivity, and organic carbon content, as input. Each of these features is a potential contributor to water potability.', css="footer {visibility: hidden}", title='Water Potability Prediction')
app.launch(share=True)

