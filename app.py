import streamlit as st
from PIL import Image, ImageDraw

st.title("KPSC Photo Maker")

# 1. പേരും തീയതിയും ചോദിക്കുന്നു
name = st.text_input("ഫോട്ടോയിൽ നൽകേണ്ട പേര്:")
date = st.text_input("തീയതി (ഉദാ: 03/02/2026):")

# 2. ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യുന്നു
uploaded_file = st.file_uploader("നിങ്ങളുടെ ഫോട്ടോ തിരഞ്ഞെടുക്കുക", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # ഫോട്ടോ തുറക്കുന്നു
    img = Image.open(uploaded_file)
    
    # KPSC സൈസിലേക്ക് മാറ്റുന്നു (150x200)
    img = img.resize((150, 200))
    
    # ഫോട്ടോയിൽ എഴുതാൻ തുടങ്ങുന്നു
    draw = ImageDraw.Draw(img)
    # ശ്രദ്ധിക്കുക: ഫോണ്ട് ഫയൽ ഇല്ലെങ്കിൽ ഡിഫോൾട്ട് ഫോണ്ട് ഉപയോഗിക്കും
    draw.text((10, 160), name, fill="black")
    draw.text((10, 180), date, fill="black")

    # 3. ഫോട്ടോ സ്ക്രീനിൽ കാണിക്കുന്നു (ഇതാണ് നിങ്ങൾ ചോദിച്ച ഭാഗം)
    st.image(img, caption='തയ്യാറാക്കിയ ഫോട്ടോ', use_container_width=False)

    # 4. ഡൗൺലോഡ് ചെയ്യാനുള്ള ബട്ടൺ
    img.save("final_photo.jpg")
    with open("final_photo.jpg", "rb") as file:
        st.download_button(
            label="ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യുക",
            data=file,
            file_name="kpsc_photo.jpg",
            mime="image/jpg"
        )
