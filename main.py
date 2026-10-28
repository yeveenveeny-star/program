import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="Letter Mailbox",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 세션 상태 초기화 (편지 제출 여부 저장)
if "submitted" not in st.session_state:
    st.session_state.submitted = False

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

    /* 구름 1 (좌측 상단) */
    .cloud-1 {
        width: 140px; height: 45px;
        top: 15%; left: 12%;
    }
    .cloud-1::before { width: 60px; height: 60px; top: -30px; left: 20px; }
    .cloud-1::after { width: 80px; height: 80px; top: -45px; left: 55px; }

    /* 구름 2 (우측 상단, 조금 크게) */
    .cloud-2 {
        width: 200px; height: 60px;
        top: 20%; right: 10%;
        opacity: 0.6;
    }
    .cloud-2::before { width: 80px; height: 80px; top: -40px; left: 35px; }
    .cloud-2::after { width: 100px; height: 100px; top: -55px; left: 85px; }

    /* 구름 3 (중앙 좌측 부근) */
    .cloud-3 {
        width: 120px; height: 40px;
        top: 45%; left: 8%;
        opacity: 0.5;
    }
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

    /* 맨 처음 화면 상단에 띄울 안내 텍스트 스타일 ("고민을 적어주세요!") */
    .guide-text {
        font-family: 'Malgun Gothic', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: #5C5320;
        margin-bottom: 12px;
        text-align: center;
    }

    /* 버튼 클릭 후 상단에 띄울 완료 텍스트 스타일 ("편지가 발송되었습니다" - 하얀색 배경) */
    .sent-notice-text {
        background-color: #FFFFFF;
        color: #5C5320;
        font-family: 'Malgun Gothic', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        padding: 10px 24px;
        border-radius: 12px;
        border: 2px solid #E6D785;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
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

    /* 우체통 전체 (헤드 + 몸통 + 받침대) */
    .mailbox-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
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

    /* 텍스트 입력 영역 전체 폭 300px, 높이 100px 고정 */
    div[data-testid="stTextArea"] {
        width: 300px !important;
        height: 100px !important;
        margin: 0 auto !important;
    }

    /* 텍스트 입력창 내부 스타일 커스텀 */
    div.stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-size: 0.9rem !important;
        border-radius: 12px !important;
        border: 2px solid #BFE5B7 !important;
        padding: 10px !important;
        line-height: 1.4 !important;
        height: 100px !important;
        min-height: 100px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* 스트림릿 기본 라벨 숨기기 */
    div.stTextArea label {
        display: none;
    }

    /* 연한 노란색 '작성 완료' 버튼 */
    div.stButton > button {
        background-color: #FFF3B0 !important;
        color: #5C5320 !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-weight: 700 !important;
        border: 2px solid #E6D785 !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        width: 280px !important;
        display: block !important;
        margin: 0 auto 0 calc(50% + 395px) !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08) !important;
        transition: all 0.2s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: #FFEE8C !important;
        border-color: #D4C36C !important;
        color: #423B14 !important;
    }

    /* 단독 편지 이모지 스타일 & 펑! 등장 + 0.5초 정지 후 투입구 낙하 애니메이션 */
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
        /* 1) 펑! 하고 확대되며 등장 */
        0% {
            transform: scale(0) translateY(-20px);
            opacity: 0;
        }
        25% {
            transform: scale(1.15) translateY(0);
            opacity: 1;
        }
        30% {
            transform: scale(1) translateY(0);
            opacity: 1;
        }
        /* 2) 0.5초간 가만히 정지 (30% ~ 55%) */
        55% {
            transform: scale(1) translateY(0);
            opacity: 1;
        }
        /* 3) 우체통 투입구 위치로 빠르게 가속 하강 및 약간의 회전 */
        85% {
            transform: translateY(350px) scale(0.6) rotate(-10deg);
            opacity: 1;
        }
        /* 4) 투입구 안으로 쏙 들어가면서 사라짐 */
        100% {
            transform: translateY(370px) scale(0.05) rotate(0deg);
            opacity: 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 3. 화면 UI 구성
# ---------------------------------------------------------

# 하늘 배경 위 구름 추가
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

# 하단 잔디밭 배경
st.markdown('<div class="grass-field"></div>', unsafe_allow_html=True)

# 1) 상단 영역: 제출 전/후 상태에 따른 안내 텍스트, 입력창, 버튼, 애니메이션 배치
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if not st.session_state.submitted:
    # 맨 처음 화면에만 보이는 "고민을 적어주세요!" 텍스트
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
            st.rerun()
        else:
            st.warning("내용을 입력해주세요!")
else:
    # 작성 완료 버튼을 누른 후 상단에 뜨는 하얀색 배경의 "편지가 발송되었습니다" 텍스트
    st.markdown('<div class="sent-notice-text">편지가 발송되었습니다</div>', unsafe_allow_html=True)
    # 펑! 하고 나타나서 투입구로 떨어지는 편지 이모지
    st.markdown(
        """
        <div class="letter-envelope-animated">✉️</div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# 2) 하단 영역: 하단에서 160px 위로 올라간 우체통 전체 배치
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
