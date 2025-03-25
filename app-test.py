import streamlit as st

# Set page config
st.set_page_config(page_title="Bhaskar Reddy - Portfolio", layout="wide")

# Custom CSS for background animation
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="st"] {
        font-family: 'Poppins', sans-serif;
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
    .centered-text {
        font-size: 60px;
        font-weight: bold;
        color: white;
        margin-top: 20vh;
        text-align: center;
    }
    .scroll-button {
        display: block;
        margin: 20px auto;
        background-color: #4F8BF9;
        color: white;
        padding: 15px 30px;
        font-size: 20px;
        border-radius: 30px;
        border: none;
        cursor: pointer;
    }
    </style>
    <canvas id="background-canvas"></canvas>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
    particlesJS('background-canvas', {
        particles: {
            number: {
                value: 80,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: "#ffffff"
            },
            shape: {
                type: "circle",
                stroke: {
                    width: 0,
                    color: "#000000"
                }
            },
            opacity: {
                value: 0.5,
                random: false,
                anim: {
                    enable: false,
                    speed: 1,
                    opacity_min: 0.1,
                    sync: false
                }
            },
            size: {
                value: 3,
                random: true
            },
            move: {
                enable: true,
                speed: 3,
                direction: "none",
                random: false,
                straight: false,
                out_mode: "out",
                bounce: false
            }
        }
    });
    </script>
    """,
    unsafe_allow_html=True
)

# First Section - Name and Button
st.markdown('<div class="centered-text">Bhaskar Reddy</div>', unsafe_allow_html=True)

if st.button('Explore My Projects 👉', key='scroll_button'):
    st.session_state.page = 'projects'

# Second Section - Projects
if 'page' in st.session_state and st.session_state.page == 'projects':
    st.title('My Projects')

    projects = [
        {"name": "Drug Recommendation System", "image": "https://i.imgur.com/QX7q6oN.jpeg"},
        {"name": "Crypto Forecasting", "image": "https://i.imgur.com/FVtCGXl.jpeg"},
        {"name": "News Sentiment Analysis", "image": "https://i.imgur.com/HhA9x1N.jpeg"}
    ]

    cols = st.columns(3)
    
    for i, project in enumerate(projects):
        with cols[i]:
            st.image(project['image'], use_column_width=True)
            st.subheader(project['name'])
            st.write("Explore the details of this project.")
            st.button(f"View {project['name']}", key=f"btn_{i}")
