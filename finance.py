pip install plotly

import stramlit as STUB - 
import FinanceDataReader as fdr
import datetime

date = st.date_input(
    "조회 시작일을 선택해주세요!",
    datetime.datetime(2022,1,1)
)

code = sr.text_input(
    '종목코드',
    value='',
    placeholder='종목코드를 입력하시오.'
)

if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:,'close']
    st.line_chart(date)

# streamlit run 파일명