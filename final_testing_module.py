import streamlit as st

from util import set_background


def main():
    st.title("Final Testing Module")

    st.sidebar.title("Modules")
    selected_module = st.sidebar.selectbox("Select Module", ["Enhance Image", "Detect Face", "Recognize Face", "View/Generate CSV", "Combined"])

    if selected_module == "Enhance Image":
        import test_enhance_image
        set_background('pix/1.png')
        test_enhance_image.main()
    elif selected_module == "Detect Face":
        import test_detect_face
        set_background('pix/2.png')
        test_detect_face.main()
    elif selected_module == "Recognize Face":
        import test_recognize_face
        set_background('pix/4.png')
        test_recognize_face.main()
    elif selected_module == "View/Generate CSV":
        import test_csv
        set_background('pix/3.png')
        test_csv.main()
    elif selected_module == "Combined":
        import test_main
        set_background('pix/5.png')
        test_main.main()

if __name__ == "__main__":
    main()
