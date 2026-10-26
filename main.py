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
    /* 전체 앱 배경색: 더 연한 파스텔톤 하늘색 */
    .stApp {
        background-color: #E2ECFD;
        background: linear-gradient(180deg, #E2ECFD 0%, #EEF4FF 70%, #F8FBFF 100%);
    }
    header, footer { visibility: hidden; }

    /* 화면 전체를 중앙 정렬하는 Flex 컨테이너 */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        max-width: 600px;
        margin: 20px auto 0 auto;
        position: relative;
        z-index: 2;
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

    /* 더 연한 파스텔톤 연두색 잔디밭 레이어 */
    .grass-field {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100vw;
        height: 160px;
        background: linear-gradient(180deg, #D4EDCD 0%, #BFE5B7 100%);
        border-top-left-radius: 50% 30px;
        border-top-right-radius: 50% 30px;
        box-shadow: inset 0 10px 15px rgba(255,255,255,0.3);
        z-index: 1;
    }

    /* 텍스트 입력 영역 전체를 화면 중앙에 160px 폭으로 고정 */
    div[data-testid="stTextArea"] {
        width: 160px !important;
        margin: 0 auto !important;
    }

    /* 텍스트 입력창 스타일 커스텀 */
    div.stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-size: 0.9rem !important;
        border-radius: 12px !important;
        border: 2px solid #BFE5B7 !important;
        padding: 10px !important;
        line-height: 1.4 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* 스트림릿 기본 라벨 숨기기 */
    div.stTextArea label {
        display: none;
    }

    /* 연한 노란색 '작성 완료' 버튼 커스텀 스타일 */
    div.stButton > button {
        background-color: #FFF3B0 !important;
        color: #5C5320 !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-weight: 700 !important;
        border: 2px solid #E6D785 !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08) !important;
        transition: all 0.2s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: #FFEE8C !important;
        border-color: #D4C36C !important;
        color: #423B14 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. 화면 UI 구성
# ---------------------------------------------------------

# 하단 잔디밭 배경
st.markdown('<div class="grass-field"></div>', unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 1) 하늘 배경 중앙의 전체 우체통 (POST 하얀색 글씨 포함)
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

# 2) 가로폭 160px 텍스트 입력 영역 (중앙 배치)
user_message = st.text_area(
    "letter_input",
    height=120,
    placeholder="편지 작성...",
)

st.markdown("<br>", unsafe_allow_html=True)

# 3) 화면 하단 중앙 연한 노란색 '작성 완료' 버튼 배치
col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
    submit_btn = st.button("작성 완료", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. 하단 동작 처리
# ---------------------------------------------------------
if submit_btn:
    if user_message:
        st.success("편지가 작성 완료되었습니다!")
    else:
        st.warning("내용을 입력해주세요!")
