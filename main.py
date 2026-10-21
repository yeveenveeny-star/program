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
        max-width: 600px;
        margin: 40px auto;
    }

    /* 우체통 본체 (상단이 둥근 우체통 모양) */
    .mailbox-head {
        background: linear-gradient(135deg, #E54B4B, #C23838);
        width: 220px;
        height: 110px;
        border-top-left-radius: 110px;
        border-top-right-radius: 110px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        padding-bottom: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        position: relative;
        z-index: 2;
        margin-bottom: -10px; /* 우체통과 편지지가 살짝 겹치도록 설정 */
    }

    /* 우체통에 들어가는 하얀색 'POST' 글씨 */
    .mailbox-post-text {
        color: #FFFFFF;
        font-family: 'Courier New', monospace, sans-serif;
        font-weight: 900;
        font-size: 1.8rem;
        letter-spacing: 4px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    /* 우체통 투입구 슬롯 */
    .mailbox-slot {
        width: 90px;
        height: 8px;
        background-color: #331A1A;
        border-radius: 4px;
        margin-top: 4px;
        box-shadow: inset 0 2px 3px rgba(0,0,0,0.5);
    }

    /* 분홍색 편지지 네모 박스 (입력 영역 포함) */
    .letter-box {
        background-color: #FFF0F3;
        border: 3px dashed #FFB3C1;
        border-radius: 20px;
        padding: 35px 25px 25px 25px;
        width: 100%;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        position: relative;
        z-index: 1;
    }

    /* 스트림릿 기본 text_area 스타일 커스텀 (분홍 편지지 안의 진짜 입력창) */
    div.stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-size: 1rem !important;
        border-radius: 12px !important;
        border: 1px solid #FFC2D1 !important;
        padding: 15px !important;
    }
    
    /* 스트림릿 라벨 숨기기 (깔끔한 디자인 유지) */
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

# 1) 상단 우체통 모양 (POST 글씨 포함)
st.markdown(
    """
    <div class="mailbox-head">
        <div class="mailbox-post-text">POST</div>
        <div class="mailbox-slot"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 2) 하단 분홍색 편지지 박스 및 직접 글을 쓰는 입력창
st.markdown('<div class="letter-box">', unsafe_allow_html=True)

user_message = st.text_area(
    "letter_input",
    height=160,
    placeholder="여기에 편지 내용을 자유롭게 적어보세요...",
)

st.markdown("</div>", unsafe_allow_html=True)  # letter-box 닫기
st.markdown("</div>", unsafe_allow_html=True)  # main-container 닫기

# ---------------------------------------------------------
# 4. 하단 부가 기능 (글자 수 확인 및 제출 버튼)
# ---------------------------------------------------------
if user_message:
    st.write("")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info(f"현재 작성 중인 편지 글자 수: **{len(user_message)}자**")
    with col2:
        if st.button("우체통에 넣기 ✈️", use_container_width=True):
            st.success("편지가 안전하게 접수되었습니다!")
