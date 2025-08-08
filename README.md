# 🦧 Donkey Kong — Terminal Edition

🎮 A retro arcade tribute to Donkey Kong,  
built entirely in the terminal with Python's `curses` module.
Celebrating the launch of Donkey Kong Bananza!

<br><br>

## 🧰 Tech Stack

- Python 3.11  
- `curses` (built-in Python terminal UI library)  
- Works best in macOS Terminal / Linux console

<br><br>

## 🧠 Concept & Motivatio

I wanted to see how much fun you can pack into **pure text mode** —  
no graphics, no game engine, just code and a terminal.

- Experimenting with core mechanics like gravity, jumping, and collision 
- Practicing real-time input handling and character movement in Python

<br><br>

## ✨ Features

- 🦧 **Player movement** — Left/Right arrow keys to move, Up arrow to jump  
- 🪵 **Rolling barrels** — Reverse direction when hitting screen edges  
- 💀 **Collision detection** — Lose a life when hit by a barrel  
- ❤️ **Lives system** — Start with 3 lives, game over when you hit 0  
- ⌨️ **ESC to exit**  
- 🧱 **Static platform** — Player and barrels are placed above a fixed ground line  

<br><br>

## 🎮 Controls

| Key   | Action       |
| ----- | ------------ |
| ←     | Move left    |
| →     | Move right   |
| ↑     | Jump         |
| ESC   | Quit game    |

<br><br>

## ⚙️ Tweakable Settings & Customization

Most of the game's "feel" is controlled by a few constants at the top of the code.  
Tweak them to change difficulty, pacing, and level layout.

| Variable | Description | Default | Example tweak |
|----------|-------------|---------|---------------|
| `JUMP_HEIGHT` | Max jump height in rows | 4 | `6` → Higher jumps |
| `JUMP_DELAY`  | Frame delay (lower is faster) | 0.05 | `0.02` → Faster game loop |
| `barrels[].dir` | Barrel movement speed | ±1 | ±2 → Barrels move 2 tiles per tick |

> **Example:** Want higher jumps? change value of `JUMP_HEIGHT`.  
> **Example:** Want faster barrels? Change value of `dir`.

<br><br>

## 🐛 Debugging & Caveats

- **Terminal size is fixed**  
  The game uses fixed `GAME_HEIGHT` and `GAME_WIDTH`.  
  If you shrink the terminal window during play, `curses.error` will be thrown and the game will freeze.  
  → Solution: Set your terminal to a safe size before starting.

- **Coordinate range errors**  
  Moving the player or barrels outside the visible range will cause `curses.error`.  
  The code already `try/except`s most of these, but resizing the terminal can still cause issues.

- **Platform position (`platform_y`)**  
  Setting this too small moves the ground too far up and can spawn the player off-screen.

- **Frame rate / CPU load**  
  The main loop uses `time.sleep()` to pace the game. Lowering this too much will make it too fast and eat CPU cycles.

<br><br>

## ▶️ How to Run

```bash
git clone https://github.com/your-username/donkeykong-cli.git
cd donkeykong-cli
python donkeykong.py
```

>Best experienced in macOS/Linux terminal.
>For emoji rendering, make sure your terminal is using UTF-8.

<br><br><br><br>

# 🦧 동키콩 터미널 에디션

🎮 복고풍 아케이드 감성을 담은 동키콩 스타일 게임,
터미널과 Python curses 만으로 구현한 미니 프로젝트입니다.

<br><br>

## 🧰 사용 기술

- Python 3.11  
- curses 모듈 (Python 내장 터미널 UI)
- macOS 터미널 / Linux 콘솔 환경 권장

<br><br>

## 🧠 기획 의도

그래픽 없이 순수 **텍스트 기반**으로 얼마나 재미있는 게임을 만들 수 있을까?
복잡한 게임 엔진 없이도 "게임다운 게임"을 만들 수 있다는 걸 시험해보고 싶었습니다.

- 중력, 점프, 충돌 처리 같은 핵심 메커니즘
- 고전 게임에 대한 오마주
- 실시간 입력과 캐릭터 이동, 충돌 처리

<br><br>

## ✨ 구현된 주요 기능 
- 🦧 플레이어 이동: 좌/우 방향키로 이동, ↑ 키로 점프<br>
- 🪵 굴러가는 장애물: 양 끝에서 방향을 바꾸며 이동<br>
- 💀 충돌 판정: 장애물에 닿으면 목숨 감소<br>
- ❤️ 목숨 시스템: 시작 시 3개, 0이 되면 게임 오버<br>
- ⌨️ ESC로 게임 종료<br>
- 🧱 플랫폼: 바닥(y 좌표 고정)에 캐릭터와 장애물 배치<br>

<br><br>

## 🎮 조작법
| 키   | 동작     |
| --- | ------ |
| ←   | 왼쪽 이동  |
| →   | 오른쪽 이동 |
| ↑   | 점프     |
| ESC | 게임 종료  |

<br><br>

## ⚙️ 변수 조정 & 커스터마이징

이 게임은 여러 상수값을 수정해 플레이 스타일을 바꿀 수 있습니다.

| 변수 | 설명 | 기본값 | 변경 예시 |
|------|------|--------|-----------|
| `JUMP_HEIGHT` | 점프 시 올라가는 최대 높이 | 4 | `6` → 더 높은 점프 |
| `JUMP_DELAY` | 프레임 지연(작을수록 빠름) | 0.05 | `0.02` → 점프/이동이 빠름 |
| `barrels[].dir` | 장애물 이동 속도 | ±1 | ±2로 변경 → 두 칸씩 이동 |

> **예시**: 점프 높이를 높이고 싶다면 `JUMP_HEIGHT` 값을 변경하세요.  
> **예시**: 통나무를 더 빠르게 만들려면 `barrel['dir']` 값을 변경하세요.

<br><br>

## 🐛 디버깅 & 주의사항

- **터미널 크기 고정**  
  게임 화면 크기는 고정값(`GAME_HEIGHT`, `GAME_WIDTH`)으로 설정되어 있습니다.  
  실행 중 터미널 높이를 줄이면 `curses.error`가 발생해 게임이 멈출 수 있습니다.  
  게임 시작 전에 터미널 크기를 충분히 확보하세요.

- **좌표 범위 오류**  
  플레이어나 장애물이 화면 밖 좌표로 이동하면 `curses.error`가 발생합니다.  
  코드에서 이미 `try/except`로 대부분 무시하지만, 화면 크기 조정 시 주의하세요.

- **플랫폼 위치 조정 시 주의**  
  `platform_y` 값이 너무 작으면(화면 위쪽) 플레이어가 화면 밖에서 시작할 수 있습니다.

- **게임 루프 실행속도 조절**
  CPU 과부화를 예방을 위해, `time.sleep()` 을 활용하여 프레임 속도를 조절하세요. 

<br><br>

## ▶️ 실행 방법

```bash
git clone https://github.com/your-username/donkeykong-cli.git
cd donkeykong-cli
python donkeykong.py
```

>macOS/Linux 터미널 환경에서 가장 잘 작동합니다.
>이모지를 사용하므로 UTF-8 환경을 권장합니다.

<br><br>

📜 MIT License
