import os
from openai import OpenAI  # 또는 사용하시려는 AI 라이브러리

# API 클라이언트 초기화 (Streamlit Secrets 등에 키를 안전하게 보관하는 것이 좋습니다)
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.session_state.ai_reply = ""

# ... (기존 CSS 및 디자인 코드 생략) ...

# 1) 상단 영역 처리
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if not st.session_state.submitted:
    st.markdown('<div class="guide-text">고민을 적어주세요!</div>', unsafe_allow_html=True)

    user_message = st.text_area(
        "letter_input",
        height=100,
        placeholder="편지 작성...",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    submit_btn = st.button("작성 완료")

    if submit_btn:
        if user_message:
            st.session_state.submitted = True
            
            # [AI 연동 부분] 캐릭터의 답장 생성하기
            try:
                # 예시: OpenAI API 호출
                # response = client.chat.completions.create(
                #     model="gpt-4o-mini",
                #     messages=[
                #         {"role": "system", "content": "너는 사용자의 고민을 따뜻하게 위로해주는 다정한 AI 캐릭터야. 반말을 쓰고 친근하게 답장해줘."},
                #         {"role": "user", "content": user_message}
                #     ]
                # )
                # st.session_state.ai_reply = response.choices[0].message.content
                
                # 테스트용 임시 답장 (실제 API 연결 전 확인용)
                st.session_state.ai_reply = "고민을 털어놓아 주어서 고마워. 네 곁엔 항상 너를 응원하는 사람이 있다는 걸 잊지마!"
                
            except Exception as e:
                st.session_state.ai_reply = "편지를 전송하는 중에 작은 문제가 생겼어. 나중에 다시 시도해줘!"

            st.rerun()
        else:
            st.warning("내용을 입력해주세요!")
else:
    # 편지가 우체통으로 들어가는 애니메이션 영역
    st.markdown('<div class="sent-notice-text">편지가 발송되었어요!</div>', unsafe_allow_html=True)
    st.markdown('<div class="letter-envelope-animated">✉️</div>', unsafe_allow_html=True)
    
    # 애니메이션이 끝난 뒤(또는 하단에) 캐릭터의 답장 띄우기
    # 일정 시간 뒤에 답장을 보여주고 싶다면 st.empty()나 스피너를 활용할 수 있습니다.
    st.markdown(
        f"""
        <div style="background-color: #FFFFFF; padding: 20px; border-radius: 15px; border: 2px solid #E6D785; margin-top: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
            <p style="font-weight: 700; color: #5C5320; margin-bottom: 8px;">💌 캐릭터의 답장</p>
            <p style="color: #4A4A4A; font-size: 0.95rem; line-height: 1.5;">{st.session_state.ai_reply}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)
