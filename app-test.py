import streamlit as st

# Set page config
st.set_page_config(page_title="Animated Background", layout="wide")

# Custom HTML for Animation using particles.js from Exifa
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
        background: #000;
    }
    </style>
    <canvas id="background-canvas"></canvas>
    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <script>
    particlesJS.load('background-canvas', 'https://sahirmaharaj.github.io/exifa/particles.json', function() {
        console.log('Particles.js loaded with config');
    });
    </script>
    """,
    unsafe_allow_html=True
)

st.write("## Background Animation using Particles.js from Exifa")
