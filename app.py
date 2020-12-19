import streamlit as st
from model import predict

st.markdown('<style>body{text-align: center;}</style>', unsafe_allow_html=True)

# About section (sidebar)
st.sidebar.subheader('About')
st.sidebar.write('Krishi Unnati is a web application which can help you classify \
plant and crop diseases using machine learning.')

# Instructions section (sidebar)
st.sidebar.subheader('Instructions to use')
st.sidebar.write("Using the app is very simple. All you have to do is upload an \
image of the diseased plant's (or crop's) leaf and click on the Predict button. \
The app will use machine learning to predict the disease and display the result \
along with a probability percentage.")

# Information section (sidebar)
st.sidebar.subheader('More information')
st.sidebar.write('As of now, the app can detect the following 39 classes:')
st.sidebar.info('Apple - Apple scab, Apple - Black rot, Apple - Cedar apple rust, \
Apple - healthy, Background without leaves, Blueberry - healthy,  Cherry - Powdery mildew, \
Cherry - healthy, Corn - Cercospora leaf spot Gray leaf spot, Corn - Common rust, \
Corn - Northern Leaf Blight, Corn - healthy, Grape - Black rot, Grape - Esca (Black Measles), \
Grape - Leaf blight (Isariopsis Leaf Spot), Grape - healthy, Orange - Haunglongbing (Citrus greening), \
Peach - Bacterial spot, Peach - healthy, Pepper, bell - Bacterial spot, Pepper, bell - healthy, \
Potato - Early blight, Potato - Late blight, Potato - healthy, Raspberry - healthy, \
Soybean - healthy, Squash - Powdery mildew, Strawberry - Leaf scorch, Strawberry - healthy, \
Tomato - Bacterial spot, Tomato - Early blight, Tomato - Late blight, Tomato - Leaf Mold, \
Tomato - Septoria leaf spot, Tomato - Spider mites Two-spotted spider mite, Tomato - Target Spot, \
Tomato - Tomato Yellow Leaf Curl Virus, Tomato - Tomato mosaic virus, Tomato - healthy')
st.sidebar.write('We will be adding more disease classes to the app soon.')
st.sidebar.write('You can find the source code the app [here](https://github.com/prateek-senapati/krishi-unnati-streamlit).')

# Main app interface
st.title('Krishi Unnati')
st.header('A plant and crop disease detection app')
st.text('')
img = st.file_uploader(label='Upload leaf image (PNG, JPG or JPEG)', type=['png', 'jpg', 'jpeg'])
if img is not None:
    predict_button = st.button(label='Predict')
    if predict_button:
        st.text('')
        st.text('')
        st.image(image=img.read(), caption='Uploaded image')
        prediction_class, prediction_probability = predict(img)
        st.subheader('Prediction')
        st.info(f'Classification: {prediction_class}, Probability: {prediction_probability}%')
