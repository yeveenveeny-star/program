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

    /* 화면 전체를 중앙 정렬하는 Flex 컨테이너 */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        max-width: 600px;
        margin: 40px auto;
    }

    /* 우체통 전체 (헤드 + 몸통 + 받침대) */
    .mailbox-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 25px;
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

    /* 텍스트 입력 영역을 감싸는 컨테이너 (화면의 약 1/3 너비인 320px 고정 및 중앙 정렬) */
    .input-wrapper {
        width: 320px;
        max-width: 100%;
    }

    /* 텍스트 입력창 스타일 커스텀 */
    div.stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-size: 0.95rem !important;
        border-radius: 14px !important;
        border: 2px solid #C8D6B9 !important;
        padding: 12px !important;
        line-height: 1.5 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
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

# 2) 크기가 줄어든 텍스트 입력 영역 (중앙 배치)
st.markdown('<div class="input-wrapper">', unsafe_allow_html=True)
user_message = st.text_area(
    "letter_input",
    height=120,
    placeholder="이곳에 편지 내용을 적어보세요...",
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # main-container 닫기

# ---------------------------------------------------------
# 4. 하단 동작 처리
# ---------------------------------------------------------
if user_message:
    st.write("")
    # 하단 정보도 중앙 폭에 맞춰 정렬되도록 구성
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info(f"글자 수: **{len(user_message)}자**")
    with col2:
        if st.button("우체통 넣기 ✈️", use_container_width=True):
            st.success("접수 완료!")
