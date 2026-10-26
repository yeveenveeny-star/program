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

    /* 화면 전체를 중앙 정렬하는 Flex 컨테이너 */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        max-width: 600px;
        margin: 30px auto;
    }

    /* 우체통 전체 (헤드 + 몸통 + 받침대) */
    .mailbox-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
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

    /* 텍스트 입력 영역 너비를 절반(160px)으로 설정 및 중앙 정렬 */
    .input-wrapper {
        width: 160px;
        max-width: 100%;
    }

    /* 텍스트 입력창 스타일 커스텀 */
    div.stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #4A4A4A !important;
        font-family: 'Malgun Gothic', sans-serif !important;
        font-size: 0.9rem !important;
        border-
