import json
import urllib.request
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="Letter Mailbox",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 세션 상태 초기화
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "ai_reply" not in st.session_state:
    st.session_state.ai_reply = ""


# [함수] 외부 라이브러리 없이 파이썬 내장 urllib으로 OpenAI API 호출하기
def get_ai_response(user_text):
    # 👇 여기에 본인의 실제 OpenAI API 키를 입력하세요! ("YOUR_OPENAI_API_KEY" 대신 입력)
    api_key = "YOUR_OPENAI_API_KEY"

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "너는 사용자의 고민을 따뜻하게 위로해주는 다정한 AI"
                    " 캐릭터야. 반말을 쓰고 친근하고 다정하게 편지 답장을 해줘."
                ),
            },
            {"role": "user", "content": user_text},
        ],
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except Exception as e:
        return (
            "편지를 읽어보았지만, 지금은 답장을 전하기가 조금 어려울 것 같아!"
        )


# 2. 디자인 스타일 적용 (CSS)
st.markdown(
    """
    <style>
    /* 전체 앱 배경색: 더 연한 파스텔톤 하늘색 */
    .stApp {
        background-color: #E2ECFD;
        background: linear-gradient(180deg, #E2ECFD 0%, #EEF4FF 70%, #F8FBFF 100%);
    }
    header, footer { visibility: hidden; }

    /* 하늘 위 둥실 떠 있는 구름 배경 컨테이너 */
    .sky-clouds {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 1;
        pointer-events: none;
        overflow: hidden;
    }

    /* 순수 CSS로 그린 감성적인 구름 스타일 */
    .cloud {
        position: absolute;
        background: #FFFFFF;
        border-radius: 100px;
        opacity: 0.75;
    }
    .cloud::before, .cloud::after {
        content: '';
        position: absolute;
        background: #FFFFFF;
        border-radius: 50%;
    }

    .cloud-1 { width: 140px; height: 45px; top: 15%; left: 12%; }
    .cloud-1::before { width: 60px; height: 60px; top: -30px; left: 20px; }
    .cloud-1::after { width: 80px; height: 80px; top: -45px; left: 55px; }

    .cloud-2 { width: 200px; height: 60px; top: 20%; right: 10%; opacity: 0.6; }
    .cloud-2::before { width: 80px; height: 80px; top: -40px; left: 35px; }
    .cloud-2::after { width: 100px; height: 100px; top: -55px; left: 85px; }

    .cloud-3 { width: 120px; height: 40px; top: 45%; left: 8%; opacity: 0.5; }
    .cloud-3::before { width: 50px; height: 50px; top: -25px; left: 20px; }
    .cloud-3::after { width: 65px; height: 65px; top: -35px; left: 45px; }

    /* 화면 전체를 중앙 정렬하는 Flex 컨테이너 (상단 배치용) */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        max-width: 600px;
        margin: 20px auto 0 auto;
        position: relative;
        z-index: 2;
    }

    /* 맨 처음 화면 상단에 띄울 안내 텍스트 스타일 */
    .guide-text {
        font-family: 'Malgun Gothic', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: #5C5320;
        margin-bottom: 12px;
        text-align: center;
    }

    /* 버튼 클릭 후 상단에 띄울 완료 텍스트 스타일 */
    .sent-notice-text {
        color: #5C5320;
        font-family: 'Malgun Gothic', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 10px;
        text-align: center;
    }

    /* 화면 하단으로부터 160px 위치에 고정될 우체통 컨테이너 */
    .mailbox-bottom-container {
        position: fixed;
        bottom: 160px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 3;
    }

    .mailbox-wrapper { display: flex; flex-direction: column; align-items: center; }
    .mailbox-top {
        width: 180px; height: 70px; background: linear-gradient(135deg, #E54B4B, #C23838);
        border-top-left-radius: 90px; border-top-right-radius: 90px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }
    .mailbox-body {
        width: 180px; height: 120px; background: linear-gradient(135deg, #E54B4B, #C23838);
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15); border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; margin-top: -2px;
    }
    .mailbox-post-text {
        color: #FFFFFF; font-family: 'Courier New', monospace, sans-serif; font-weight: 900;
        font-size: 1.8rem; letter-spacing: 5px; text-shadow: 0 2px 4px rgba(0,0,0,0.25); margin-bottom: 8px;
    }
    .mailbox-slot { width: 110px; height: 10px; background-color: #2B1414; border-radius: 5px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.6); }
    .mailbox-stand { width: 40px; height: 35px; background-color: #A32E2E; box-shadow: inset 0 2px 5px rgba(0,0,0,0.3); }
    .mailbox-base { width: 90px; height: 12px; background-color: #7A2222; border-radius: 6px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }

    .grass-field {
        position: fixed; bottom: 0; left: 0; width: 100vw; height: 160px;
        background: linear-gradient(180deg, #D4EDCD 0%, #BFE5B7 100%);
        border-top-left-radius: 50% 30px; border-top-right-radius: 50% 30px;
        box-shadow: inset 0 10px 15px rgba(255,255,255,0.3); z-index: 1;
    }

    div[data-testid="stTextArea"] { width: 300px !important; height: 100px !important; margin: 0 auto !important; }
    div.stTextArea textarea {
        background-color: #FFFFFF !important; color: #4A4A4A !important; font-family: 'Malgun Gothic', sans-serif !important;
        font-size: 0.9rem !important; border-radius: 12px !important; border: 2px solid #BFE5B7 !important;
        padding: 10px !important; line-height: 1.4 !important; height: 100px !important; min-height: 100px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    div.stTextArea label { display: none; }

    div.stButton > button {
        background-color: #FFF3B0 !important; color: #5C5320 !important; font-family: 'Malgun Gothic', sans-serif !important;
        font-weight: 700 !important; border: 2px solid #E6D785 !important; border-radius: 12px !important;
        padding: 10px 20px !important; width: 280px !important; display: block !important;
        margin: 0 auto 0 calc(50% + 395px) !important; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08) !important;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover { background-color: #FFEE8C !important; border-color: #D4C36C !important; color: #423B14 !important; }

    /* 편지 이모지 낙하 애니메이션 (투입구 위치에 맞춤) */
    .letter-envelope-animated {
        font-size: 10.5rem;
        text-align: center;
        margin: 20px auto 0 auto;
        position: relative;
        z-index: 4;
        filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.15));
        animation: letterDropSequence 1.6s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    }

    @keyframes letterDropSequence {
        0% { transform: scale(0) translateY(-20px); opacity: 0; }
        25% { transform: scale(1.15) translateY(0); opacity: 1; }
        30% { transform: scale(1) translateY(0); opacity: 1; }
        55% { transform: scale(1) translateY(0); opacity: 1; }
        85% { transform: translateY(220px) scale(0.6) rotate(-10deg); opacity: 1; }
        100% { transform: translateY(240px) scale(0.05) rotate(0deg); opacity: 0; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. 화면 UI 구성
# ---------------------------------------------------------

st.markdown(
    """
    <div class="sky-clouds">
        <div class="cloud cloud-1"></div>
        <div class="cloud cloud-2"></div>
        <div class="cloud cloud-3"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="grass-field"></div>', unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

if not st.session_state.submitted:
    st.markdown(
        '<div class="guide-text">고민을 적어주세요!</div>',
        unsafe_allow_html=True,
    )

    user_message = st.text_area(
        "letter_input", height=100, placeholder="편지 작성..."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    submit_btn = st.button("작성 완료")

    if submit_btn:
        if user_message:
            st.session_state.submitted = True
            # AI API를 통해 캐릭터 답장 받아오기
            st.session_state.ai_reply = get_ai_response(user_message)
            st.rerun()
        else:
            st.warning("내용을 입력해주세요!")
else:
    st.markdown(
        '<div class="sent-notice-text">편지가 발송되었어요!</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="letter-envelope-animated">✉️</div>
        """,
        unsafe_allow_html=True,
    )

    # AI 캐릭터의 답장 편지지 카드
    st.markdown(
        f"""
        <div style="background-color: #FFFFFF; padding: 20px; border-radius: 15px; border: 2px solid #E6D785; margin-top: 15px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); z-index: 4; position: relative; max-width: 500px; width: 100%;">
            <p style="font-weight: 700; color: #5C5320; margin-bottom: 8px; font-size: 1rem;">💌 캐릭터의 답장</p>
            <p style="color: #4A4A4A; font-size: 0.95rem; line-height: 1.5; white-space: pre-wrap;">{st.session_state.ai_reply}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 다시 편지를 쓸 수 있게 초기화하는 버튼
    if st.button("새로운 고민 나누기"):
        st.session_state.submitted = False
        st.session_state.ai_reply = ""
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# 하단 우체통 배치
st.markdown(
    """
    <div class="mailbox-bottom-container">
        <div class="mailbox-wrapper">
            <div class="mailbox-top"></div>
            <div class="mailbox-body">
                <div class="mailbox-post-text">POST</div>
                <div class="mailbox-slot"></div>
            </div>
            <div class="mailbox-stand"></div>
            <div class="mailbox-base"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
