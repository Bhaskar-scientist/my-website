import streamlit as st

# Set page config
st.set_page_config(page_title="Animated Background", layout="wide")

# Custom HTML for Animation using particles.js
st.markdown(
    """
    <style>
    html, body, [class*="st"] {
        margin: 0;
        overflow: hidden;
    }
    #background-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
    }
    </style>
    <canvas id="background-canvas"></canvas>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
    particlesJS('background-canvas', {
        particles: {
            number: {
                value: 100,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: "#ffffff"
            },
            shape: {
                type: "circle"
            },
            opacity: {
                value: 0.5,
                anim: {
                    enable: true,
                    speed: 0.5,
                    opacity_min: 0.1
                }
            },
            size: {
                value: 3,
                random: true
            },
            move: {
                enable: true,
                speed: 2,
                direction: "none",
                out_mode: "out"
            }
        }
    });
    </script>
    """,
    unsafe_allow_html=True
)

st.write("## Background Animation using Particles.js")
