import pickle
import streamlit as st

# membaca model
# Model = '/home/kisawa16/Documents/KULIAH/MACHINE LEARNING/UTS/NAIVE BAYES/naive_bayes_model.pkl'
naiveModel = pickle.load(open('naive_bayes_model.pkl', 'rb'))

# judul web
st.title('Prediksi Penyakit Jantung')

# input atribut
col1, col2 = st.columns(2)

with col1:
    age = st.text_input('Masukkan Umur anda')
    sex = st.text_input('Masukkan Jenis kelamin Male(1) Female(0)')
    cp = st.text_input('Masukkan tipe nyeri dada range 1-4')
    trtbps = st.text_input('Masukkan tekanan darah')
    chol = st.text_input('Masukkan kolesterol')
    fbs = st.text_input('Masukkan gula darah')
    restecg = st.text_input('Masukkan hasil elektrokardiografi')

with col2:
    thalach = st.text_input('Masukkan denyut jantung maksimal')
    exng = st.text_input('Masukkan Angina akibat olahraga')
    oldpeak = st.text_input('Depresi disebabkan oleh olahraga')
    slp = st.text_input('Kemiringan puncak latihan segmen')
    caa = st.text_input("Jumlah pembulu darah besar yang diwarnai dengan fluroskopi")
    thall = st.text_input("Hasil test thallium")

# Convert input values to numeric
if age and sex and cp and trtbps and chol and fbs and restecg and thalach and exng and oldpeak and slp and caa and thall:
    input_data = [
        float(age), float(sex), float(cp), float(trtbps), float(chol), float(fbs),
        float(restecg), float(thalach), float(exng), float(oldpeak), float(slp), 
        float(caa), float(thall)
    ]

    # code prediksi
    heart_diagnosis = ''

    # tombol prediksi
    if st.button('Test Prediksi Penyakit Jantung'):
        heart_predict = naiveModel.predict([input_data])

        if heart_predict[0] == 1:
            heart_diagnosis = "Pasien terindikasi terkena penyakit jantung"
        else:
            heart_diagnosis = "Pasien terindikasi tidak terkena penyakit jantung"

    # Menampilkan hasil prediksi
    st.success(heart_diagnosis)
else:
    st.warning('Masukkan semua nilai atribut sebelum melakukan prediksi.')
