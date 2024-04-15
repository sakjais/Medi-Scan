import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# loading the saved models

breastCancer_model = pickle.load(open('saved models/breastCancer_model.sav', 'rb'))

Cardiovascular_disease_model = pickle.load(open('saved models/cardiovascular_disease_model.sav','rb'))

pcos_model = pickle.load(open('saved models/pcos_model.sav', 'rb'))

symptom_model = pickle.load(open('saved models/symptom_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    languages = ['English','हिंदी']
    lang = st.selectbox('Select Language:', languages)
    if lang=='English':
        selected = option_menu('Multiple Disease Prediction System',
                            
                            ['Home',
                            'PCOS Prediction',
                            'Breast Cancer Prediction',
                            'Cardiovascular Disease Prediction',
                            'Symptom related',
                            'Talk to a Doctor'],
                            icons=['home','activity','heart','person'],
                            default_index=0)
    elif lang=='हिंदी':
        selected = option_menu('एकाधिक रोग भविष्यवाणी प्रणाली',
                            
                            ['मुखपृष्ठ',
                            'पीसीओएस की सूचना',
                            'स्तन कैंसर बीमारी की सूचना',
                            'हृदयरोग की सूचना',
                            'लक्षण से बीमारी की सूचना',
                            'डॉक्टर से बात करे'],
                            icons=['home','activity','heart','person'],
                            default_index=0)

#English Title Page
if (selected == 'Home'):
    st.title("ML Disease Prediction System v2.0")
    st.write("This project is prepared under the guidance of Dr. Nancy Kumari. This website can help predict a lot of diseases from basic symptoms and lab test results.\n\n Disclaimer:  All these predictions are powered by artificial intelligence, they don't replace doctors.")

#Hindi Title Page
if (selected == 'मुखपृष्ठ'):
    st.title("कंप्यूटर आधारित रोग पूर्वानुमान प्रणाली v2.0")
    st.write("यह प्रोजेक्ट डॉ. नॅन्सी कुमारी के मार्गदर्शन में तैयार किया गया है। यह वेबसाइट बुनियादी लक्षणों और प्रयोगशाला परीक्षण के परिणामों से बहुत सी बीमारियों की भविष्यवाणी करने में मदद कर सकती है।\n\nअस्वीकरण: ये सभी भविष्यवाणियां कृत्रिम बुद्धिमत्ता द्वारा संचालित हैं, ये डॉक्टरों की जगह नहीं लेती हैं।")


# PCOS Prediction Page English
if (selected == 'PCOS Prediction'):
    
    # page title
    st.title('PCOS Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age(yrs)')

    with col2:
        Weight = st.text_input('Wight (Kg)')
        
    with col3:
        Height = st.text_input('Height (cm)')
    
    with col1:
        BMI = st.text_input('BMI')
    
    with col2:
        Blood_Group = st.text_input('Blood Groups (A+ = 11, A- = 12, B+ = 13, B- = 14, O+ =15, O- = 16, AB+ =17, AB- = 18)')
    
    with col3:
        Pulse_Rate = st.text_input('Pulse Rate (BPM)')
    
    with col1:
        RR = st.text_input('Breaths/min')
    
    with col2:
        Hb = st.text_input('Hb(g/dl)')
    
    with col3:
        Cycle = st.text_input('Cycle (R/l)')

    with col1:
        Cycle_Length = st.text_input('Cycle Length (Days)')

    with col2:
        Marraige_Status = st.text_input('Marriage Status (Yrs)')
    
    with col3:
        Pregnant = st.text_input('Pregnant (0 for NO and 1 for YES)')
        
    with col1:
        No_Of_Abortions = st.text_input('Number of Abortions')

    with col2:
        I_beta_HCG = st.text_input('I beta HCG (mIU/mL)')
    
    with col3:
        II_beta_HCG = st.text_input('II beta-HCG(mIU/mL)')
    
    with col1:
        FSH = st.text_input('FSH(mIU/mL)')

    with col2:
        LH= st.text_input('LH(mIU/mL)')
    
    with col3:
        FSH_LH = st.text_input('FSH/LH')
    
    with col1:
        Hip= st.text_input('Hip(inch)')

    with col2:
        Waist= st.text_input('Waist(inch)')
    
    with col3:
        Ratio = st.text_input('Ratio = Waist:Hip')
    
    with col1:
        TSH = st.text_input('TSH (mIU/L)')
    
    with col2:
        AMH = st.text_input('AMH(ng/mL)')
    
    with col3:
        PRL = st.text_input('PRL(ng/mL)')
    
    with col1:
        Vit_D3 = st.text_input('Vit D3 (ng/mL)')
    
    with col2:
        PRG= st.text_input('PRG(ng/mL)')
    
    with col3:
        RBS= st.text_input('RBS(mg/dl)')
    
    with col1:
        Weight_Gain= st.text_input('Weight gain(YES->1 / NO->0)')
    
    with col2:
        hair_Growth = st.text_input('Hair Growth (YES->1 / NO->0)')
    
    with col3:
        Skin_Darkening = st.text_input('Skin Darkening (YES->1 / NO->0)')
    
    with col1:
        Hair_loss = st.text_input('Hair Loss (YES->1 / NO->0)')
    
    with col2:
        Pimples = st.text_input('Pimples (YES->1 / NO->0)')
    
    with col3:
        Fast_food = st.text_input('Fast Food (YES->1 / NO->0)')
    
    with col1:
        Reg_Exercise= st.text_input('Regular Exercise (YES->1 / NO->0)')
    
    with col2:
        BP_Systolic = st.text_input('BP_Systolic (mmHg)')
    
    with col3:
        BP_Diastolic = st.text_input('BP_Diastolic (mmHg)')
    
    with col1:
        Follicle_No_L = st.text_input('Follicle No. (L)')
    
    with col2:
        Follicle_No_R = st.text_input('Follicle No. (R)')
    
    with col3:
        Avg_F_size_L = st.text_input('Avg. F size (L) (mm)')
    
    with col1:
        Avg_F_size_R = st.text_input('Avg. F size (R) (mm)')

    with col2:
        Endometrium = st.text_input('Endometrium (mm)')
    

    
    
    # code for Prediction
    pcos_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('PCOS Test Result'):
        pcos_prediction = pcos_model.predict([[age, Weight, Height, BMI, Blood_Group, Pulse_Rate, RR, Hb, Cycle, Cycle_Length, Marraige_Status, Pregnant, No_Of_Abortions, I_beta_HCG, II_beta_HCG, FSH, LH, FSH_LH, Hip, Waist, Ratio, TSH, AMH, PRL, Vit_D3, PRG, RBS, Weight_Gain, hair_Growth, Skin_Darkening, Hair_loss, Pimples, Fast_food, Reg_Exercise, BP_Systolic, BP_Diastolic, Follicle_No_L, Follicle_No_R, Avg_F_size_L, Avg_F_size_R, Endometrium ]])


        #diab_prediction1 = diabetes_model.predict_proba([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (pcos_prediction[0] == 1):
          pcos_diagnosis = 'The person is suffering from PCOS'#+str(diab_prediction1[0][1])
        else:
          pcos_diagnosis = 'The person is not suffering from pcos'
        
        st.success(pcos_diagnosis)

# PCOS Prediction Page Hindi
if (selected == 'पीसीओएस की सूचना'):
    
    # page title
    st.title('मशीन लर्निंग का उपयोग कर डायबिटीज की भविष्यवाणी')
    
    
    # getting the input data from the user
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('आयु (yrs)')

    with col2:
        Weight = st.text_input('वजन (Kg)')
        
    with col3:
        Height = st.text_input('लम्बाई (cm)')
    
    with col1:
        BMI = st.text_input('शरीरिक माप अनुपात')
    
    with col2:
        Blood_Group = st.text_input('रक्त समूह (A+ = 11, A- = 12, B+ = 13, B- = 14, O+ =15, O- = 16, AB+ =17, AB- = 18)')
    
    with col3:
        Pulse_Rate = st.text_input('पल्स दर (BPM)')
    
    with col1:
        RR = st.text_input('रेट रेट(Breaths/min)')
    
    with col2:
        Hb = st.text_input('हेमोग्लोबिन(g/dl)')
    
    with col3:
        Cycle = st.text_input('चक्र (R/l)')

    with col1:
        Cycle_Length = st.text_input('चक्र लंबाई (Days)')

    with col2:
        Marraige_Status = st.text_input('विवाह स्थिति (Yrs)')
    
    with col3:
        Pregnant = st.text_input('गर्भवती (0 for NO and 1 for YES)')
        
    with col1:
        No_Of_Abortions = st.text_input('गर्भपातों की संख्या')

    with col2:
        I_beta_HCG = st.text_input('आई बीटा HCG (mIU/mL)')
    
    with col3:
        II_beta_HCG = st.text_input('द्वितीय बीटा-HCG(mIU/mL)')
    
    with col1:
        FSH = st.text_input('एफएसएच(mIU/mL)')

    with col2:
        LH= st.text_input('एलएच(mIU/mL)')
    
    with col3:
        FSH_LH = st.text_input('एफएसएच/एलएच')
    
    with col1:
        Hip= st.text_input('बोकन(inch)')

    with col2:
        Waist= st.text_input('कमर(inch)')
    
    with col3:
        Ratio = st.text_input('अनुपात = कमर:बोकन')
    
    with col1:
        TSH = st.text_input('टीएसएच (mIU/L)')
    
    with col2:
        AMH = st.text_input('एएमएच(ng/mL)')
    
    with col3:
        PRL = st.text_input('प्रोलैक्टिन(ng/mL)')
    
    with col1:
        Vit_D3 = st.text_input('विटामिन डी३ (ng/mL)')
    
    with col2:
        PRG= st.text_input('प्रोगेस्टेरोन(ng/mL)')
    
    with col3:
        RBS= st.text_input('रंधानीय रक्त शर्करा(mg/dl)')
    
    with col1:
        Weight_Gain= st.text_input('वजन बढ़ाना(YES->1 / NO->0)')
    
    with col2:
        hair_Growth = st.text_input('बालों का वृद्धि (YES->1 / NO->0)')
    
    with col3:
        Skin_Darkening = st.text_input('त्वचा का गहरापन (YES->1 / NO->0)')
    
    with col1:
        Hair_loss = st.text_input('बालों का झड़ना (YES->1 / NO->0)')
    
    with col2:
        Pimples = st.text_input('मुँहासे (YES->1 / NO->0)')
    
    with col3:
        Fast_food = st.text_input('फ़ास्ट फ़ूड (YES->1 / NO->0)')
    
    with col1:
        Reg_Exercise= st.text_input('नियमित व्यायाम (YES->1 / NO->0)')
    
    with col2:
        BP_Systolic = st.text_input('रक्तचाप उच्च (mmHg)')
    
    with col3:
        BP_Diastolic = st.text_input('रक्तचाप निम्न (mmHg)')
    
    with col1:
        Follicle_No_L = st.text_input('फॉलिकल संख्या (L)')
    
    with col2:
        Follicle_No_R = st.text_input('फॉलिकल संख्या (R)')
    
    with col3:
        Avg_F_size_L = st.text_input('औसत फॉलिकल आकार (L) (mm)')
    
    with col1:
        Avg_F_size_R = st.text_input('औसत फोलिकल आकार (R) (mm)')

    with col2:
        Endometrium = st.text_input('अंतः गर्भाशय परिपच (mm)')
        
    # code for Prediction
    pcos_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('पीसीओएस जाँच परिणाम'):
        pcos_prediction = pcos_model.predict([[age, Weight, Height, BMI, Blood_Group, Pulse_Rate, RR, Hb, Cycle, Cycle_Length, Marraige_Status, Pregnant, No_Of_Abortions, I_beta_HCG, II_beta_HCG, FSH, LH, FSH_LH, Hip, Waist, Ratio, TSH, AMH, PRL, Vit_D3, PRG, RBS, Weight_Gain, hair_Growth, Skin_Darkening, Hair_loss, Pimples, Fast_food, Reg_Exercise, BP_Systolic, BP_Diastolic, Follicle_No_L, Follicle_No_R, Avg_F_size_L, Avg_F_size_R, Endometrium ]])

        
        if (pcos_prediction[0] == 1):
          pcos_diagnosis = 'इस व्यक्ति को पीसीओएस हो सकती है'
        else:
          pcos_diagnosis = 'इस व्यक्ति को पीसीओएस नहीं है'
        
        st.success(pcos_diagnosis)



# Cardiovascular Disease Prediction Page English
if (selected == 'Cardiovascular Disease Prediction'):
    
    # page title
    st.title('Cardiovascular Disease Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        gender = st.text_input('gender')
        
    with col2:
        height = st.text_input('height')
        
    with col3:
        weight = st.text_input('weight')
        
    with col1:
        ap_hi = st.text_input('apical systolic blood pressure')
        
    with col2:
        ap_lo = st.text_input('apical diastolic blood pressure')
        
    with col3:
        cholesterol = st.text_input('cholesterol')
        
    with col1:
        gluc = st.text_input('Glocose')
        
    with col2:
        smoke = st.text_input('Smoking (0/1)')
        
    with col3:
        alco = st.text_input('alcohol consumption (0/1)')
        
    with col1:
        active = st.text_input('Physical activity level of the individual (0/1)')
    
    
    if gender:
        gender = int(gender)
    if height:
        height = float(height)
    if weight:
        weight = float(weight)
    if ap_hi:
        ap_hi = int(ap_hi)
    if ap_lo:
        ap_lo = int(ap_lo)
    if cholesterol:
        cholesterol = int(cholesterol)
    if gluc:
        gluc = int(gluc)
    if smoke:
        smoke = int(smoke)
    if alco:
        alco = int(alco)
    if active:
        active = int(active)

# code for Prediction
    cardiovascular_diagnosis = ''
    
# creating a button for Prediction
    
    if st.button('Cardiovascular Disease Test Result'):
        cardiovascular_prediction = Cardiovascular_disease_model.predict([[gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])
        
        if (cardiovascular_prediction[0] == 1):
            cardiovascular_diagnosis = 'The person is suffering from Cardiovascular Disease'
        else:
            cardiovascular_diagnosis = 'The person is not sufferning from Cardiovascular Disease'
        
        st.success(cardiovascular_diagnosis)

# cardiovascular Prediction Page Hindi
if (selected == 'हृदयरोग की सूचना'):
    
    # page title
    st.title('मशीन लर्निंग का उपयोग कर हृदयरोग की भविष्यवाणी')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.text_input('जेंडर')
        
    with col2:
        height = st.text_input('लंबाई')
        
    with col3:
        weight = st.text_input('वजन')
        
    with col1:
        ap_hi = st.text_input('शीर्ष सिस्टोलिक रक्तचाप')
        
    with col2:
        ap_lo = st.text_input('शीर्ष डायस्टोलिक रक्तचाप')
        
    with col3:
        cholesterol = st.text_input('कोलेस्ट्रोल')
        
    with col1:
        gluc = st.text_input('ग्लूकोज')
        
    with col2:
        smoke = st.text_input('धूम्रपान (0/1)')
        
    with col3:
        alco = st.text_input('शराब का सेवन (0/1)')
        
    with col1:
        active = st.text_input('व्यक्ति का शारीरिक गतिविधि स्तर (0/1)')
    
    
    # code for Prediction
    cardiovascular_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('हृदयरोग जाँच परिणाम'):
        cardiovascular_prediction = Cardiovascular_disease_model.predict([[gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])
        
        if (cardiovascular_prediction[0] == 1):
          cardiovascular_diagnosis = 'इस व्यक्ति को हृदयरोग हो सकती है'
        else:
          cardiovascular_diagnosis = 'इस व्यक्ति को हृदयरोग नहीं है'
        
        st.success(cardiovascular_diagnosis)




# breast Cancer's Prediction Page English
if (selected == "Breast Cancer Prediction"):
    
    # page title
    st.title("Breast Cancer Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        radius_mean = st.text_input('Radius Mean')
        
    with col2:
        texture_mean = st.text_input('Texture Mean')
        
    with col3:
        perimeter_mean = st.text_input('Perimeter mean')
        
    with col4:
        area_mean = st.text_input('Area Mean')
        
    with col5:
        smoothness_mean = st.text_input('Smoothness Mean')
        
    with col1:
        compactness_mean = st.text_input('Compactness Mean')
        
    with col2:
        concavity_mean = st.text_input('Concavity mean')
        
    with col3:
        concave_points_mean = st.text_input('Cancave points mean')
        
    with col4:
        symmetry_mean = st.text_input('Symmetry mean')
        
    with col5:
        fractal_dimension_mean = st.text_input('Fractal Dimention Mean')
        
    with col1:
        radius_se = st.text_input('Radius se')
        
    with col2:
        texture_se = st.text_input('texture se')
        
    with col3:
        perimeter_se = st.text_input('perimeter se')
        
    with col4:
        area_se = st.text_input('area se')
        
    with col5:
        smoothness_se = st.text_input('smoothness se')
        
    with col1:
        compactness_se = st.text_input('compactness se')
        
    with col2:
        concavity_se = st.text_input('concavity se')
        
    with col3:
        concave_points_se = st.text_input('concave points se')
        
    with col4:
        symmetry_se = st.text_input('symmetry se')
        
    with col5:
        fractal_dimension_se = st.text_input('fractal dimension se')
        
    with col1:
        radius_worst = st.text_input('radius worst')
        
    with col2:
        texture_worst = st.text_input('texture worst')
    
    with col3:
        perimeter_worst = st.text_input('Perimeter worst')
        
    with col4:
        area_worst = st.text_input('Area Worst')
        
    with col5:
        smoothness_worst = st.text_input('smoothness worst')
        
    with col1:
        compactness_worst = st.text_input('compactness worst')
        
    with col2:
        concavity_worst = st.text_input('concavity worst')
        
    with col3:
        concave_points_worst = st.text_input('concave points worst')
        
    with col4:
        symmetry_worst = st.text_input('symmetry worst')
        
    with col5:
        fractal_dimension_worst = st.text_input('fractal dimension worst')
        
    
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Breast Cancer   
    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breastCancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])                          
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = "The person has Breast Cancer"
        else:
          breast_cancer_diagnosis = "The person does not have Breast Cancer"
        
    st.success(breast_cancer_diagnosis)

# Breast Cancer Prediction Page Hindi
if (selected == 'स्तन कैंसर बीमारी की सूचना'):
    # page title
    st.title("मशीन लर्निंग का उपयोग कर स्तन कैंसर की भविष्यवाणी")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        radius_mean = st.text_input('रेडियस माध्य')
        
    with col2:
        texture_mean = st.text_input('बनावट माध्य')
        
    with col3:
        perimeter_mean = st.text_input('परिधि माध्य')
        
    with col4:
        area_mean = st.text_input('क्षेत्रफल माध्य')
        
    with col5:
        smoothness_mean = st.text_input('मुलायमता माध्य')
        
    with col1:
        compactness_mean = st.text_input('संक्षिप्तता माध्य')
        
    with col2:
        concavity_mean = st.text_input('अवतलता माध्य')
        
    with col3:
        concave_points_mean = st.text_input('अवतल बिंदु माध्य')
        
    with col4:
        symmetry_mean = st.text_input('सममिति माध्य')
        
    with col5:
        fractal_dimension_mean = st.text_input('फ्रैक्टल आयाम माध्य')
        
    with col1:
        radius_se = st.text_input('रेडियस से')
        
    with col2:
        texture_se = st.text_input('बनावट से')
        
    with col3:
        perimeter_se = st.text_input('परिधि से')
        
    with col4:
        area_se = st.text_input('क्षेत्रफल से')
        
    with col5:
        smoothness_se = st.text_input('मुलायमता से')
        
    with col1:
        compactness_se = st.text_input('संक्षिप्तता से')
        
    with col2:
        concavity_se = st.text_input('अवतलता से')
        
    with col3:
        concave_points_se = st.text_input('अवतल बिंदुओं से')
        
    with col4:
        symmetry_se = st.text_input('सममिति से')
        
    with col5:
        fractal_dimension_se = st.text_input('फ्रैक्टल आयाम से')
        
    with col1:
        radius_worst = st.text_input('रेडियस सबसे खराब')
        
    with col2:
        texture_worst = st.text_input('बनावट सबसे खराब')
    
    with col3:
        perimeter_worst = st.text_input('परिधि सबसे खराब')
        
    with col4:
        area_worst = st.text_input('क्षेत्रफल सबसे खराब')
        
    with col5:
        smoothness_worst = st.text_input('मुलायमता सबसे खराब')
        
    with col1:
        compactness_worst = st.text_input('संक्षिप्तता सबसे खराब')
        
    with col2:
        concavity_worst = st.text_input('अवतलता सबसे खराब')
        
    with col3:
        concave_points_worst = st.text_input('अवतल बिंदुओं सबसे खराब')
        
    with col4:
        symmetry_worst = st.text_input('सममिति सबसे खराब')
        
    with col5:
        fractal_dimension_worst = st.text_input('फ्रैक्टल आयाम सबसे खराब')
        
        
    
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("स्तन कैंसर की बीमारी का जाँच परिणाम"):
        breast_cancer_prediction = breastCancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])                          
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = "इस व्यक्ति को पार्किंसंस रोग हो सकता है।"
        else:
          breast_cancer_diagnosis = "इस व्यक्ति को पार्किंसंस नहीं है।"
        
    st.success(breast_cancer_diagnosis)

# Symptom based disease prediction page English
if (selected == 'Symptom related'):
    st.title("Symptom based Disease Prediction")
    st.write("Select a few symptoms from the list below \n\n\n")
    symptoms = ['itching', 'weight_loss', 'pain_behind_the_eyes', 'mild_fever',
       'throat_irritation', 'neck_pain', 'swollen_extremeties',
       'slurred_speech', 'hip_joint_pain', 'movement_stiffness',
       'unsteadiness', 'continuous_feel_of_urine', 'internal_itching',
       'depression', 'muscle_pain', 'altered_sensorium', 'belly_pain',
       'abnormal_menstruation', 'dischromic _patches', 'increased_appetite',
       'rusty_sputum', 'lack_of_concentration', 'fluid_overload.1',
       'blood_in_sputum', 'prominent_veins_on_calf', 'silver_like_dusting',
       'yellow_crust_ooze']

    HNR = st.multiselect('Your Symptoms:', symptoms)
    list1 = [symptoms.index(i) for i in HNR]
    symp_test = np.zeros(28)
    for i in list1:
        symp_test[i]=1
    symp_test = symp_test.reshape(1,-1)
    
    symptoms_prediction = symptom_model.predict(symp_test)
    if(len(HNR)>1):
        st.success("You may be suffering from "+symptoms_prediction[0]+". This is a machine learning prediction. You may or may not be suffering from the following disease. Consult a doctor.")

# Symptom based disease prediction page Hindi
if (selected == 'लक्षण से बीमारी की सूचना'):
    st.title("लक्षण आधारित रोग भविष्यवाणी")
    st.write("नीचे दी गई सूची में से कुछ लक्षणों का चयन करें \n\n\n")
    symptoms = ['खुजली', 'वजन घटना', 'आँखों के पीछे दर्द', 'हल्का बुखार',
       'गले में जलन', 'गर्दन में दर्द', 'सूजे हुए अंग',
       'अस्पष्ट भाषण', 'कूल्हे_जोड़_दर्द', 'हिलने में परेशानी',
       'अस्थिरता', 'पेशाब का लगातार महसूस होना', 'आंतरिक खुजली',
       'अवसाद', 'मांसपेशियों में दर्द', 'परिवर्तित धारणा', 'पेट दर्द',
       'असामान्य मासिक धर्म', 'डिस्क्रोमिक पैच', 'बढ़ी हुई भूख',
       'जंग लगा थूक', 'एकाग्रता का अभाव', 'द्रव अधिभार',
       'थूक में खून', 'बछड़े पर प्रमुख नसें', 'चाँदी_की_धूल',
       'पीली पपड़ी रसना संक्रमण']

    HNR = st.multiselect('आपके लक्षण:', symptoms)
    list1 = [symptoms.index(i) for i in HNR]
    symp_test = np.zeros(27)
    for i in list1:
        symp_test[i]=1
    symp_test = symp_test.reshape(1,-1)
    
    symptoms_prediction = symptom_model.predict(symp_test)
    if(len(HNR)>1):
        st.success("आपको शायद "+symptoms_prediction[0]+" हो सकता है। यह एक मशीन लर्निंग भविष्यवाणी है। आप निम्न रोग से पीड़ित हो भी सकते हैं और नहीं भी। कृपया डॉक्टर से सलाह लें।")


if (selected == 'Talk to a Doctor'):
    st.title("Get an Appointment")
    st.write("Coming Soon.")

if (selected == 'डॉक्टर से बात करे'):
    st.title("अपॉइंटमेंट लें")
    st.write("Coming Soon")