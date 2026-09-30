import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="모닥불 키우기",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 어두운 배경 및 8칸 정사각형 인벤토리 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경을 어두운 밤하늘 톤으로 설정 */
    .stApp {
        background-color: #12161f;
        color: #e2e8f0;
    }
    header, footer { visibility: hidden; }

    /* 중앙 모닥불 영역 */
    .fire-container {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 30px;
    }
    .fire-icon {
        font-size: 5rem;
        text-shadow: 0 0 25px rgba(255, 165, 0, 0.6);
        animation: pulse 2s infinite alternate;
    }
    .fire-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffb703;
        margin-top: 10px;
    }

    /* 하단 인벤토리 슬롯 (정사각형) */
    .slot-box {
        aspect-ratio: 1 / 1; /* 정사각형 비율 유지 */
        background-color: #1e2532;
        border: 2px solid #3b475d;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        color: #a0aec0;
        transition: all 0.2s ease;
        margin-bottom: 5px;
    }
    .slot-box:hover {
        border-color: #ffb703;
        background-color: #263042;
    }
    .slot-label {
        font-size: 0.7rem;
        color: #718096;
        margin-top: 2px;
    }
    .inventory-title {
        font-size: 0.9rem;
        color: #a0aec0;
        margin-bottom: 8px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


# 3. 게임 세션 상태 초기화 (8칸 인벤토리)
if "inventory" not in st.session_state:
    # 8칸 슬롯 (초기에는 비어있거나 기본 아이템 배치 가능)
    st.session_state.inventory = [
        {"icon": "🪵", "name": "장작", "count": 3},
        {"icon": "🍄", "name": "버섯", "count": 1},
        None, None, None, None, None, None  # 빈 슬롯들
    ]


# ---------------------------------------------------------
# 화면 레이아웃 구성
# ---------------------------------------------------------

# 1. 중앙 모닥불 배치
st.markdown("""
    <div class="fire-container">
        <div class="fire-icon">🔥</div>
        <div class="fire-title">작은 모닥불</div>
    </div>
""", unsafe_allow_html=True)

# 시각적 여백
st.write("")
st.write("")
st.divider()

# 2. 하단 인벤토리 (8개 정사각형 슬롯)
st.markdown('<div class="inventory-title">🎒 가방 (8칸)</div>', unsafe_allow_html=True)

# 8개 컬럼 생성
cols = st.columns(8)

for i in range(8):
    item = st.session_state.inventory[i]
    with cols[i]:
        if item:
            # 아이템이 들어있는 슬롯
            st.markdown(f"""
                <div class="slot-box">
                    <div>{item['icon']}</div>
                    <div class="slot-label">x{item['count']}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            # 빈 슬롯
            st.markdown("""
                <div class="slot-box">
                    <div style="font-size: 0.8rem; opacity: 0.3;">{i+1}</div>
                </div>
            """.format(i=i), unsafe_allow_html=True)
