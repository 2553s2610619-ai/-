import streamlit as st
import time

# 문장 리스트
sentences = [
    "안녕하세요 반갑습니다",
    "파이썬은 재미있는 언어입니다",
    "스트림릿으로 웹앱 만들기",
    "타자 연습을 시작해봅시다"
]

st.title("⌨️ 타자연습 앱")

# 문장 선택
if "sentence" not in st.session_state:
    st.session_state.sentence = sentences[0]

if st.button("새 문장"):
    st.session_state.sentence = sentences[
        (sentences.index(st.session_state.sentence) + 1) % len(sentences)
    ]

target = st.session_state.sentence

st.subheader("따라 입력하세요")
st.code(target)

# 시작 시간 저장
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

user_input = st.text_input("여기에 입력하세요")

# 결과 확인
if user_input:
    if user_input == target:
        end_time = time.time()
        elapsed = round(end_time - st.session_state.start_time, 2)

        st.success("정답입니다!")
        st.write(f"걸린 시간: {elapsed}초")

        speed = round(len(target) / elapsed, 2)
        st.write(f"타자 속도: {speed} 글자/초")

    else:
        st.error("틀렸습니다. 다시 입력해보세요.")
