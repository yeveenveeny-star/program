import random
import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="모닥불 키우기",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# 커스텀 이미지 URL 설정 (본인 이미지로 교체 가능)
# ---------------------------------------------------------
# 숲 배경 이미지 (Unsplash 무료 이미지)
BG_IMAGE_URL = "https://images.unsplash.com/photo-1511497584788-8767611136f6?q=80&w=1200&auto=format&fit=crop"

# 타오르는 모닥불 GIF 이미지
FIRE_GIF_URL = "https://media.giphy.com/media/3o72FfM5HJydzaMpf2/giphy.gif"


# 2. CSS 스타일링 (스크롤 방지 콤팩트 레이아웃 + 숲 배경)
st.markdown(
    f"""
    <style>
    /* 전체 배경을 숲 이미지로 설정 */
    .stApp {{
        background: linear-gradient(rgba(18, 22, 31, 0.75), rgba(18, 22, 31, 0.85)),
                    url('{BG_IMAGE_URL}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #e2e8f0;
    }}
    header, footer {{ visibility: hidden; }}

    /* 메인 블록 여백 줄이기 (스크롤 방지 핵심) */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        max-width: 650px !important;
    }}

    /* 중앙 모닥불 영역 */
    .fire-container {{
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }}
    .fire-img {{
        width: 130px;
        height: 130px;
        object-fit: contain;
        filter: drop-shadow(0 0 18px rgba(255, 165, 0, 0.8));
    }}
    .fire-title {{
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffb703;
        margin-top: 5px;
    }}
    .fire-stats {{
        font-size: 0.9rem;
        color: #ffaaa5;
        font-weight: 600;
        margin-top: 2px;
    }}

    /* 탐색 버튼 콤팩트 디자인 */
    div[data-testid="stButton"] > button.gather-btn {{
        background-color: #2d3748 !important;
        color: #e2e8f0 !important;
        border: 1px solid #4a5568 !important;
        padding: 4px 12px !important;
        font-size: 0.85rem !important;
        height: auto !important;
        aspect-ratio: auto !important;
        border-radius: 6px !important;
        margin: 0 auto;
        display: block;
    }}
    div[data-testid="stButton"] > button.gather-btn:hover {{
        background-color: #4a5568 !important;
        border-color: #ffb703 !important;
    }}

    /* 하단 인벤토리 슬롯 (정사각형 버튼) */
    .stButton > button {{
        width: 100% !important;
        aspect-ratio: 1 / 1 !important;
        height: auto !important;
        background-color: rgba(30, 37, 50, 0.85) !important;
        border: 2px solid #3b475d !important;
        border-radius: 8px !important;
        color: #e2e8f0 !important;
        font-size: 1.1rem !important;
        padding: 0 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        line-height: 1.1 !important;
        transition: all 0.15s ease !important;
    }}
    .stButton > button:hover {{
        border-color: #ffb703 !important;
        background-color: rgba(38, 48, 66, 0.95) !important;
    }}

    .inventory-title {{
        font-size: 0.85rem;
        color: #cbd5e0;
        margin-top: 15px;
        margin-bottom: 8px;
        text-align: center;
    }}
    
    /* Divider 간격 감소 */
    hr {{
        margin: 10px 0 !important;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# 3. 게임 세션 상태 초기화
if "fire_level" not in st.session_state:
    st.session_state.fire_level = 10

if "inventory" not in st.session_state:
    st.session_state.inventory = [
        {"icon": "🪵", "name": "장작", "count": 3, "value": 10},
        {"icon": "🍄", "name": "버섯", "count": 1, "value": 5},
        None,
        None,
        None,
        None,
        None,
        None,
    ]

if "log_msg" not in st.session_state:
    st.session_state.log_msg = "숲속의 조용한 밤, 모닥불이 피어오릅니다."


# --- 게임 로직 함수 ---
def use_item(index):
    item = st.session_state.inventory[index]
    if item:
        st.session_state.fire_level += item["value"]
        item["count"] -= 1
        st.session_state.log_msg = (
            f"🔥 {item['name']}을(를) 모닥불에 넣어 온기 +{item['value']}℃"
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

    for slot in st.session_state.inventory:
        if slot and slot["name"] == found["name"]:
            slot["count"] += 1
            st.session_state.log_msg = (
                f"🌲 탐색 결과: {found['icon']} {found['name']} 획득!"
            )
            return

    for i in range(8):
        if st.session_state.inventory[i] is None:
            st.session_state.inventory[i] = found.copy()
            st.session_state.log_msg = (
                f"🌲 탐색 결과: {found['icon']} {found['name']} 획득!"
            )
            return

    st.session_state.log_msg = "🎒 가방이 가득 찼습니다!"


# ---------------------------------------------------------
# 화면 레이아웃 구성
# ---------------------------------------------------------

# 1. 중앙 모닥불 (GIF 이미지 적용)
st.markdown(
    f"""
    <div class="fire-container">
        <img src="{FIRE_GIF_URL}" class="fire-img" alt="모닥불" />
        <div class="fire-title">작은 모닥불</div>
        <div class="fire-stats">온기: {st.session_state.fire_level} ℃</div>
    </div>
""",
    unsafe_allow_html=True,
)

# 알림 메시지 (상단 배치)
st.info(st.session_state.log_msg)

# 2. 작은 탐색 버튼
col_left, col_btn, col_right = st.columns([1, 2, 1])
with col_btn:
    if st.button("🌲 주변 탐색 (아이템 채집)", key="gather_btn"):
        gather_resource()
        st.rerun()

st.divider()

# 3. 하단 인벤토리 (8칸)
st.markdown(
    '<div class="inventory-title">🎒 가방 (아이템 클릭 시 모닥불에 사용)</div>',
    unsafe_allow_html=True,
)

cols = st.columns(8)

for i in range(8):
    item = st.session_state.inventory[i]
    with cols[i]:
        if item:
            button_label = f"{item['icon']}\nx{item['count']}"
            if st.button(button_label, key=f"slot_{i}"):
                use_item(i)
                st.rerun()
        else:
            st.button(f"{i+1}", key=f"slot_{i}", disabled=True)
