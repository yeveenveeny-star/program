import random
import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="모닥불 키우기",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. 어두운 배경 및 커스텀 버튼/인벤토리 CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #12161f;
        color: #e2e8f0;
    }
    header, footer { visibility: hidden; }

    /* 중앙 모닥불 영역 */
    .fire-container {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .fire-icon {
        font-size: 5rem;
        text-shadow: 0 0 25px rgba(255, 165, 0, 0.7);
        animation: pulse 2s infinite alternate;
    }
    .fire-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffb703;
        margin-top: 5px;
    }
    .fire-stats {
        font-size: 0.95rem;
        color: #f77f00;
        margin-top: 8px;
    }

    /* 하단 인벤토리 슬롯 (정사각형 버튼) */
    .stButton > button {
        width: 100% !important;
        aspect-ratio: 1 / 1 !important;
        height: auto !important;
        background-color: #1e2532 !important;
        border: 2px solid #3b475d !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
        font-size: 1.2rem !important;
        padding: 0 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        line-height: 1.2 !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        border-color: #ffb703 !important;
        background-color: #263042 !important;
        transform: translateY(-2px);
    }
    .stButton > button:active {
        transform: translateY(0);
    }

    .inventory-title {
        font-size: 0.9rem;
        color: #a0aec0;
        margin-bottom: 12px;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. 게임 세션 상태 초기화
if "fire_level" not in st.session_state:
    st.session_state.fire_level = 10  # 모닥불 온기(체력)

if "inventory" not in st.session_state:
    st.session_state.inventory = [
        {"icon": "🪵", "name": "장작", "count": 3, "value": 10},
        {"icon": "🍄", "name": "버섯", "count": 1, "value": 5},
        None,
        None,
        None,
        None,
        None,
        None,  # 8칸 슬롯
    ]

if "log_msg" not in st.session_state:
    st.session_state.log_msg = "불꽃이 은은하게 타오르고 있습니다."


# --- 게임 로직 함수 ---
def use_item(index):
    item = st.session_state.inventory[index]
    if item:
        st.session_state.fire_level += item["value"]
        item["count"] -= 1
        st.session_state.log_msg = (
            f"🔥 {item['name']}을(를) 모닥불에 넣어 온기가 +{item['value']} 상승했습니다!"
        )

        if item["count"] <= 0:
            st.session_state.inventory[index] = None


def gather_resource():
    item_pool = [
        {"icon": "🪵", "name": "장작", "count": 1, "value": 10},
        {"icon": "🍄", "name": "버섯", "count": 1, "value": 5},
        {"icon": "🌿", "name": "약초", "count": 1, "value": 8},
    ]
    found = random.choice(item_pool)

    # 1. 이미 존재하는 같은 아이템 수량 증가
    for slot in st.session_state.inventory:
        if slot and slot["name"] == found["name"]:
            slot["count"] += 1
            st.session_state.log_msg = (
                f"🌲 주변을 탐색해 {found['icon']} {found['name']}을(를) 획득했습니다!"
            )
            return

    # 2. 빈 슬롯에 새 아이템 추가
    for i in range(8):
        if st.session_state.inventory[i] is None:
            st.session_state.inventory[i] = found.copy()
            st.session_state.log_msg = (
                f"🌲 주변을 탐색해 {found['icon']} {found['name']}을(를) 획득했습니다!"
            )
            return

    # 3. 인벤토리가 가득 찬 경우
    st.session_state.log_msg = "🎒 가방이 가득 차서 더 이상 주울 수 없습니다!"


# ---------------------------------------------------------
# 화면 레이아웃 구성
# ---------------------------------------------------------

# 1. 중앙 모닥불 배치
st.markdown(
    f"""
    <div class="fire-container">
        <div class="fire-icon">🔥</div>
        <div class="fire-title">작은 모닥불</div>
        <div class="fire-stats">모닥불 온기: {st.session_state.fire_level} ℃</div>
    </div>
""",
    unsafe_allow_html=True,
)

# 알림 메시지 출력
st.info(st.session_state.log_msg)

# 탐색(채집) 버튼
if st.button("🌲 주변 탐색하기 (아이템 채집)", use_container_width=True):
    gather_resource()
    st.rerun()

st.write("")
st.divider()

# 2. 하단 인벤토리 (8개 정사각형 클릭 버튼 슬롯)
st.markdown(
    '<div class="inventory-title">🎒 가방 (슬롯을 클릭하면 모닥불에 투입됩니다)</div>',
    unsafe_allow_html=True,
)

cols = st.columns(8)

for i in range(8):
    item = st.session_state.inventory[i]
    with cols[i]:
        if item:
            # 아이템 클릭 시 모닥불에 사용
            button_label = f"{item['icon']}\nx{item['count']}"
            if st.button(button_label, key=f"slot_{i}"):
                use_item(i)
                st.rerun()
        else:
            # 빈 슬롯 클릭 시 반응 없음
            st.button(f"{i+1}", key=f"slot_{i}", disabled=True)
