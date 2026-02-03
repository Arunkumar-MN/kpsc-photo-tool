import streamlit as st
from PIL import Image, ImageDraw, ImageOps

st.title("KPSC ഫോട്ടോ മേക്കർ (Text Box Border)")

name = st.text_input("ഫോട്ടോയിൽ നൽകേണ്ട പേര്:")
date = st.text_input("ഫോട്ടോ എടുത്ത തീയതി (DD/MM/YYYY):")

uploaded_file = st.file_uploader("നിങ്ങളുടെ ഫോട്ടോ അപ്‌ലോഡ് ചെയ്യുക", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 1. ഫോട്ടോ തുറക്കുന്നു
    img = Image.open(uploaded_file)
    
    # 2. ഫോട്ടോ 150x200 സൈസിലേക്ക് മാറ്റുന്നു
    img = img.resize((150, 200))
    
    # 3. താഴെ വെള്ള ബോക്സ് ചേർക്കുന്നു
    img_with_white_box = ImageOps.expand(img, border=(0, 0, 0, 50), fill='white')
    
    # 4. വെള്ള ബോക്സിന് ചുറ്റും മാത്രം ഒരു കറുത്ത ബോർഡർ വരയ്ക്കുന്നു
    draw = ImageDraw.Draw(img_with_white_box)
    
    # ബോക്സിന്റെ നാല് വശങ്ങളും വരയ്ക്കുന്നു (xmin, ymin, xmax, ymax)
    # ഇത് വെള്ള ബോക്സിനെ മാത്രം കവർ ചെയ്യും
    draw.rectangle([0, 200, 149, 249], outline="black", width=1)
    
    # 5. പേരും തീയതിയും എഴുതുന്നു
    draw.text((10, 205), f"NAME: {name}", fill="black")
    draw.text((10, 225), f"DATE: {date}", fill="black")

    # 6. ഫോട്ടോ സ്ക്രീനിൽ കാണിക്കുന്നു
    st.image(img_with_white_box, caption='തയ്യാറാക്കിയ ഫോട്ടോ', use_container_width=False)

    # 7. ഡൗൺലോഡ് ബട്ടൺ
    img_with_white_box.save("kpsc_final.jpg")
    with open("kpsc_final.jpg", "rb") as file:
        st.download_button(
            label="ഫോട്ടോ ഡൗൺലോഡ് ചെയ്യുക",
            data=file,
            file_name="kpsc_photo.jpg",
            mime="image/jpg"
        )
