<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>휘명고등학교</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            background: #050607;
            font-family: "Noto Sans KR", sans-serif;
            color: white;
        }

        /* =========================
           복도 배경
        ========================= */

        .game-screen {
            position: relative;
            width: 100%;
            height: 100%;
            overflow: hidden;

            background:
                linear-gradient(
                    rgba(3, 6, 8, 0.45),
                    rgba(2, 4, 6, 0.75)
                ),
                linear-gradient(
                    90deg,
                    #11191d 0%,
                    #253138 35%,
                    #11181c 50%,
                    #253138 65%,
                    #11191d 100%
                );
        }

        /* 복도 천장 */
        .ceiling {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 38%;

            background:
                linear-gradient(
                    to bottom,
                    #11181b,
                    #293237 70%,
                    #151b1e
                );

            clip-path: polygon(
                0 0,
                100% 0,
                67% 100%,
                33% 100%
            );
        }

        /* 복도 바닥 */
        .floor {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 48%;

            background:
                linear-gradient(
                    to bottom,
                    #252d30,
                    #101416 80%
                );

            clip-path: polygon(
                33% 0,
                67% 0,
                100% 100%,
                0 100%
            );
        }

        /* 복도 양쪽 벽 */
        .wall-left,
        .wall-right {
            position: absolute;
            top: 20%;
            width: 35%;
            height: 55%;
            background: #182024;
        }

        .wall-left {
            left: 0;
            clip-path: polygon(0 0, 100% 25%, 100% 100%, 0 100%);
        }

        .wall-right {
            right: 0;
            clip-path: polygon(0 25%, 100% 0, 100% 100%, 0 100%);
        }

        /* 복도 끝 */
        .hall-end {
            position: absolute;
            left: 50%;
            top: 27%;
            transform: translateX(-50%);

            width: 18%;
            height: 43%;

            background:
                radial-gradient(
                    ellipse at center,
                    #080b0d 0%,
                    #020304 65%,
                    #000000 100%
                );

            box-shadow:
                0 0 50px rgba(0, 0, 0, 0.9),
                inset 0 0 50px rgba(0, 0, 0, 0.9);
        }

        /* 천장 형광등 */
        .light {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);

            width: 8%;
            height: 7px;

            background: #cbd3d3;

            box-shadow:
                0 0 10px rgba(220, 235, 235, 0.6),
                0 0 30px rgba(180, 210, 210, 0.25);

            opacity: 0.65;
        }

        .light1 {
            top: 11%;
            width: 15%;
            opacity: 0.4;
        }

        .light2 {
            top: 22%;
            width: 10%;
            opacity: 0.35;
        }

        .light3 {
            top: 31%;
            width: 6%;
            opacity: 0.28;
        }

        /* 복도 원근선 */
        .perspective-line {
            position: absolute;
            left: 50%;
            top: 27%;

            width: 2px;
            height: 73%;

            background: rgba(0, 0, 0, 0.3);

            transform-origin: top;
        }

        .line-left {
            transform: rotate(34deg);
        }

        .line-right {
            transform: rotate(-34deg);
        }

        /* =========================
           어두운 비네팅
        ========================= */

        .darkness {
            position: absolute;
            inset: 0;

            background:
                radial-gradient(
                    ellipse at center,
                    transparent 20%,
                    rgba(0, 0, 0, 0.25) 55%,
                    rgba(0, 0, 0, 0.85) 100%
                );

            pointer-events: none;
        }

        /* =========================
           메인 UI
        ========================= */

        .menu {
            position: absolute;
            z-index: 10;

            top: 50%;
            left: 50%;

            transform: translate(-50%, -50%);

            width: 100%;
            text-align: center;
        }

        .title {
            font-family: "Noto Serif KR", serif;

            font-size: clamp(42px, 6vw, 86px);
            font-weight: 500;
            letter-spacing: 12px;

            color: #e3e7e7;

            text-shadow:
                0 0 10px rgba(255,255,255,0.12),
                0 0 30px rgba(150,180,180,0.08);

            animation: titleFade 3s ease-in-out infinite alternate;
        }

        .subtitle {
            margin-top: 15px;

            font-size: 12px;
            letter-spacing: 6px;

            color: rgba(210,220,220,0.45);
        }

        .buttons {
            margin-top: 70px;

            display: flex;
            flex-direction: column;
            align-items: center;

            gap: 18px;
        }

        .menu-button {
            width: 240px;
            height: 55px;

            background: rgba(10, 14, 16, 0.55);

            border: 1px solid rgba(200, 210, 210, 0.22);

            color: rgba(230,235,235,0.85);

            font-size: 16px;
            letter-spacing: 4px;

            cursor: pointer;

            transition:
                background 0.3s,
                border-color 0.3s,
                color 0.3s,
                transform 0.3s,
                box-shadow 0.3s;
        }

        .menu-button:hover {
            background: rgba(160, 180, 180, 0.12);

            border-color: rgba(220, 230, 230, 0.55);

            color: white;

            transform: translateY(-2px);

            box-shadow:
                0 0 20px rgba(180,200,200,0.08);
        }

        .menu-button:active {
            transform: translateY(0);
        }

        /* =========================
           애니메이션
        ========================= */

        @keyframes titleFade {
            from {
                opacity: 0.82;
            }

            to {
                opacity: 1;
            }
        }

        /* 형광등 미세한 깜빡임 */
        .light1 {
            animation: flicker 6s infinite;
        }

        .light2 {
            animation: flicker 4.5s infinite;
        }

        @keyframes flicker {
            0%, 94%, 100% {
                opacity: 0.35;
            }

            95% {
                opacity: 0.08;
            }

            96% {
                opacity: 0.35;
            }

            97% {
                opacity: 0.15;
            }

            98% {
                opacity: 0.35;
            }
        }

        /* 모바일 */
        @media (max-width: 600px) {
            .title {
                letter-spacing: 6px;
            }

            .menu-button {
                width: 210px;
            }
        }
    </style>
</head>

<body>

    <div class="game-screen">

        <!-- 복도 배경 -->
        <div class="ceiling"></div>

        <div class="wall-left"></div>
        <div class="wall-right"></div>

        <div class="hall-end"></div>

        <div class="floor"></div>

        <!-- 천장 형광등 -->
        <div class="light light1"></div>
        <div class="light light2"></div>
        <div class="light light3"></div>

        <!-- 원근선 -->
        <div class="perspective-line line-left"></div>
        <div class="perspective-line line-right"></div>

        <!-- 어두운 화면 효과 -->
        <div class="darkness"></div>

        <!-- 메인 메뉴 -->
        <div class="menu">

            <h1 class="title">휘명고등학교</h1>

            <div class="subtitle">
                WHIMYEONG HIGH SCHOOL
            </div>

            <div class="buttons">

                <button
                    class="menu-button"
                    onclick="newGame()">
                    새 게임 시작
                </button>

                <button
                    class="menu-button"
                    onclick="continueGame()">
                    이어서 하기
                </button>

            </div>
        </div>

    </div>


    <script>

        function newGame() {
            alert("새 게임을 시작합니다.");
        }

        function continueGame() {
            alert("저장된 게임을 확인합니다.");
        }

    </script>

</body>
</html>
