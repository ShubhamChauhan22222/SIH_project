import streamlit as st
import tempfile
from PIL import Image
#from object_detection_image_video_streamlit import *
import numpy as np
import cv2
def main():
    st.title("Identification of Medicinal Plants")
    st.sidebar.title("Settings")
    st.sidebar.subheader("Parameters")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
            width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
            width: 300px;
            margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    app_mode = st.sidebar.selectbox('Choose the App Mode', ['About App', 'Run on Image', 'Run on Video'])

    if app_mode == "About App":
        st.markdown('Welcome to our  Herb&Seek application, the ultimate solution to your exploration needs of the botanical world! Our application provides you with an effortless identification of various medicinal plants. Take a snap or a video of the plant you are curious about and our application will recognise it within seconds. Customise your search with the varied options available.')
        st.image('herbal-medicinal-Plants.jpg')
        st.header('How to use')
        st.graphviz_chart("""
            digraph{
            
            Choose_the_app_mode -> Run_on_Image
            Choose_the_app_mode -> Run_on_Video
            Run_on_Image -> Confidence
            Confidence -> Upload_Image
            Upload_Image -> Result
            
            Run_on_Video -> Use_WebCam
            Run_on_Video -> Upload_Video
            Use_WebCam -> Result
            Upload_Video -> Result
            }                  
             """)
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
                width: 300px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
                width: 300px;
                margin-left: -300px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )


    if app_mode == "Run on Image":
        st.sidebar.markdown('---')
        confidence = st.sidebar.slider('Confidence', min_value=0.0, max_value=1.0)
        st.sidebar.markdown('---')
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
                width: 300px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
                width: 300px;
                margin-left: -300px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        img_file_buffer = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

        DEMO_IMAGE = 'photo-1618130070080-91f4d55a2383.jpeg'

        if img_file_buffer is not None:
            img = cv2.imdecode(np.fromstring(img_file_buffer.read(), np.uint8),1)
            image = np.array(Image.open(img_file_buffer))

        else:
            img = cv2.imread(DEMO_IMAGE)
            image = np.array(Image.open(DEMO_IMAGE))

        st.sidebar.text('Original Image')
        st.sidebar.image(image)
        #load_yolonas_process_each_image(img, confidence, st)


    if app_mode == "Run on Video":
        st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
                width: 300px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
                width: 300px;
                margin-left: -300px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.sidebar.markdown('---')
        use_webcam = st.sidebar.checkbox('Use Webcam')
        st.sidebar.markdown('---')
        video_file_buffer = st.sidebar.file_uploader("Upload a Video", type = ["mp4", "avi", "nov", "asf"])

        DEMO_VIDEO = 'Untitled design.mp4'  # demo video paste address here
        tffile = tempfile.NamedTemporaryFile(suffix= '.mp4', delete=False) # video for detection here

        if not video_file_buffer:
            if use_webcam:
                tffile.name = 0
            else:
                vid = cv2.VideoCapture(DEMO_VIDEO)
                tffile.name = DEMO_VIDEO
                demo_vid = open(tffile.name, 'rb')
                demo_bytes = demo_vid.read()
                st.sidebar.text('Input Video')
                st.sidebar.video(demo_bytes)

        else:
            tffile.write(video_file_buffer.read())
            demo_vid = open(tffile.name, 'rb')
            demo_bytes = demo_vid.read()
            st.sidebar.text('Input Video')
            st.sidebar.video(demo_bytes)

        stframe = st.empty()
        st.markdown("<hr/>", unsafe_allow_html=True)
        kpi1, kpi2, kpi3 = st.columns(3)
        with kpi1:
            st.markdown("**Frame Rate**")
            kpi1_text = st.markdown("0")
        with kpi2:
            st.markdown("**Width**")
            kpi2_text = st.markdown("0")
        with kpi3:
            st.markdown("**Height**")
            kpi3_text = st.markdown("0")
        st.markdown("<hr/>", unsafe_allow_html=True)
        # load_yolo_nas_process_each_frame(tffile.name, kpi1_text, kpi2_text, kpi3_text, stframe)



if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass