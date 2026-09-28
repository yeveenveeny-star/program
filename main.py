import tkinter as tk
import math


# ==============================
# 기본 설정
# ==============================

WIDTH = 1200
HEIGHT = 700


root = tk.Tk()
root.title("휘명고등학교")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)


# ==============================
# 화면
# ==============================

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    highlightthickness=0,
    bg="#050708"
)

canvas.pack()


# ==============================
# 배경
# ==============================

# 전체 배경
canvas.create_rectangle(
    0, 0,
    WIDTH, HEIGHT,
    fill="#111719",
    outline=""
)


# 천장
canvas.create_polygon(
    0, 0,
    WIDTH, 0,
    800, 300,
    400, 300,
    fill="#20282b",
    outline=""
)


# 왼쪽 벽
canvas.create_polygon(
    0, 150,
    400, 300,
    400, HEIGHT,
    0, HEIGHT,
    fill="#151d20",
    outline=""
)


# 오른쪽 벽
canvas.create_polygon(
    WIDTH, 150,
    800, 300,
    800, HEIGHT,
    WIDTH, HEIGHT,
    fill="#151d20",
    outline=""
)


# ==============================
# 복도 끝
# ==============================

canvas.create_rectangle(
    400, 300,
    800, 650,
    fill="#030405",
    outline=""
)


# 복도 끝의 더 깊은 어둠
canvas.create_rectangle(
    500, 350,
    700, 650,
    fill="#000000",
    outline=""
)


# ==============================
# 바닥
# ==============================

canvas.create_polygon(
    400, 300,
    800, 300,
    WIDTH, HEIGHT,
    0, HEIGHT,
    fill="#202729",
    outline=""
)


# 바닥 중앙 어두운 부분
canvas.create_polygon(
    500, 300,
    700, 300,
    850, HEIGHT,
    350, HEIGHT,
    fill="#111617",
    outline=""
)


# ==============================
# 복도 타일 / 원근선
# ==============================

for i in range(1, 8):

    y = 300 + i * 55

    canvas.create_line(
        400 - i * 55,
        y,
        800 + i * 55,
        y,
        fill="#151b1d",
        width=2
    )


# 왼쪽 원근선
canvas.create_line(
    400, 300,
    0, HEIGHT,
    fill="#111719",
    width=3
)


# 오른쪽 원근선
canvas.create_line(
    800, 300,
    WIDTH, HEIGHT,
    fill="#111719",
    width=3
)


# ==============================
# 형광등
# ==============================

lights = []


def create_light(y, width):

    light = canvas.create_rectangle(
        WIDTH // 2 - width // 2,
        y,
        WIDTH // 2 + width // 2,
        y + 6,
        fill="#c9d0cf",
        outline=""
    )

    lights.append(light)


create_light(70, 180)
create_light(175, 120)
create_light(250, 75)


# ==============================
# 제목
# ==============================

title = canvas.create_text(
    WIDTH // 2,
    330,
    text="휘명고등학교",
    fill="#e0e5e5",
    font=("Malgun Gothic", 54),
)


# ==============================
# 버튼
# ==============================

def button_hover(event):

    event.widget.configure(
        bg="#20282a",
        fg="#ffffff"
    )


def button_leave(event):

    event.widget.configure(
        bg="#080b0c",
        fg="#cfd5d5"
    )


def new_game():

    name_screen()


def continue_game():

    message = tk.Label(
        root,
        text="저장된 게임이 없습니다.",
        bg="#050708",
        fg="#d5dddd",
        font=("Malgun Gothic", 16)
    )

    message.place(
        relx=0.5,
        rely=0.85,
        anchor="center"
    )

    root.after(
        2000,
        message.destroy
    )


# 새 게임 버튼
new_button = tk.Button(
    root,
    text="새 게임 시작",
    command=new_game,

    bg="#080b0c",
    fg="#cfd5d5",

    activebackground="#20282a",
    activeforeground="#ffffff",

    relief="flat",
    bd=0,

    width=18,
    height=2,

    font=("Malgun Gothic", 15)
)

