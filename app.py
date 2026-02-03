import streamlit as st
from PIL import Image, ImageDraw, ImageOps

st.title("KPSC ഫോട്ടോ മേക്കർ (With Border)")

name = st.text_input("ഫോട്ടോയിൽ നൽകേണ്ട പേര്:")
date = st.text_input("ഫോട്ടോ എടുത്ത തീയതി (DD/MM/YYYY):")

uploaded_file = st.file_uploader("നിങ്ങളുടെ ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യുക", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 1. ഫോട്ടോ തുറക്കുന്നു
    img = Image.open(uploaded_file)
    
    # 2. ഫോട്ടോ 150x200 സൈസിലേക്ക് മാറ്റുന്നു
    img = img.resize((150, 200))
    
    # 3. താഴെ മാത്രം വെള്ള ബോക്സ് ചേർക്കുന്നു (പേരും തീയതിയും എഴുതാൻ)
    img_with_white_box = ImageOps.expand(img, border=(0, 0, 0, 50), fill='white')
    
    # 4. വെള്ള ബോക്സിൽ പേരും തീയതിയും എഴുതുന്നു
    draw = ImageDraw.Draw(img_with_white_box)
    draw.text((10, 205), f"NAME: {name}", fill="black")
    draw.text((10, 225), f"DATE: {date}", fill="black")
    
    # 5. ഫോട്ടോയ്ക്ക് ചുറ്റും ഒരു കറുത്ത ബോർഡർ ചേർക്കുന്നു (1 pixel thickness)
    final_img = ImageOps.expand(img_with_white_box, border=1, fill='black')

    # 6. ഫോട്ടോ സ്ക്രീനിൽ കാണിക്കുന്നു
    st.image(final_img, caption='കറുത്ത ബോർഡറോട് കൂടിയ ഫോട്ടോ', use_container_width=False)

    # 7. സേവ് ചെയ്യാനും ഡൗൺലോഡ് ചെയ്യാനും
    final_img.save("kpsc_final_with_border.jpg")
    with open("kpsc_final_with_border.jpg", "rb") as file:
        st.download_button(
            label="ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യുക",
            data=file,
            file_name="kpsc_photo_bordered.jpg",
            mime="image/jpg"
        )
