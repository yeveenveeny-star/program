import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="Letter Mailbox",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. 디자인 스타일 적용 (CSS)
st.markdown(
    """
    <style>
    /* 전체 앱 배경색: 따뜻한 연두색 */
    .stApp {
        background-color: #DCE7C8;
    }
    header, footer { visibility: hidden; }

    /* 메인 화면 중앙 정렬 컨테이너 */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        max-width: 550px;
        margin: 30px auto;
    }

    /* 우체통 전체 (헤드 + 몸통 + 받침대) */
    .mailbox-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
    }

    /* 1) 우체통 상단 (둥근 뚜껑) */
    .mailbox-top {
        width: 180px;
        height: 70px;
        background: linear-gradient(135deg, #E54B4B, #C23838);
        border-top-left-radius: 90px;
        border-top-right-radius: 90px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    }

    /* 2) 우체통 몸통 */
    .mailbox-body {
        width: 180px;
        height: 120px;
        background: linear-gradient(135deg, #E54B4B, #C23838);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
        border-bottom-left-radius: 12px;
        border-bottom-right-radius: 12px;
        margin-top: -2px;
    }

    /* 하얀색 'POST' 글씨 */
    .mailbox-post-text {
        color: #FFFFFF;
        font-family: 'Courier New', monospace, sans-serif;
        font-weight: 900;
        font-size: 1.8rem;
        letter-spacing: 5px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.25);
        margin-bottom: 8px;
    }

    /* 편지 투입구 슬롯 */
    .mailbox-slot {
        width: 110px;
        height: 10px;
        background-color: #2B1414;
        border-radius: 5px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.6);
    }

    /* 3) 우체통 기둥/받침대 */
    .mailbox-stand {
        width: 40px;
        height: 35px;
        background-color: #A32E2E;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.3);
    }
    
    .mailbox-base {
        width: 90px;
        height: 12px;
        background-color: #7A2222;
        border-radius: 6px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    /* 분홍색 편지지 네모 박스 (입력 영역) */
    .letter-box {
        background-color: #FFF0F3;
        border: 3px dashed #FFB3C1;
        border-radius: 20px;
        padding: 20px;
        width: 100%;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    }

    /* 분홍 박스 내 텍스트 입력창 커스텀 */
    div.stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-size: 1rem !important;
        border-radius: 12px !important;
        border: 1px solid #FFC2D1 !important;
        padding: 15px !important;
        line-height: 1.6 !important;
    }
    
    /* 스트림릿 기본 라벨 숨기기 */
    div.stTextArea label {
        display: none;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. 화면 UI 구성
# ---------------------------------------------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 1) 중앙 전체 우체통 (POST 하얀색 글씨 포함)
st.markdown(
    """
    <div class="mailbox-wrapper">
        <div class="mailbox-top"></div>
        <div class="mailbox-body">
            <div class="mailbox-post-text">POST</div>
            <div class="mailbox-slot"></div>
        </div>
        <div class="mailbox-stand"></div>
        <div class="mailbox-base"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 2) 분홍색 네모 박스 내부 텍스트 입력 영역
st.markdown('<div class="letter-box">', unsafe_allow_html=True)

user_message = st.text_area(
    "letter_input",
    height=180,
    placeholder="분홍색 편지지에 내용을 직접 적어보세요...",
)

st.markdown("</div>", unsafe_allow_html=True)  # letter-box 닫기
st.markdown("</div>", unsafe_allow_html=True)  # main-container 닫기

# ---------------------------------------------------------
# 4. 하단 동작 처리
# ---------------------------------------------------------
if user_message:
    st.write("")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info(f"작성 중인 편지 글자 수: **{len(user_message)}자**")
    with col2:
        if st.button("우체통에 넣기 ✈️", use_container_width=True):
            st.success("편지가 우체통에 넣어졌습니다!")