new_button.place(
    relx=0.5,
    rely=0.65,
    anchor="center"
)


# 이어하기 버튼
continue_button = tk.Button(
    root,
    text="이어서 하기",
    command=continue_game,

    bg="#080b0c",
    fg="#cfd5d5",

    activebackground="#20282a",
    activeforeground="#ffffff",

    relief="flat",
    bd=0,

    width=18,
    height=2,

    font=("Malgun Gothic", 15)
)

continue_button.place(
    relx=0.5,
    rely=0.74,
    anchor="center"
)


new_button.bind(
    "<Enter>",
    button_hover
)

new_button.bind(
    "<Leave>",
    button_leave
)

continue_button.bind(
    "<Enter>",
    button_hover
)

continue_button.bind(
    "<Leave>",
    button_leave
)


# ==============================
# 이름 입력 화면
# ==============================

def name_screen():

    # 기존 화면 숨기기
    new_button.place_forget()
    continue_button.place_forget()

    canvas.itemconfig(
        title,
        state="hidden"
    )

    # 화면 어둡게
    overlay = tk.Frame(
        root,
        bg="#050708"
    )

    overlay.place(
        x=0,
        y=0,
        width=WIDTH,
        height=HEIGHT
    )


    label = tk.Label(
        overlay,
        text="당신의 이름을 입력하세요",
        bg="#050708",
        fg="#dfe5e5",
        font=("Malgun Gothic", 24)
    )

    label.place(
        relx=0.5,
        rely=0.40,
        anchor="center"
    )


    entry = tk.Entry(
        overlay,
        bg="#111719",
        fg="#ffffff",
        insertbackground="#ffffff",

        relief="flat",
        justify="center",

        font=("Malgun Gothic", 18),

        width=20
    )

    entry.place(
        relx=0.5,
        rely=0.50,
        anchor="center"
    )

    entry.focus()


    def start_game():

        player_name = entry.get().strip()

        if player_name == "":
            player_name = "학생"

        overlay.destroy()

        start_game_screen(player_name)


    start_button = tk.Button(
        overlay,
        text="시작",
        command=start_game,

        bg="#111719",
        fg="#dfe5e5",

        activebackground="#263033",
        activeforeground="#ffffff",

        relief="flat",
        bd=0,

        width=12,
        height=2,

        font=("Malgun Gothic", 14)
    )

    start_button.place(
        relx=0.5,
        rely=0.60,
        anchor="center"
    )


# ==============================
# 게임 시작 화면
# ==============================

def start_game_screen(player_name):

    for widget in root.winfo_children():

        if isinstance(widget, tk.Button):
            widget.place_forget()

    canvas.delete("all")

    canvas.create_rectangle(
        0, 0,
        WIDTH, HEIGHT,
        fill="#050708",
        outline=""
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 - 60,
        text=f"{player_name}의 이야기",
        fill="#dfe5e5",
        font=("Malgun Gothic", 32)
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 10,
        text="휘명고등학교",
        fill="#899494",
        font=("Malgun Gothic", 18)
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 80,
        text="게임이 시작됩니다...",
        fill="#606b6b",
        font=("Malgun Gothic", 14)
    )


# ==============================
# 형광등 깜빡임
# ==============================

def flicker():

    for light in lights:

        if math.floor(root.tk.call("after", "info") if False else 0):

            pass

    # 아주 가끔 밝기가 변하는 효과
    import random

    for light in lights:

        value = random.choice([
            "#c9d0cf",
            "#c9d0cf",
            "#aeb6b5",
            "#727b7b"
        ])

        canvas.itemconfig(
            light,
            fill=value
        )

    root.after(
        random.randint(300, 1500),
        flicker
    )


flicker()


# ==============================
# 실행
# ==============================

root.mainloop()
