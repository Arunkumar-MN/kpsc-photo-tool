import streamlit as st
from PIL import Image, ImageDraw, ImageOps

st.title("KPSC ഫോട്ടോ മേക്കർ")

name = st.text_input("ഫോട്ടോയിൽ നൽകേണ്ട പേര് (Capital Letters):")
date = st.text_input("ഫോട്ടോ എടുത്ത തീയതി (DD/MM/YYYY):")

uploaded_file = st.file_uploader("നിങ്ങളുടെ ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യുക", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 1. ഫോട്ടോ തുറക്കുന്നു
    img = Image.open(uploaded_file)
    
    # 2. ഫോട്ടോ 150x200 സൈസിലേക്ക് മാറ്റുന്നു
    img = img.resize((150, 200))
    
    # 3. ഫോട്ടോയുടെ താഴെ വെള്ള ബോക്സ് ചേർക്കുന്നു (Border/Padding)
    # താഴെ മാത്രം 40 പിക്സൽ വെള്ള നിറം ചേർക്കുന്നു
    img_with_border = ImageOps.expand(img, border=(0, 0, 0, 50), fill='white')
    
    # 4. വെള്ള ബോക്സിൽ എഴുതാൻ തുടങ്ങുന്നു
    draw = ImageDraw.Draw(img_with_border)
    
    # പേരും തീയതിയും വെള്ള ബോക്സിൽ കൃത്യമായി വരാൻ (Positioning)
    draw.text((10, 205), f"NAME: {name}", fill="black")
    draw.text((10, 225), f"DATE: {date}", fill="black")

    # 5. ഫോട്ടോ സ്ക്രീനിൽ കാണിക്കുന്നു
    st.image(img_with_border, caption='PSC നിബന്ധന പ്രകാരമുള്ള ഫോട്ടോ', use_container_width=False)

    # 6. സേവ് ചെയ്യാനും ഡൗൺലോഡ് ചെയ്യാനും
    img_with_border.save("kpsc_ready.jpg")
    with open("kpsc_ready.jpg", "rb") as file:
        st.download_button(
            label="ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യുക",
            data=file,
            file_name="kpsc_photo.jpg",
            mime="image/jpg"
        )
