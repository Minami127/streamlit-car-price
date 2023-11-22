import streamlit as st

def run_home_app() :
    st.subheader('Welcome~')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('고객 정보를 넣으먄, 차 구매 금액도 예측해 줍니다.')
    
    img_url= 'https://media.istockphoto.com/id/503346867/ko/%EC%82%AC%EC%A7%84/%ED%81%B4%EB%9E%98%EC%8B%9D-%EC%9E%90%EB%8F%99%EC%B0%A8-%EB%9E%A0%EB%A6%AC-bmw-dixi.jpg?s=612x612&w=0&k=20&c=66u2h0-A09R8jxX6M8sbwoFLcb8pW0LrE-hc6AtfEyQ='

    st.image(img_url)