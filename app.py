
from pathlib import Path
import base64
import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="A Special Birthday Surprise",
    page_icon="🦚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"

VIDEO_PATH = ASSET_DIR / "krishna.mp4"
AUDIO_PATH = ASSET_DIR / "bansuri.mp3"


# =====================================================
# LOAD MEDIA FILES
# =====================================================

def load_media(path):
    if not path.exists():
        st.error(
            f"Missing file: {path.name}. "
            f"Please place it inside: {ASSET_DIR}"
        )
        st.stop()

    return base64.b64encode(path.read_bytes()).decode("ascii")


video_b64 = load_media(VIDEO_PATH)
audio_b64 = load_media(AUDIO_PATH)


# =====================================================
# STREAMLIT OUTER PAGE STYLING
# =====================================================

st.markdown("""
<style>
    #MainMenu,
    footer,
    header {
        visibility: hidden;
    }

    [data-testid="stAppViewContainer"] {
        background: #100b24;
    }

    [data-testid="stMain"] {
        padding: 0 !important;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding: 0 !important;
    }

    iframe {
        width: 100% !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)


# =====================================================
# HTML TEMPLATE
# =====================================================

html = r"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    width: 100%;
    min-height: 100%;
    scroll-behavior: smooth;
}

body {
    width: 100%;
    min-height: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    font-family: Georgia, serif;
    color: white;
    background: #100b24;
}

/* =================================================
   MAIN FULL-WIDTH BACKGROUND
================================================= */

#app {
    width: 100%;
    min-height: 100vh;
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(
            ellipse at 50% 25%,
            #59376f 0%,
            #2b1948 48%,
            #0b081a 100%
        );
}

.stars {
    position: absolute;
    inset: 0;
    pointer-events: none;
    opacity: .7;

    background-image:
        radial-gradient(2px 2px at 10% 20%, white, transparent),
        radial-gradient(2px 2px at 70% 15%, #ffe8a8, transparent),
        radial-gradient(2px 2px at 85% 55%, white, transparent),
        radial-gradient(1px 1px at 30% 75%, white, transparent),
        radial-gradient(2px 2px at 50% 40%, #ffe8a8, transparent);

    background-size: 250px 220px;

    animation: twinkle 3s ease-in-out infinite alternate;
}

@keyframes twinkle {
    from { opacity: .7; }
    to { opacity: .25; }
}

/* =================================================
   SCENES
================================================= */

.scene {
    position: relative;
    z-index: 2;

    width: 100%;
    min-height: 100vh;

    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    text-align: center;

    padding: 65px 20px;

    transition: opacity .9s ease;
}

#birthday {
    display: none;
    opacity: 0;

    background:
        radial-gradient(
            ellipse at 50% 35%,
            #77415e 0%,
            #321a48 55%,
            #0b081a 100%
        );
}

/* =================================================
   TYPOGRAPHY
================================================= */

h1 {
    font-size: clamp(2.1rem, 6vw, 4.8rem);
    line-height: 1.2;
    margin: 20px 0;

    color: #ffe5a6;

    text-shadow:
        0 0 12px #ffbf5e,
        0 0 28px #ff5e9c;
}

.subtitle {
    font-family: Arial, sans-serif;
    font-size: clamp(12px, 2vw, 17px);
    letter-spacing: 3px;
    color: #f9d9f0;
    margin-bottom: 8px;
}

.message {
    width: min(750px, 94%);
    font-family: Arial, sans-serif;
    font-size: clamp(15px, 2vw, 18px);
    line-height: 1.8;
    color: #fff0f4;
    margin: 10px auto 20px;
}

/* =================================================
   KRISHNA VIDEO
================================================= */

.krishna-video {
    width: min(850px, 92vw);
    height: min(58vh, 520px);

    min-height: 260px;

    object-fit: contain;

    background: #100b24;

    border-radius: 22px;

    border: 2px solid rgba(255, 226, 160, .75);

    box-shadow:
        0 0 35px rgba(255, 196, 104, .4),
        0 0 90px rgba(193, 114, 255, .25);
}

/* =================================================
   BUTTONS
================================================= */

button {
    font-family: Arial, sans-serif;
    cursor: pointer;
    transition: .25s ease;
}

button:hover {
    transform: translateY(-3px);
}

.open-btn,
.replay-btn {
    margin-top: 25px;
    padding: 15px 32px;

    border: none;
    border-radius: 40px;

    background: linear-gradient(
        110deg,
        #ffcf75,
        #ff8caa
    );

    color: #35152f;
    font-weight: bold;
    font-size: 16px;

    box-shadow: 0 7px 25px #ff9b9b55;
}

.note {
    font: 13px Arial, sans-serif;
    color: #d8c5e9;
    margin-top: 14px;
}

/* =================================================
   CAKE - MEDIUM SIZE
================================================= */

.cake-area {
    width: 270px;
    height: 230px;
    position: relative;
    margin: 18px auto 5px;
}

.cake-plate {
    position: absolute;
    bottom: 12px;
    left: 10px;

    width: 250px;
    height: 18px;

    border-radius: 50%;

    background: linear-gradient(
        #fff1d5,
        #d9a7bd
    );

    box-shadow: 0 8px 18px #0005;
}

.cake-body {
    position: absolute;
    bottom: 27px;
    left: 40px;

    width: 190px;
    height: 105px;

    border-radius: 12px 12px 17px 17px;

    background: linear-gradient(
        to bottom,
        #ffb7d0 0%,
        #f47da7 25%,
        #e45b91 100%
    );

    box-shadow:
        inset 0 -12px #cf477d,
        0 8px 20px #0004;
}

.cake-top {
    position: absolute;
    top: -16px;
    left: 0;

    width: 190px;
    height: 34px;

    border-radius: 50%;

    background: #ffe1e9;
    border-bottom: 6px solid #f58caf;
}

.cake-decoration {
    position: absolute;
    top: 32px;
    left: 15px;

    width: 160px;

    color: #fff5d9;
    font-size: 19px;
    letter-spacing: 12px;
}

.candle {
    position: absolute;
    z-index: 5;

    bottom: 131px;
    left: 129px;

    width: 13px;
    height: 43px;

    border-radius: 4px;

    background: repeating-linear-gradient(
        45deg,
        white 0 6px,
        #a77ce8 6px 12px
    );
}

.flame {
    position: absolute;
    z-index: 6;

    bottom: 174px;
    left: 128px;

    width: 16px;
    height: 25px;

    border-radius: 50% 50% 45% 45%;

    background: radial-gradient(
        ellipse at 50% 70%,
        #fff8a8 0 20%,
        #ff9e37 50%,
        #ff4e45 80%
    );

    filter: drop-shadow(0 0 10px #ffb52e);

    transform-origin: bottom center;

    animation: flicker .35s infinite alternate;
}

@keyframes flicker {
    from { transform: scale(1) rotate(-4deg); }
    to { transform: scale(.83) rotate(5deg); }
}

/* =================================================
   CANDLE BLOW EFFECT
================================================= */

.flame.blown {
    animation: extinguish .5s forwards;
}

@keyframes extinguish {
    0% {
        opacity: 1;
        transform: scale(1);
    }

    100% {
        opacity: 0;
        transform: translateY(-20px) scale(.1);
    }
}

.smoke {
    position: absolute;
    z-index: 7;

    bottom: 175px;
    left: 132px;

    width: 12px;
    height: 12px;

    border-radius: 50%;

    background: #d7d7d7aa;

    animation: smoke 1.5s ease-out forwards;
}

@keyframes smoke {
    to {
        opacity: 0;
        transform: translateY(-45px) scale(3);
    }
}

/* =================================================
   BUTTON GROUP
================================================= */

.actions {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
    margin-top: 15px;
}

.action-btn {
    padding: 13px 21px;

    border: 1px solid #ffd7a5;
    border-radius: 30px;

    background: #ffffff18;
    color: white;

    font-size: 15px;
}

.action-btn:hover {
    background: #ffffff40;
}

#status {
    min-height: 28px;
    margin-top: 12px;
    font: 14px Arial, sans-serif;
    color: #ffe3ad;
}

/* =================================================
   CONFETTI / PARTY POPPERS
================================================= */

#confetti {
    position: absolute;
    inset: 0;
    z-index: 10;

    overflow: hidden;
    pointer-events: none;
}

.confetti-piece {
    position: absolute;
    top: -15px;

    width: 9px;
    height: 15px;

    border-radius: 2px;

    animation: confettiFall linear forwards;
}

@keyframes confettiFall {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 1;
    }

    100% {
        transform: translateY(110vh) rotate(800deg);
        opacity: .8;
    }
}

/* Side cannon bursts */

.burst-piece {
    position: absolute;
    z-index: 11;

    width: 10px;
    height: 13px;

    border-radius: 2px;

    animation: burst .95s ease-out forwards;
}

@keyframes burst {
    0% {
        opacity: 1;
        transform: translate(0, 0) rotate(0deg) scale(1);
    }

    100% {
        opacity: 0;
        transform:
            translate(var(--dx), var(--dy))
            rotate(700deg)
            scale(.3);
    }
}

/* =================================================
   BALLOONS - FIXED ABOVE ALL SCENES
================================================= */

.balloon {
    position: fixed;
    z-index: 20;
    bottom: -90px;
    width: 48px;
    height: 64px;
    border-radius: 50% 50% 45% 45%;
    box-shadow: inset -7px -5px 10px #0002, 0 0 12px #ffffff30;
    opacity: 0;
    pointer-events: none;
    animation: floatup 14s ease-in forwards;
}

.balloon:before {
    content: "";
    position: absolute;
    top: 12px;
    left: 10px;
    width: 10px;
    height: 20px;
    border-radius: 50%;
    background: #ffffff55;
}

.balloon:after {
    content: "";
    position: absolute;
    bottom: -55px;
    left: 23px;
    width: 1px;
    height: 58px;
    background: #ffffffaa;
}

@keyframes floatup {
    0% {
        transform: translateY(0) translateX(0) rotate(-5deg);
        opacity: 0;
    }
    10% { opacity: 1; }
    50% {
        transform: translateY(-55vh) translateX(25px) rotate(8deg);
    }
    100% {
        transform: translateY(-120vh) translateX(-20px) rotate(-8deg);
        opacity: 0;
    }
}

/* =================================================
   FOOTER
================================================= */

.footer {
    margin-top: 20px;
    font: 13px Arial, sans-serif;
    color: #e1cce9;
    padding-bottom: 15px;
}

/* =================================================
   MOBILE RESPONSIVE
================================================= */

@media(max-width: 600px) {

    .scene {
        padding: 45px 13px;
    }

    .krishna-video {
        width: 96vw;
        height: 42vh;
        min-height: 220px;
    }

    .cake-area {
        transform: scale(.9);
        margin-top: 8px;
        margin-bottom: 0;
    }

    .actions {
        gap: 9px;
    }

    .action-btn {
        padding: 12px 15px;
        font-size: 13px;
    }

    .message {
        line-height: 1.65;
    }
}

</style>
</head>

<body>

<div id="app">

    <div class="stars"></div>

    <div id="confetti"></div>

    <!-- KRISHNA OPENING -->

    <section id="krishna" class="scene">

        <div class="subtitle">
            A LITTLE DIVINE BEGINNING
        </div>

        <h1>
            May your day begin with blessings ✨
        </h1>

        <video
            id="krishnaVideo"
            class="krishna-video"
            muted
            playsinline
            preload="auto"
        >
            <source
                src="data:video/mp4;base64,__VIDEO_B64__"
                type="video/mp4"
            >
        </video>

        <button
            class="open-btn"
            onclick="startSurprise()"
        >
            Open Your Surprise 🦚
        </button>

        <div class="note">
            Tap to begin • Peaceful flute music awaits
        </div>

    </section>


    <!-- BIRTHDAY REVEAL -->

    <section id="birthday" class="scene">

        <div class="subtitle">
            TODAY IS ALL ABOUT YOU
        </div>

        <h1>
            Happy Birthday,<br>
            My Bestfriend! 🎂
        </h1>

        <p class="message">
            May your life always be filled with happiness,
            courage, laughter, beautiful memories and countless
            reasons to smile. Thank you for being such a special
            part of my life. Keep shining, always. 💗
        </p>


        <!-- MEDIUM CAKE -->

        <div class="cake-area" id="cakeArea">

            <div class="flame" id="flame"></div>

            <div class="candle"></div>

            <div class="cake-body">

                <div class="cake-top"></div>

                <div class="cake-decoration">
                    ♥ ♥ ♥
                </div>

            </div>

            <div class="cake-plate"></div>

        </div>


        <!-- CAKE AND CELEBRATION CONTROLS -->

        <div class="actions">

            <button
                class="action-btn"
                onclick="blowCandles()"
            >
                🌬️ Blow the candles
            </button>

            <button
                class="action-btn"
                onclick="partyPoppers()"
            >
                🎉 Party poppers
            </button>

            <button
                class="action-btn"
                onclick="toggleMusic()"
                id="musicBtn"
            >
                ⏸ Pause music
            </button>

        </div>

        <div id="status">
            Make a wish and blow out the candles! ✨
        </div>

        <div class="footer">
            Made with care, just for you 💗
        </div>

        <button
            class="replay-btn"
            onclick="replay()"
        >
            ↻ Replay the surprise
        </button>

    </section>

</div>


<!-- FLUTE MUSIC -->

<audio id="fluteMusic" loop preload="auto">

    <source
        src="data:audio/mpeg;base64,__AUDIO_B64__"
        type="audio/mpeg"
    >

</audio>


<script>

/* =================================================
   ELEMENTS
================================================= */

const video = document.getElementById("krishnaVideo");
const music = document.getElementById("fluteMusic");

const krishnaScene = document.getElementById("krishna");
const birthdayScene = document.getElementById("birthday");

const confettiBox = document.getElementById("confetti");

let started = false;
let candlesBlown = false;
let balloonTimer = null;


/* =================================================
   START SURPRISE
================================================= */

function startSurprise() {

    if (started) return;

    started = true;

    video.currentTime = 0;

    video.play().catch(() => {
        document.getElementById("status").innerText =
            "Video could not start. Check your MP4 file.";
    });

    music.volume = 0.55;

    music.play().catch(() => {
        document.getElementById("status").innerText =
            "Tap the music button to start the flute.";
    });

    // Show Krishna for 35 seconds.
    // If the video finishes earlier, reveal the birthday then.

    let revealed = false;

    function revealBirthday() {

        if (revealed) return;

        revealed = true;

        video.pause();

        krishnaScene.style.opacity = "0";

        setTimeout(() => {

            krishnaScene.style.display = "none";

            birthdayScene.style.display = "flex";

            requestAnimationFrame(() => {
                birthdayScene.style.opacity = "1";
            });

            partyPoppers();

        }, 900);

    }

    const timer = setTimeout(revealBirthday, 35000);

    video.onended = () => {
        clearTimeout(timer);
        revealBirthday();
    };

}


/* =================================================
   CONFETTI FALL
================================================= */

function celebrate() {

    const colors = [
        "#ffd166",
        "#ff70a6",
        "#8ecae6",
        "#cdb4db",
        "#b7efc5",
        "#ffffff"
    ];

    for (let i = 0; i < 120; i++) {

        const piece = document.createElement("i");

        piece.className = "confetti-piece";

        piece.style.left = Math.random() * 100 + "%";

        piece.style.background =
            colors[Math.floor(Math.random() * colors.length)];

        piece.style.animationDuration =
            (3 + Math.random() * 4) + "s";

        piece.style.animationDelay =
            Math.random() * 1.2 + "s";

        confettiBox.appendChild(piece);

        setTimeout(() => {
            piece.remove();
        }, 8500);

    }

}


/* =================================================
   WORKING SIDE PARTY POPPERS
================================================= */

function partyPoppers() {

    const colors = [
        "#ff4d9d",
        "#ffd166",
        "#8ecae6",
        "#b7efc5",
        "#cdb4db",
        "#ffffff"
    ];

    const app = document.getElementById("app");

    const width = app.clientWidth;
    const height = app.clientHeight;

    // Launch two bursts from the bottom corners.

    const origins = [
        { x: 15, y: height * 0.70 },
        { x: width - 15, y: height * 0.70 }
    ];

    origins.forEach(origin => {

        for (let i = 0; i < 55; i++) {

            const piece = document.createElement("i");

            piece.className = "burst-piece";

            piece.style.left = origin.x + "px";
            piece.style.top = origin.y + "px";

            piece.style.background =
                colors[Math.floor(Math.random() * colors.length)];

            const dx = (Math.random() - 0.5) * 300;
            const dy = -(Math.random() * 360 + 80);

            piece.style.setProperty("--dx", dx + "px");
            piece.style.setProperty("--dy", dy + "px");

            app.appendChild(piece);

            setTimeout(() => {
                piece.remove();
            }, 1100);

        }

    });

    celebrate();
    startBalloons();

}


/* =================================================
   BLOW OUT CANDLES
================================================= */

function blowCandles() {

    if (candlesBlown) {

        document.getElementById("status").innerText =
            "The candles are already blown out! 💗";

        return;
    }

    candlesBlown = true;

    const flame = document.getElementById("flame");

    flame.classList.add("blown");

    // Smoke effect

    const smoke = document.createElement("i");

    smoke.className = "smoke";

    document.getElementById("cakeArea").appendChild(smoke);

    setTimeout(() => {
        smoke.remove();
    }, 1600);

    document.getElementById("status").innerText =
        "Wish made! Happy Birthday! 🎂💗";

    // Celebration after blowing the candle

    partyPoppers();

}


/* =================================================
   BALLOONS
================================================= */

function startBalloons() {

    const colors = [
        "#ff4d9d", "#ffd166", "#8ecae6", "#cdb4db",
        "#a8e6cf", "#ff8c69", "#ffffff"
    ];

    // Remove any previous balloon wave before starting another.
    document.querySelectorAll(".balloon").forEach(
        balloon => balloon.remove()
    );

    for (let i = 0; i < 18; i++) {
        const balloon = document.createElement("div");
        balloon.className = "balloon";
        balloon.style.left = (Math.random() * 92 + 2) + "vw";
        balloon.style.background =
            colors[Math.floor(Math.random() * colors.length)];

        const duration = 12 + Math.random() * 5;
        const delay = Math.random() * 3;
        balloon.style.animationDuration = duration + "s";
        balloon.style.animationDelay = delay + "s";

        document.body.appendChild(balloon);

        setTimeout(() => balloon.remove(), (duration + delay) * 1000 + 500);
    }
}


/* =================================================
   MUSIC CONTROL
================================================= */

function toggleMusic() {

    const btn = document.getElementById("musicBtn");

    if (music.paused) {

        music.play().then(() => {

            btn.innerText = "⏸ Pause music";

        }).catch(() => {

            document.getElementById("status").innerText =
                "Unable to play the music file.";

        });

    } else {

        music.pause();

        btn.innerText = "▶ Play music";

    }

}


/* =================================================
   REPLAY EVERYTHING
================================================= */

function replay() {

    // Stop music and video

    music.pause();
    music.currentTime = 0;

    video.pause();
    video.currentTime = 0;

    // Reset candle

    candlesBlown = false;

    document.getElementById("flame").classList.remove("blown");

    // Reset music button

    document.getElementById("musicBtn").innerText =
        "⏸ Pause music";

    document.getElementById("status").innerText =
        "Make a wish and blow out the candles! ✨";

    // Remove previous animations

    document.querySelectorAll(".balloon").forEach(
        item => item.remove()
    );

    document.querySelectorAll(".burst-piece").forEach(
        item => item.remove()
    );

    document.querySelectorAll(".smoke").forEach(
        item => item.remove()
    );

    confettiBox.innerHTML = "";

    // Reset scenes

    birthdayScene.style.display = "none";
    birthdayScene.style.opacity = "0";

    krishnaScene.style.display = "flex";
    krishnaScene.style.opacity = "1";

    started = false;

}


/* =================================================
   CLEANUP
================================================= */

window.addEventListener("beforeunload", () => {

    music.pause();
    video.pause();

});

</script>

</body>
</html>
"""


# =====================================================
# INSERT MEDIA
# =====================================================

html = html.replace("__VIDEO_B64__", video_b64)
html = html.replace("__AUDIO_B64__", audio_b64)


# =====================================================
# RENDER FULL-WIDTH COMPONENT
# =====================================================

components.html(
    html,
    height=1050,
    scrolling=True
)
