import streamlit as st
from PIL import Image, ImageDraw, ImageOps

st.title("KPSC ഫോട്ടോ മേക്കർ (Merged Border)")

name = st.text_input("ഫോട്ടോയിൽ നൽകേണ്ട പേര്:")
date = st.text_input("ഫോട്ടോ എടുത്ത തീയതി (DD/MM/YYYY):")

uploaded_file = st.file_uploader("നിങ്ങളുടെ ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യുക", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 1. ഫോട്ടോ തുറക്കുന്നു
    img = Image.open(uploaded_file)
    
    # 2. ഫോട്ടോ 150x200 സൈസിലേക്ക് മാറ്റുന്നു
    img = img.resize((150, 200))
    
    # 3. താഴെ വെള്ള ബോക്സ് ചേർക്കുന്നു (ഇപ്പോൾ ബോർഡർ ഇല്ല)
    img_with_white_box = ImageOps.expand(img, border=(0, 0, 0, 50), fill='white')
    
    # 4. വെള്ള ബോക്സിൽ പേരും തീയതിയും എഴുതുന്നു
    draw = ImageDraw.Draw(img_with_white_box)
    draw.text((10, 205), f"NAME: {name}", fill="black")
    draw.text((10, 225), f"DATE: {date}", fill="black")
    
    # 5. ഫോട്ടോയ്ക്കും ബോക്സിനും കൂടി മൊത്തത്തിൽ ഒരൊറ്റ ബോർഡർ നൽകുന്നു
    # border=1 എന്നത് 1 pixel കനം നൽകും
    final_img = ImageOps.expand(img_with_white_box, border=1, fill='black')

    # 6. ഫോട്ടോ സ്ക്രീനിൽ കാണിക്കുന്നു
    st.image(final_img, caption='PSC നിബന്ധന പ്രകാരമുള്ള ഫോട്ടോ', use_container_width=False)

    # 7. ഡൗൺലോഡ് ബട്ടൺ (ഫയൽ സൈസ് നിയന്ത്രിക്കാൻ quality=95 നൽകുന്നു)
    final_img.save("kpsc_final.jpg", quality=95)
    with open("kpsc_final.jpg", "rb") as file:
        st.download_button(
            label="ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യുക",
            data=file,
            file_name="kpsc_photo.jpg",
            mime="image/jpg"
        )
