import streamlit as st

# 1. 페이지 설정 (타이틀, 레이아웃)
st.set_page_config(
    page_title="휘명고등학교",
    page_icon="🏫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 검은색 배경 및 중앙 정렬 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경을 검은색으로 변경 */
    .stApp {
        background-color: #0e0e11;
        color: #ffffff;
    }

    /* 상단 기본 헤더/메뉴 숨기기 (몰입감 향상) */
    header { visibility: hidden; }
    footer { visibility: hidden; }

    #root > div:nth-child(1) > div > div > div > section {
        padding-top: 5rem;
    }

    /* 메인 타이틀 스타일링 */
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        letter-spacing: 4px;
        margin-top: 100px;
        margin-bottom: 60px;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
    }

    /* 버튼 스타일링 */
    div.stButton > button {
        width: 100%;
        background-color: #1a1a24;
        color: #e0e0e0;
        border: 1px solid #3a3a4d;
        padding: 16px 24px;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.25s ease;
        margin-bottom: 12px;
    }

    /* 버튼 마우스 호버 효과 */
    div.stButton > button:hover {
        background-color: #2e2e42;
        color: #ffffff;
        border-color: #7a7a9e;
        box-shadow: 0 0 10px rgba(122, 122, 158, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 3. 게임 세션 상태 초기화
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "has_save_data" not in st.session_state:
    st.session_state.has_save_data = False  # 세이브 데이터 존재 여부
if "scene" not in st.session_state:
    st.session_state.scene = "intro"


# 4. 화면 렌더링
if not st.session_state.game_started:
    # --- 메인 화면 ---
    st.markdown('<div class="main-title">휘명고등학교</div>', unsafe_allow_html=True)

    # 중앙 배치를 위해 3컬럼 구조 사용 (가운데 컬럼에 버튼 배치)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # 시작하기 버튼
        if st.button("시작하기"):
            st.session_state.game_started = True
            st.session_state.scene = "intro"
            st.rerun()

        # 이어서하기 버튼 (저장 데이터가 없을 경우 비활성화 안내)
        if st.button("이어서하기"):
            if st.session_state.has_save_data:
                st.session_state.game_started = True
                st.rerun()
            else:
                st.toast("저장된 데이터가 없습니다.", icon="⚠️")

else:
    # --- 게임 플레이 화면 예시 ---
    st.write(f"현재 장면: {st.session_state.scene}")
    st.write("게임이 시작되었습니다.")
    
    if st.button("메인화면으로 돌아가기"):
        st.session_state.game_started = False
        st.rerun()
