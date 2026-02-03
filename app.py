# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

# വെബ്സൈറ്റിലെ തലക്കെട്ട്
st.title("കേരള ഗവൺമെന്റ് ജോബ് ഫോട്ടോ സെറ്റർ")

# ഉപഭോക്താവിൽ നിന്ന് പേര് വാങ്ങാൻ
name = st.text_input("നിങ്ങളുടെ പേര് നൽകുക:")

# ഫയൽ അപ്‌ലോഡ് ചെയ്യാൻ
uploaded_file = st.file_uploader("നിങ്ങളുടെ ഫോട്ടോ തിരഞ്ഞെടുക്കുക", type=['jpg', 'png', 'jpeg'])

if st.button("ഫോട്ടോ തയ്യാറാക്കുക"):
    if uploaded_file is not None:
        st.write(f"നന്ദി {name}, നിങ്ങളുടെ ഫോട്ടോ പ്രോസസ്സ് ചെയ്യുന്നു...")
# %%
        # ഇവിടെയാണ് നമ്മൾ നേരത്തെ പഠിച്ച Pillow കോഡ് ചേർക്കേണ്ടത്
from PIL import Image, ImageDraw, ImageFont

def process_photo(input_image_path, name, date):
    # ഫോട്ടോ തുറക്കുക
    img = Image.open(input_image_path)
    
    # 150x200 സൈസിലേക്ക് മാറ്റുക
    img = img.resize((150, 200))
    
    # പേരും തീയതിയും ചേർക്കാൻ ഒരു Draw ഒബ്ജക്റ്റ് ഉണ്ടാക്കുക
    draw = ImageDraw.Draw(img)
    
    # പേരും തീയതിയും എഴുതുക (ഫോണ്ട് സെറ്റ് ചെയ്യണം)
    draw.text((10, 160), name, fill="black")
    draw.text((10, 180), date, fill="black")
    
    # സേവ് ചെയ്യുക
    img.save("kpsc_photo.jpg", quality=90)