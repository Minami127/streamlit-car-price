import numpy as np
import streamlit as st

import joblib

def run_ml_app() :
    st.subheader('구매 금액 예측')

    # 인공지능 파일을 읽어와서
    # 예측하는 화면을 개발한다

    regressor = joblib.load('./model/regressor.pkl')

    gender=st.radio('성별선택',['여자','남자'])

    if gender == '여자' :
        gender == 0
    else :
        gender == 1

    age=st.number_input('나이 입렵',20,100)

    salary=st.number_input('연봉입력', 10000, 1000000)

    debt =st.number_input('카드빚 입력',0,1000000)

    worth = st.number_input('자산입력',1000,10000000)
    

    if st.button('구매 예상 금액!') :
        # 예측한 결과를 화면에 보여준다.
        new_data=np.array([gender,age,salary,debt,worth]).reshape(1,-1)

        y_pred=regressor.predict(new_data)

        print(new_data)

        price = y_pred[0]
        if price < 0 :
            st.text('자동차를 구매하기 어렵습니다')
        else :
            st.text('이 고객은 {}금액정도 구매가능합니다.'.format(price))

    else :
        st.text('')

