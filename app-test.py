import streamlit as st

# HTML and JavaScript for particles.js
particles_js = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
    }
    #particles-js {
      position: absolute;
      width: 100%;
      height: 100%;
      background-color: #1e1e1e;
      z-index: -1;
    }
    .content {
      position: relative;
      color: white;
      font-size: 48px;
      text-align: center;
      top: 40%;
    }
  </style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">Bhaskar Reddy</div>

  <script>
    particlesJS.load('particles-js', 'https://cdn.jsdelivr.net/particles.js/2.0.0/particles.json', function() {
      console.log('particles.js loaded');
    });
  </script>
</body>
</html>
'''

# Streamlit app
st.set_page_config(page_title="Particles Background", layout="wide")
st.components.v1.html(particles_js, height=800)
