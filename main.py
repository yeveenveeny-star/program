from http.server import HTTPServer, BaseHTTPRequestHandler


HTML = """
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
    color: white;
    font-family: sans-serif;
}

/* 전체 화면 */
.screen {
    width: 100vw;
    height: 100vh;
    position: relative;
    overflow: hidden;

    background:
        linear-gradient(
            to bottom,
            #11191d 0%,
            #202a2e 40%,
            #101517 100%
        );
}

/* 복도 */
.corridor {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            #101619 0%,
            #263237 35%,
            #111719 50%,
            #263237 65%,
            #101619 100%
        );
}

/* 복도 끝 */
.end {
    position: absolute;

    left: 50%;
    top: 25%;

    transform: translateX(-50%);

    width: 18%;
    height: 48%;

    background: #020303;

    box-shadow:
        0 0 80px rgba(0,0,0,0.9),
        inset 0 0 40px #000;
}

/* 바닥 */
.floor {
    position: absolute;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 48%;

    background:
        linear-gradient(
            to bottom,
            #272f32,
            #0c1012
        );

    clip-path: polygon(
        32% 0,
        68% 0,
        100% 100%,
        0 100%
    );
}

/* 형광등 */
.light {
    position: absolute;

    left: 50%;
    transform: translateX(-50%);

    height: 6px;

    background: #d9e0df;

    box-shadow:
        0 0 15px rgba(220,235,235,0.5);

    opacity: 0.4;
}

.light1 {
    top: 12%;
    width: 14%;
}

.light2 {
    top: 23%;
    width: 9%;
}

.light3 {
    top: 32%;
    width: 5%;
}

/* 어두운 가장자리 */
.dark {
    position: absolute;
    inset: 0;

    background:
        radial-gradient(
            ellipse at center,
            transparent 20%,
            rgba(0,0,0,0.3) 55%,
            rgba(0,0,0,0.9) 100%
        );
}

/* 메뉴 */
.menu {
    position: absolute;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);

    text-align: center;

    width: 100%;
}

/* 제목 */
.title {
    font-family: serif;

    font-size: 70px;

    font-weight: normal;

    letter-spacing: 12px;

    color: #e1e6e6;

    text-shadow:
        0 0 20px rgba(255,255,255,0.15);
}

/* 버튼 */
.buttons {
    margin-top: 70px;

    display: flex;
    flex-direction: column;

    align-items: center;

    gap: 18px;
}

button {
    width: 240px;
    height: 55px;

    background: rgba(5,8,9,0.65);

    border: 1px solid rgba(220,230,230,0.3);

    color: #dce2e2;

    font-size: 16px;

    letter-spacing: 4px;

    cursor: pointer;

    transition: 0.3s;
}

button:hover {
    background: rgba(180,200,200,0.12);

    border-color: rgba(230,240,240,0.7);

    color: white;

    transform: translateY(-2px);

    box-shadow:
        0 0 25px rgba(200,220,220,0.1);
}

</style>
</head>


<body>

<div class="screen">

    <div class="corridor"></div>

    <div class="end"></div>

    <div class="floor"></div>

    <div class="light light1"></div>
    <div class="light light2"></div>
    <div class="light light3"></div>

    <div class="dark"></div>


    <div class="menu">

        <div class="title">
            휘명고등학교
        </div>


        <div class="buttons">

            <button onclick="newGame()">
                새 게임 시작
            </button>

            <button onclick="continueGame()">
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

    alert("저장된 게임을 불러옵니다.");

}

</script>

</body>
</html>
"""


class GameHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            HTML.encode("utf-8")
        )


server = HTTPServer(
    ("localhost", 8000),
    GameHandler
)

print("게임 실행 중...")
print("http://localhost:8000")

server.serve_forever()
