import json
import random
import requests
import streamlit as st
import streamlit.components.v1 as components
import streamlit_lottie
import time
import utils

def load_lottieurl():
    lottie_url =  random.choice(utils.animations)
    r = requests.get(lottie_url)

    while r.status_code != 200 and count < 10:
        lottie_url =  random.choice(utils.animations)
        count += 1
    return r.json()

def scrum_order():
    st.set_page_config(
        page_title = 'Scrum Randomizer'
        , page_icon = '🔀'
    )
    # st.title('Scrum Order')

################################################################################
#                         Display Date and Time                                #
################################################################################
    # javascript clock https://codepen.io/afarrar/pen/JRaEjP
    # javascript date https://www.freecodecamp.org/news/how-to-format-dates-in-javascript/
    components.html(
        """
        <body onload="startTime()" style="color: #17D4FE; font-size: 48px; font-family: Orbitron;">
        <div id="txt"></div>

        <script>
        function startTime() {
        const today = new Date();
        let h = today.getHours();
        let m = today.getMinutes();
        let s = today.getSeconds();
        m = checkTime(m);
        s = checkTime(s);
        todayDate = new Date().toLocaleDateString('en-us', { weekday:"long", 
            year:"numeric", month:"short", day:"numeric"}) 

        document.getElementById('txt').innerHTML =  todayDate + " " + h + ":" + m + ":" + s;
        setTimeout(startTime, 1000);
        }

        function checkTime(i) {
        if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
        return i;
        }
        </script>

        </body>
        """, height = 64
        )
################################################################################
#                                Scrum Order                                   #
################################################################################
    include_lst = st.multiselect('Select scrum participants:'
        , options = utils.names
        , default = utils.names)

    random.shuffle(include_lst)

    if st.button('Set Scrum Order'):

        col1, col2 = st.columns(2)

        with col1:
            with st.spinner('Setting Scrum Order...'):
                time.sleep(5)
            st.success('Done!')

            lottie_url = load_lottieurl()
            streamlit_lottie.st_lottie(lottie_url
                , key = 'animation'
                , height = 300 # in pixels
                , width  = 300)

        with col2:
            for i, name in enumerate(include_lst, 1):
                st.write(f'{i}. {name}')

    # Hide Streamlit branding
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html = True)

scrum_order()