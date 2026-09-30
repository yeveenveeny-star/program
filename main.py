import random
import time
import streamlit as st

# ---------------------------------------------------------
# 1. 페이지 및 분위기 있는 파스텔 CSS 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="신비한 모닥불과 밤의 숲",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0f141d;
        color: #e2e8f0;
    }
    header, footer { visibility: hidden; }

    /* 메인 타이틀 */
    .title-text {
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        color: #ffb703;
        letter-spacing: 2px;
        margin-top: 30px;
        margin-bottom: 10px;
        text-shadow: 0 0 20px rgba(255, 183, 3, 0.4);
    }

    /* 대사 및 카드 */
    .dialogue-card {
        background: linear-gradient(180deg, #18202c 0%, #111620 100%);
        border: 1.5px solid #fb8500;
        border-radius: 16px;
        padding: 20px;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
    }
    .fire-spirit {
        color: #ffb703;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }

    /* 버튼 커스텀 */
    div.stButton > button {
        width: 100%;
        background-color: #1f2937;
        color: #ffb703;
        border: 1.5px solid #fb8500;
        padding: 12px 18px;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: 600;
        transition: all 0.25s ease;
    }
    div.stButton > button:hover {
        background-color: #fb8500;
        color: #0f141d;
        box-shadow: 0 0 15px rgba(251, 133, 0, 0.4);
    }
    </style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# 2. 게임 데이터베이스 (아이템 및 모닥불 선물 테이블)
# ---------------------------------------------------------
HUNT_ITEMS = {
    "🪵 바싹 마른 장작": {"exp": 15, "rarity": "일반", "desc": "기본적인 모닥불의 먹이."},
    "🍄 야광 버섯": {"exp": 25, "rarity": "일반", "desc": "신비한 푸른빛을 내는 버섯."},
    "🥩 숲토끼 고기": {"exp": 40, "rarity": "희귀", "desc": "사냥으로 얻은 신선한 고기. 불꽃이 아주 좋아합니다."},
    "🔮 달빛 결정 열매": {"exp": 70, "rarity": "전설", "desc": "밤의 숲 깊은 곳에서만 자라는 전설의 열매."}
}

FIRE_GIFTS = {
    "일반": ["🍵 따스한 찻잎", "✨ 작은 별가루", "🪵 바싹 탄 숯 조각"],
    "희귀": ["💎 붉은 화염 보석", "🕯️ 정령의 은은한 등불", "📜 잊혀진 숲의 지도"],
    "전설": ["👑 불꽃 정령의 왕관", "💖 영원히 꺼지지 않는 불씨", "🌟 밤하늘의 조각"]
}


# ---------------------------------------------------------
# 3. 게임 상태(Session State) 초기화
# ---------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "title"

if "state" not in st.session_state:
    st.session_state.state = {
        "fire_level": 1,        # 모닥불 레벨 (1~5)
        "fire_exp": 0,          # 현재 경험치
        "inventory": {"🪵 바싹 마른 장작": 2}, # 인벤토리 (아이템: 개수)
        "gifts": set(),         # 받은 선물들
        "last_msg": "모닥불이 기분 좋게 타오르고 있습니다."
    }

S = st.session_state.state


# ---------------------------------------------------------
# 4. 헬퍼 함수
# ---------------------------------------------------------
def get_fire_appearance(level):
    """레벨별 모닥불 시각화 모습"""
    appearances = {
        1: ("🔥 [LV.1 아기 모닥불]", "작고 귀여운 불꽃이 조용히 flicker거립니다."),
        2: ("🔥 [LV.2 따스한 모닥불]", "주변을 환하게 비출 만큼 불꽃이 꽤 커졌습니다."),
        3: ("💥 [LV.3 활활 타오르는 불꽃]", "강렬한 온기와 신비로운 정령의 기운이 느껴집니다."),
        4: ("🌟 [LV.4 거대한 정령의 불길]", "마치 살아있는 생명체처럼 불꽃이 춤을 춥니다."),
        5: ("👑 [LV.5 전설의 태양 불꽃]", "숲 전체를 따뜻하게 감싸는 커다란 불꽃입니다!")
    }
    return appearances.get(level, appearances[1])


def feed_fire(item_name):
    """모닥불에게 먹이(아이템) 주기 로직"""
    if S["inventory"].get(item_name, 0) > 0:
        S["inventory"][item_name] -= 1
        if S["inventory"][item_name] == 0:
            del S["inventory"][item_name]

        item_data = HUNT_ITEMS[item_name]
        exp_gained = item_data["exp"]
        rarity = item_data["rarity"]

        S["fire_exp"] += exp_gained

        # 레벨업 체크 (레벨당 필요 EXP: 50 * level)
        needed_exp = S["fire_level"] * 50
        leveled_up = False
        if S["fire_exp"] >= needed_exp and S["fire_level"] < 5:
            S["fire_level"] += 1
            S["fire_exp"] -= needed_exp
            leveled_up = True

        # 선물 생성
        gift = random.choice(FIRE_GIFTS[rarity])
        S["gifts"].add(gift)

        # 메시지 구성
        msg = f"<b>[{item_name}]</b>을(를) 모닥불에게 바쳤습니다! (+{exp_gained} EXP)<br>"
        if leveled_up:
            msg += f"✨ <b>축하합니다! 모닥불이 성장하여 LV.{S['fire_level']}이 되었습니다!</b><br>"
        msg += f"🎁 모닥불이 고마워하며 <b>[{gift}]</b>을(를) 선물로 내어주었습니다!"
        
        S["last_msg"] = msg
        return True
    return False


# ---------------------------------------------------------
# 5. 화면 로직
# ---------------------------------------------------------

# --- A. 타이틀 화면 ---
if st.session_state.page == "title":
    st.markdown('<div class="title-text">신비한 모닥불과 밤의 숲 🔥</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="dialogue-card" style="text-align: center;">
            어두운 밤숲 한가운데, 살아있는 작은 불꽃 정령이 기다리고 있습니다.<br>
            숲속에서 사냥하고 수집한 아이템을 모닥불에게 먹여보세요.<br>
            불꽃이 자라나며 당신에게 보답으로 특별한 선물을 줄 것입니다.
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔥 모닥불 찾아가기"):
            st.session_state.page = "game"
            st.rerun()

# --- B. 게임 메인 화면 ---
elif st.session_state.page == "game":
    fire_title, fire_desc = get_fire_appearance(S["fire_level"])
    
    # 1. 모닥불 상태 표시
    st.subheader(fire_title)
    st.caption(fire_desc)
    
    needed_exp = S["fire_level"] * 50
    st.progress(min(1.0, S["fire_exp"] / needed_exp), text=f"불꽃 성장도: {S['fire_exp']} / {needed_exp} EXP")

    # 2. 대사/메시지 상자
    st.markdown(f"""
        <div class="dialogue-card">
            <div class="fire-spirit">🔥 모닥불 정령</div>
            <div style="line-height: 1.6;">{S['last_msg']}</div>
        </div>
    """, unsafe_allow_html=True)

    # 3. 탭 구성 (먹이주기 / 숲 사냥하기)
    tab1, tab2 = st.tabs(["🔥 모닥불에게 먹이주기", "🏹 밤의 숲 탐험/사냥"])

    # [탭 1: 먹이주기]
    with tab1:
        st.write("가방에 있는 아이템을 모닥불에게 바쳐 불꽃을 키웁니다.")
        if S["inventory"]:
            for item, count in list(S["inventory"].items()):
                col_item, col_btn = st.columns([3, 1])
                with col_item:
                    rarity = HUNT_ITEMS[item]["rarity"]
                    st.write(f"**{item}** x{count}개 `[{rarity}]` - EXP +{HUNT_ITEMS[item]['exp']}")
                with col_btn:
                    if st.button("먹이기", key=f"feed_{item}"):
                        feed_fire(item)
                        st.rerun()
        else:
            st.info("가방이 비어있습니다. '밤의 숲 탐험/사냥' 탭에서 아이템을 얻어오세요!")

    # [탭 2: 숲 사냥/채집]
    with tab2:
        st.write("어두운 숲속으로 들어가 모닥불이 먹을 만한 물건을 찾아옵니다.")
        
        col_hunt1, col_hunt2 = st.columns(2)
        with col_hunt1:
            if st.button("🍃 숲 근처 수풀 채집"):
                found_item = random.choice(["🪵 바싹 마른 장작", "🍄 야광 버섯"])
                S["inventory"][found_item] = S["inventory"].get(found_item, 0) + 1
                S["last_msg"] = f"숲 근처에서 <b>[{found_item}]</b>을(를) 주웠습니다!"
                st.rerun()

        with col_hunt2:
            if st.button("🏹 숲 깊은 곳 사냥하기"):
                # 확률형 사냥 (성공/희귀)
                rand_val = random.random()
                if rand_val < 0.6:
                    found_item = "🥩 숲토끼 고기"
                elif rand_val < 0.9:
                    found_item = "🍄 야광 버섯"
                else:
                    found_item = "🔮 달빛 결정 열매"

                S["inventory"][found_item] = S["inventory"].get(found_item, 0) + 1
                S["last_msg"] = f"깊은 숲속을 수색하여 희귀한 <b>[{found_item}]</b>을(를) 획득했습니다!"
                st.rerun()

    # 4. 하단 보물 상자 (받은 선물들)
    st.divider()
    st.subheader("🎁 모닥불에게 받은 선물 도감")
    if S["gifts"]:
        for g in S["gifts"]:
            st.write(f"- {g}")
    else:
        st.caption("아직 모닥불에게 받은 선물이 없습니다. 아이템을 바쳐보세요!")

    if st.button("🏠 메인 화면으로"):
        st.session_state.page = "title"
        st.rerun()
