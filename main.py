import streamlit as st
import random
import time

# ==========================================
# 기본 설정
# ==========================================

st.set_page_config(
    page_title="휘명고등학교",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    margin: 0;
    padding: 0;
}

.stApp {
    background: #050708;
}

/* 기본 여백 제거 */
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}


/* =========================================
   전체 화면
========================================= */

.game {
    position: relative;

    width: 100%;
    height: 100vh;

    overflow: hidden;

    background:
        linear-gradient(
            90deg,
            #0c1113 0%,
            #222c30 35%,
            #101618 50%,
            #222c30 65%,
            #0c1113 100%
        );
}


/* =========================================
   천장
========================================= */

.ceiling {
    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 40%;

    background:
        linear-gradient(
            to bottom,
            #111719,
            #273135,
            #141b1e
        );

    clip-path: polygon(
        0 0,
        100% 0,
        67% 100%,
        33% 100%
    );
}


/* =========================================
   왼쪽 벽
========================================= */

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


/* =========================================
   오른쪽 벽
========================================= */

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


/* =========================================
   복도 끝
========================================= */

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
            #080b0c 0%,
            #020303 70%,
            #000000 100%
        );

    box-shadow:
        0 0 80px rgba(0,0,0,0.9),
        inset 0 0 60px #000;
}


/* =========================================
   바닥
========================================= */

.floor {
    position: absolute;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 50%;

    background:
        linear-gradient(
            to bottom,
            #242c2f,
            #0b0f11
        );

    clip-path: polygon(
        33% 0,
        67% 0,
        100% 100%,
        0 100%
    );
}


/* =========================================
   형광등
========================================= */

.light {
    position: absolute;

    left: 50%;

    transform: translateX(-50%);

    height: 6px;

    background: #cbd3d2;

    box-shadow:
        0 0 12px rgba(220,235,235,0.6),
        0 0 35px rgba(180,210,210,0.2);
}

.light1 {
    top: 10%;
    width: 15%;
    opacity: 0.45;
}

.light2 {
    top: 21%;
    width: 10%;
    opacity: 0.35;
}

.light3 {
    top: 30%;
    width: 6%;
    opacity: 0.25;
}


/* =========================================
   어두운 가장자리
========================================= */

.darkness {
    position: absolute;

    inset: 0;

    background:
        radial-gradient(
            ellipse at center,
            transparent 15%,
            rgba(0,0,0,0.3) 55%,
            rgba(0,0,0,0.88) 100%
        );

    pointer-events: none;
}


/* =========================================
   메뉴
========================================= */

.menu {
    position: absolute;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);

    text-align: center;

    width: 100%;

    z-index: 10;
}


/* 제목 */

.title {
    color: #e1e6e6;

    font-family:
        "Noto Serif KR",
        "Malgun Gothic",
        serif;

    font-size: clamp(40px, 6vw, 80px);

    font-weight: 400;

    letter-spacing: 14px;

    text-shadow:
        0 0 15px rgba(255,255,255,0.12);
}


/* =========================================
   버튼
========================================= */

.stButton > button {

    width: 250px !important;
    height: 55px !important;

    background: rgba(5,8,9,0.75) !important;

    color: #d8dfdf !important;

    border: 1px solid rgba(210,220,220,0.3) !important;

    border-radius: 0 !important;

    font-family:
        "Malgun Gothic",
        sans-serif !important;

    font-size: 16px !important;

    letter-spacing: 4px !important;

    transition: all 0.3s ease !important;
}


.stButton > button:hover {

    background: rgba(180,200,200,0.12) !important;

    border-color: rgba(230,240,240,0.7) !important;

    color: white !important;

    transform: translateY(-2px);
}


/* 버튼 간격 */

.buttons {
    margin-top: 70px;
}


/* =========================================
   이름 입력 화면
========================================= */

.name-screen {

    position: absolute;

    inset: 0;

    z-index: 20;

    background:
        radial-gradient(
            ellipse at center,
            #111719,
            #020304
        );

    display: flex;

    justify-content: center;

    align-items: center;

    text-align: center;
}


.name-title {

    color: #dfe5e5;

    font-size: 26px;

    letter-spacing: 3px;

    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 세션 상태
# ==========================================

if "screen" not in st.session_state:
    st.session_state.screen = "menu"

if "player_name" not in st.session_state:
    st.session_state.player_name = ""


# ==========================================
# 메인 메뉴
# ==========================================

if st.session_state.screen == "menu":

    st.markdown("""
    <div class="game">

        <div class="ceiling"></div>

        <div class="wall-left"></div>

        <div class="wall-right"></div>

        <div class="hall-end"></div>

        <div class="floor"></div>

        <div class="light light1"></div>
        <div class="light light2"></div>
        <div class="light light3"></div>

        <div class="darkness"></div>

        <div class="menu">

            <div class="title">
                휘명고등학교
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    # 버튼을 화면 아래쪽에 배치
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:

        st.markdown(
            '<div class="buttons"></div>',
            unsafe_allow_html=True
        )

        if st.button(
            "새 게임 시작",
            use_container_width=True
        ):
            st.session_state.screen = "name"
            st.rerun()


        if st.button(
            "이어서 하기",
            use_container_width=True
        ):
            st.info("저장된 게임이 없습니다.")


# ==========================================
# 이름 입력
# ==========================================

elif st.session_state.screen == "name":

    st.markdown("""
    <div class="name-screen">

        <div>

            <div class="name-title">
                당신의 이름을 입력하세요
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    name = st.text_input(
        "이름",
        placeholder="이름을 입력하세요",
        label_visibility="collapsed"
    )


    if st.button("게임 시작"):

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

    st.markdown("""
    <style>

    .game-start {

        height: 80vh;

        display: flex;

        flex-direction: column;

        justify-content: center;

        align-items: center;

        background: #050708;

        color: #dfe5e5;

        text-align: center;

    }

    </style>
    """, unsafe_allow_html=True)


    st.markdown(
        f"""
        <div class="game-start">

            <div style="font-size:34px;">
                {st.session_state.player_name}의 이야기
            </div>

            <div style="
                margin-top:25px;
                font-size:18px;
                color:#737e7e;
            ">
                휘명고등학교
            </div>

            <div style="
                margin-top:70px;
                font-size:14px;
                color:#505959;
            ">
                게임이 시작됩니다...
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )
