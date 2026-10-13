
import streamlit as st
import random

st.title("🍱 오늘 뭐 먹지?")
st.write("메뉴 고민은 이제 그만! 음식을 추천해 드립니다.")

# 음식 목록
foods = {
    "한식": ["김치찌개", "제육볶음", "비빔밥", "불고기"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕"],
    "일식": ["초밥", "라멘", "돈가스", "우동"],
    "양식": ["피자", "파스타", "햄버거", "스테이크"],
    "분식": ["떡볶이", "김밥", "순대", "라볶이"]
}

# 음식 종류 선택
category = st.selectbox("어떤 종류가 먹고 싶나요?", list(foods.keys()))

# 추천 버튼
if st.button("🎲 음식 추천받기"):
    food = random.choice(foods[category])
    st.success(f"오늘의 추천 메뉴는 {food}입니다! 😋")
