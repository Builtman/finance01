# pip install plotly

import streamlit as st
import FinanceDataReader as fdr
import datetime

# datetime: 날짜와시간을 다루는 모듈
# date: 날짜 기능만 제공합니다. 연, 월, 일
date = st.date_input(
    "조회 시작일을 선택해주세요!",
    datetime.datetime(2022,1,1)
)

# placeholder: 자리표시자, 어떤 동작인지 설명하는 문구 /  value: 값
code = st.text_input(
    '종목코드',
    value='',
    placeholder='종목코드를 입력하시오.'
)

# fdr: FinanceDataReader는 한국 주식 가격, 미국 주식 가격, 지수, 환율, 암호 화폐 가격, 종목 리스트 등을 제공하는 API 패키지
# df = fdr.DataReader(code, date): 가격가져오기
# sort.index(): 인덱스를 기준으로 데이터 정렬
# ascending=True: 오름차순 
# st.line_chart: 라인 차트를 표시하는 명령입니다.
if code and date:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:,'close']
    st.line_chart(date)

# streamlit run 파일명
# zeros952@naver.com / 파일명 : 고지은 / 메일제목 : 빅데이터_고지은