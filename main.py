import streamlit as st

# 1. 페이지 기본 설정 (와이드 모드, 깔끔한 브라우저 탭 제목)
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

    /* 메인 컨테이너 중앙 정렬 및 레이아웃 */
    .main-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 30px;
    }

    /* 빨간 우체통 컨테이너 (화면의 약 1/3 크기감 연출) */
    .mailbox-container {
        width: 100%;
        max-width: 420px;
        background: linear-gradient(135deg, #E54B4B, #C23838);
        border-radius: 24px;
        padding: 30px 20px 40px 20px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
        margin: 0 auto;
    }

    /* 우체통 투입구 장식 */
    .mailbox-slot {
        width: 120px;
        height: 10px;
        background-color: #331A1A;
        border-radius: 5px;
        margin-bottom: 25px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
    }

    /* 분홍색 편지지 네모 박스 스타일 */
    .letter-paper {
        background-color: #FFF0F3;
        border: 2px dashed #FFB3C1;
        border-radius: 16px;
        padding: 25px;
        width: 100%;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }

    /* 스트림릿 기본 text_area 내부 스타일 조정 */
    textarea {
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-family: 'Courier New', monospace, sans-serif !important;
        font-size: 1.05rem !important;
        border-radius: 12px !important;
        border: 1px solid #FFC2D1 !important;
        padding: 15px !important;
    }
    
    /* 타이틀 텍스트 스타일 */
    .mailbox-title {
        color: #FFFFFF;
        font-weight: 700;
        font-size: 1.5rem;
        margin-bottom: 5px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .mailbox-subtitle {
        color: #FFE5EC;
        font-size: 0.9rem;
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. 화면 UI 구성
# ---------------------------------------------------------
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

# HTML/CSS 구조를 활용한 빨간 우체통 프레임 및 분홍 편지지 박스
st.markdown(
    """
    <div class="mailbox-container">
        <div class="mailbox-title">📬 소중한 마음 우체통</div>
        <div class="mailbox-subtitle">마음속 이야기를 편지에 담아 쏙 넣어주세요</div>
        <div class="mailbox-slot"></div>
    """,
    unsafe_allow_html=True,
)

# 분홍색 편지지 박스 안쪽 영역에 들어갈 플레이어 텍스트 입력창
st.markdown('<div class="letter-paper">', unsafe_allow_html=True)
user_message = st.text_area(
    "편지 내용 작성",
    height=180,
    placeholder="여기에 편지 내용을 자유롭게 적어보세요...",
    label_visibility="collapsed",
)
st.markdown("</div>", unsafe_allow_html=True)  # letter-paper 닫기

st.markdown("</div>", unsafe_allow_html=True)  # mailbox-container 닫기
st.markdown("</div>", unsafe_allow_html=True)  # main-wrapper 닫기

# ---------------------------------------------------------
# 4. 하단 부가 기능 (입력한 글자 수 확인 등)
# ---------------------------------------------------------
if user_message:
    st.write("")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info(f"현재 작성 중인 편지 글자 수: **{len(user_message)}자**")
    with col2:
        if st.button("우체통에 넣기 ✈️", use_container_width=True):
            st.success("편지가 안전하게 접수되었습니다!")
