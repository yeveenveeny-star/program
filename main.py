import streamlit as st
import textwrap

# ==========================================
# 페이지 설정
# ==========================================

st.set_page_config(
    page_title="휘명고등학교",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 세션 상태
# ==========================================

if "screen" not in st.session_state:
    st.session_state.screen = "menu"

if "player_name" not in st.session_state:
    st.session_state.player_name = ""


# ==========================================
# 공통 CSS
# ==========================================

st.markdown(
    textwrap.dedent("""
    <style>

    /* Streamlit 기본 여백 제거 */
    .stApp {
        background: #050708;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* 상단 Streamlit 메뉴 */
    [data-testid="stHeader"] {
        background: transparent;
    }

    /* =====================================
       전체 게임 화면
    ===================================== */

    .game-screen {
        position: relative;

        width: 100%;
        height: 100vh;

        overflow: hidden;

        background:
            linear-gradient(
                90deg,
                #0b1012 0%,
                #222c30 34%,
                #111719 50%,
                #222c30 66%,
                #0b1012 100%
            );
    }


    /* =====================================
       천장
    ===================================== */

    .ceiling {
        position: absolute;

        left: 0;
        top: 0;

        width: 100%;
        height: 40%;

        background:
            linear-gradient(
                to bottom,
                #101719,
                #283337 70%,
                #151b1e
            );

        clip-path: polygon(
            0 0,
            100% 0,
            67% 100%,
            33% 100%
        );
    }


    /* =====================================
       왼쪽 벽
    ===================================== */

    .wall-left {
        position: absolute;

        left: 0;
        top: 20%;

        width: 35%;
        height: 60%;

        background: #151d20;

        clip-path: polygon(
            0 0,
            100% 25%,
            100% 100%,
            0 100%
        );
    }


    /* =====================================
       오른쪽 벽
    ===================================== */

    .wall-right {
        position: absolute;

        right: 0;
        top: 20%;

        width: 35%;
        height: 60%;

        background: #151d20;

        clip-path: polygon(
            0 25%,
            100% 0,
            100% 100%,
            0 100%
        );
    }


    /* =====================================
       복도 끝
    ===================================== */

    .hall-end {
        position: absolute;

        left: 50%;
        top: 27%;

        transform: translateX(-50%);

        width: 18%;
        height: 45%;

        background:
            radial-gradient(
                ellipse at center,
                #090c0d 0%,
                #020303 65%,
                #000000 100%
            );

        box-shadow:
            0 0 90px rgba(0,0,0,0.9),
            inset 0 0 60px #000;
    }


    /* =====================================
       바닥
    ===================================== */

    .floor {
        position: absolute;

        left: 0;
        bottom: 0;

        width: 100%;
        height: 50%;

        background:
            linear-gradient(
                to bottom,
                #252d30,
                #0a0e10
            );

        clip-path: polygon(
            33% 0,
            67% 0,
            100% 100%,
            0 100%
        );
    }


    /* =====================================
       바닥 원근선
    ===================================== */

    .floor-line-left {
        position: absolute;

        left: 0;
        bottom: 0;

        width: 50%;
        height: 50%;

        border-top: 1px solid rgba(0,0,0,0.25);

        transform: skewY(20deg);
        transform-origin: top right;
    }

    .floor-line-right {
        position: absolute;

        right: 0;
        bottom: 0;

        width: 50%;
        height: 50%;

        border-top: 1px solid rgba(0,0,0,0.25);

        transform: skewY(-20deg);
        transform-origin: top left;
    }


    /* =====================================
       형광등
    ===================================== */

    .light {
        position: absolute;

        left: 50%;

        transform: translateX(-50%);

        height: 5px;

        background: #cbd3d2;

        box-shadow:
            0 0 12px rgba(220,235,235,0.5),
            0 0 35px rgba(180,210,210,0.18);
    }

    .light1 {
        top: 10%;
        width: 15%;
        opacity: 0.45;
    }

    .light2 {
        top: 21%;
        width: 10%;
        opacity: 0.32;
    }

    .light3 {
        top: 30%;
        width: 6%;
        opacity: 0.22;
    }


    /* =====================================
       어두운 가장자리
    ===================================== */

    .darkness {
        position: absolute;

        inset: 0;

        background:
            radial-gradient(
                ellipse at center,
                transparent 12%,
                rgba(0,0,0,0.28) 55%,
                rgba(0,0,0,0.88) 100%
            );

        pointer-events: none;
    }


    /* =====================================
       제목
    ===================================== */

    .title {
        position: absolute;

        left: 50%;
        top: 44%;

        transform: translate(-50%, -50%);

        width: 100%;

        text-align: center;

        color: #e1e6e6;

        font-family:
            "Noto Serif KR",
            "Malgun Gothic",
            serif;

        font-size: clamp(42px, 6vw, 78px);

        font-weight: 400;

        letter-spacing: 14px;

        text-shadow:
            0 0 15px rgba(255,255,255,0.12);

        z-index: 5;
    }


    /* =====================================
       버튼 영역
    ===================================== */

    .menu-buttons {
        position: absolute;

        left: 50%;
        top: 65%;

        transform: translateX(-50%);

        width: 260px;

        z-index: 10;
    }


    /* Streamlit 버튼 */

    .menu-buttons .stButton {
        margin-bottom: 16px;
    }

    .menu-buttons .stButton > button {

        width: 260px !important;

        height: 55px !important;

        background:
            rgba(5,8,9,0.72) !important;

        color:
            #d8dfdf !important;

        border:
            1px solid rgba(210,220,220,0.32) !important;

        border-radius:
            0 !important;

        font-family:
            "Malgun Gothic",
            sans-serif !important;

        font-size:
            16px !important;

        letter-spacing:
            4px !important;

        transition:
            all 0.3s ease !important;
    }


    .menu-buttons .stButton > button:hover {

        background:
            rgba(180,200,200,0.12) !important;

        border-color:
            rgba(230,240,240,0.7) !important;

        color:
            #ffffff !important;

        transform:
            translateY(-2px);
    }


    /* =====================================
       이름 입력 화면
    ===================================== */

    .name-screen {

        width: 100%;

        height: 100vh;

        display: flex;

        flex-direction: column;

        justify-content: center;

        align-items: center;

        background:
            radial-gradient(
                ellipse at center,
                #12191b,
                #020304
            );

        color: #dfe5e5;

        text-align: center;
    }


    .name-title {

        font-family:
            "Malgun Gothic",
            sans-serif;

        font-size: 26px;

        letter-spacing: 4px;

        margin-bottom: 30px;
    }


    </style>
    """),
    unsafe_allow_html=True
)


# ==========================================
# 메인 메뉴
# ==========================================

if st.session_state.screen == "menu":

    # 배경
    st.markdown(
        textwrap.dedent("""
        <div class="game-screen">

            <div class="ceiling"></div>

            <div class="wall-left"></div>

            <div class="wall-right"></div>

            <div class="hall-end"></div>

            <div class="floor"></div>

            <div class="floor-line-left"></div>
            <div class="floor-line-right"></div>

            <div class="light light1"></div>
            <div class="light light2"></div>
            <div class="light light3"></div>

            <div class="darkness"></div>

            <div class="title">
                휘명고등학교
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )


    # 버튼
    st.markdown(
        '<div class="menu-buttons">',
        unsafe_allow_html=True
    )

    if st.button(
        "새 게임 시작",
        key="new_game",
        use_container_width=True
    ):
        st.session_state.screen = "name"
        st.rerun()


    if st.button(
        "이어서 하기",
        key="continue_game",
        use_container_width=True
    ):
        st.toast("저장된 게임이 없습니다.")


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ==========================================
# 이름 입력
# ==========================================

elif st.session_state.screen == "name":

    st.markdown(
        """
        <div class="name-screen">

            <div class="name-title">
                당신의 이름을 입력하세요
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    name = st.text_input(
        "이름",
        placeholder="이름",
        label_visibility="collapsed"
    )


    if st.button(
        "게임 시작",
        use_container_width=True
    ):

        if name.strip() == "":
            st.warning("이름을 입력해주세요.")

        else:
            st.session_state.player_name = name.strip()
            st.session_state.screen = "game"
            st.rerun()


# ==========================================
# 게임 시작
# ==========================================

elif st.session_state.screen == "game":

    player_name = st.session_state.player_name

    st.markdown(
        f"""
        <div class="name-screen">

            <div style="
                font-size: 34px;
                letter-spacing: 3px;
            ">
                {player_name}의 이야기
            </div>

            <div style="
                margin-top: 25px;
                font-size: 18px;
                color: #737e7e;
            ">
                휘명고등학교
            </div>

            <div style="
                margin-top: 70px;
                font-size: 14px;
                color: #505959;
            ">
                게임이 시작됩니다...
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
