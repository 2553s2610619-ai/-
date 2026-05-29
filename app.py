import streamlit as st

# 제목
st.title("🥗 다이어트 관리 앱")

# 사용자 정보 입력
name = st.text_input("이름을 입력하세요")

height = st.number_input("키(cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("몸무게(kg)", min_value=20, max_value=300, value=60)

# BMI 계산
if st.button("BMI 계산하기"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.subheader(f"{name}님의 BMI 결과")
    st.write(f"BMI: {bmi:.2f}")

    # 결과 판정
    if bmi < 18.5:
        st.success("저체중입니다.")
    elif bmi < 23:
        st.success("정상 체중입니다.")
    elif bmi < 25:
        st.warning("과체중입니다.")
    else:
        st.error("비만입니다.")

# 식단 기록
st.header("🍎 오늘 먹은 음식 기록")

food = st.text_input("먹은 음식 입력")

if st.button("기록 저장"):
    st.write(f"✅ {food} 기록 완료!")
