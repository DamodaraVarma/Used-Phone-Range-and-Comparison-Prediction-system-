import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Used Phone Range & Comparison Prediction",
    layout="wide"
)

st.title("📱 Used Phone Range and Comparison Prediction System")

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    return pd.read_csv("used_phone_data.csv")

data = load_data()

# =========================================================
# TRAIN MODEL
# =========================================================
@st.cache_resource
def train_model(data):
    df = data.copy()
    le = LabelEncoder()
    df["Brand"] = le.fit_transform(df["Brand"])

    X = df.drop("Price", axis=1)
    y = df["Price"]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)
    return model, le

model, brand_encoder = train_model(data)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================
section = st.sidebar.radio(
    "Select Section",
    ["🏆 Flagship Phones", "🔮 Price Prediction", "📊 Phone Comparison"]
)

# =========================================================
# FLAGSHIP PHONES SECTION (SAFE VERSION)
# =========================================================
if section == "🏆 Flagship Phones":

    st.markdown("## 🏆 Flagship Smartphones")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Samsung", "Xiaomi", "Asus", "Vivo", "OnePlus"]
    )

    # ---------- SAFE IMAGE DISPLAY ----------
    def show_images(images):
        cols = st.columns(len(images))
        for col, img in zip(cols, images):
            col.image(img, use_container_width=True)

    def show_specs(title, details, price, link):
        st.subheader(title)
        for d in details:
            st.write("•", d)
        st.write(f"💰 Price: {price}")
        st.link_button("Buy from Official Store", link)

    # ---------------- SAMSUNG ----------------
    with tab1:
        show_images([
            "https://images.samsung.com/in/smartphones/galaxy-s23-ultra/buy/DM3-web-6.jpg",
            "https://images.samsung.com/in/smartphones/galaxy-s23-ultra/buy/DM3-web-1.jpg"
        ])
        show_specs(
            "Samsung Galaxy S23 Ultra",
            [
                "Processor: Snapdragon 8 Gen 2",
                "Display: 6.8-inch Dynamic AMOLED 2X",
                "Camera: 200 MP Quad Camera",
                "Battery: 5000 mAh",
                "RAM & Storage: Up to 12GB | 1TB",
                "OS: Android 13"
            ],
            "₹1,24,999",
            "https://www.samsung.com/in/"
        )

    # ---------------- XIAOMI ----------------
    with tab2:
        show_images([
            "https://assets.hardwarezone.com/img/2022/10/Xiaomi-12T-Pro_2.jpg"
        ])
        show_specs(
            "Xiaomi 12T Pro",
            [
                "Processor: Snapdragon 8+ Gen 1",
                "Display: 6.67-inch AMOLED",
                "Camera: 200 MP",
                "Battery: 5000 mAh",
                "RAM & Storage: Up to 12GB | 256GB",
                "OS: MIUI (Android)"
            ],
            "₹60,490",
            "https://www.mi.com/in/product/xiaomi-12-pro-5g/"
        )

    # ---------------- ASUS ----------------
    with tab3:
        show_images([
            "https://www.flashfly.net/wp/wp-content/uploads/2022/11/review-ASUS-ROG-Phone-6D-Ultimate-flashfly-1.jpg"
        ])
        show_specs(
            "Asus ROG Phone 6D Ultimate",
            [
                "Processor: MediaTek Dimensity 9000+",
                "Display: 6.78-inch AMOLED 165Hz",
                "Camera: 50 MP",
                "Battery: 6000 mAh",
                "RAM & Storage: 16GB | 512GB",
                "OS: Android"
            ],
            "₹1,08,780",
            "https://rog.asus.com/phones/rog-phone-6d-ultimate-model/"
        )

    # ---------------- VIVO ----------------
    with tab4:
        show_images([
            "https://carlosvassan.com/wp-content/uploads/2022/06/X80_Pro_Teaser59-1024x818.jpg"
        ])
        show_specs(
            "Vivo X80 Pro",
            [
                "Processor: Snapdragon 8 Gen 1",
                "Display: 6.78-inch AMOLED",
                "Camera: 50 MP Quad Camera",
                "Battery: 4700 mAh",
                "RAM & Storage: Up to 12GB | 512GB",
                "OS: Android"
            ],
            "₹79,999",
            "https://www.vivo.com/en/products/x80pro"
        )

    # ---------------- ONEPLUS ----------------
    with tab5:
        show_images([
            "https://images-eu.ssl-images-amazon.com/images/G/31/img21/Wireless/ssserene/OP11/LP/Flagship.png"
        ])
        show_specs(
            "OnePlus 11 5G",
            [
                "Processor: Snapdragon 8 Gen 2",
                "Display: 6.7-inch AMOLED",
                "Camera: 50 MP Triple Camera",
                "Battery: 5000 mAh",
                "RAM & Storage: Up to 16GB | 512GB",
                "OS: OxygenOS"
            ],
            "₹56,999",
            "https://www.oneplus.in/"
        )

# =========================================================
# PRICE PREDICTION
# =========================================================
elif section == "🔮 Price Prediction":

    st.subheader("Used Phone Price Range Prediction")

    brand = st.selectbox("Brand", sorted(data["Brand"].unique()))
    ram = st.slider("RAM (GB)", 2, 16, 6)
    storage = st.selectbox("Storage (GB)", [32, 64, 128, 256])
    camera = st.slider("Camera (MP)", 8, 108, 48)
    battery = st.slider("Battery (mAh)", 3000, 6000, 4500)
    display = st.slider("Display (inches)", 5.5, 7.2, 6.5)
    age = st.slider("Phone Age (Years)", 0, 5, 1)

    if st.button("Predict Price"):
        brand_enc = brand_encoder.transform([brand])[0]
        df = pd.DataFrame(
            [[brand_enc, ram, storage, camera, battery, display, age]],
            columns=["Brand","RAM","Storage","Camera","Battery","Display","Age"]
        )
        price = model.predict(df)[0]
        st.success(f"Estimated Price Range: ₹{int(price*0.9)} – ₹{int(price*1.1)}")

# =========================================================
# PHONE COMPARISON
# =========================================================
elif section == "📊 Phone Comparison":

    st.subheader("Phone Comparison")
    col1, col2 = st.columns(2)

    def phone(col, key):
        with col:
            brand = st.selectbox("Brand", sorted(data["Brand"].unique()), key=f"b{key}")
            ram = st.slider("RAM", 2, 16, 6, key=f"r{key}")
            storage = st.selectbox("Storage", [32,64,128,256], key=f"s{key}")
            camera = st.slider("Camera", 8,108,48, key=f"c{key}")
            battery = st.slider("Battery",3000,6000,4500,key=f"ba{key}")
            display = st.slider("Display",5.5,7.2,6.5,key=f"d{key}")
            age = st.slider("Age",0,5,1,key=f"a{key}")
        return brand,ram,storage,camera,battery,display,age

    p1 = phone(col1,1)
    p2 = phone(col2,2)

    if st.button("Compare"):
        def predict(p):
            enc = brand_encoder.transform([p[0]])[0]
            df = pd.DataFrame([[enc,*p[1:]]],
                columns=["Brand","RAM","Storage","Camera","Battery","Display","Age"])
            return model.predict(df)[0]

        price1, price2 = predict(p1), predict(p2)
        st.write(f"📱 Phone 1 Estimated Price: ₹{int(price1)}")
        st.write(f"📱 Phone 2 Estimated Price: ₹{int(price2)}")
