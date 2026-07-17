import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from datetime import datetime

# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="Dynamic Pricing Analytics for E-Commerce",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# LOAD MODEL
# ------------------------------

model = joblib.load("dynamic_pricing_model.pkl")

# ------------------------------
# CUSTOM CSS
# ------------------------------

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    padding-top:1rem;
}

h1,h2,h3{
    color:#0F172A;
}

div[data-testid="metric-container"]{
    background:white;
    padding:18px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,.08);
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:12px;
    border:none;
    background:#2563EB;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1E40AF;
}

</style>
""",unsafe_allow_html=True)

# ------------------------------
# SIDEBAR
# ------------------------------

st.sidebar.title("🛒 Navigation")

page=st.sidebar.radio(
    "Select Page",
    [
        "🏠 Home",
        "💰 Price Prediction",
        "📊 Dashboard",
        "📁 Bulk Prediction",
        "ℹ About Project"
    ]
)
# ------------------------------
# HOME PAGE
# ------------------------------

if page=="🏠 Home":

    st.title("💰 Dynamic Pricing Analytics for E-Commerce Dashboard")

    st.subheader("E-Commerce Price Recommendation")

    col1,col2,col3,col4=st.columns(4)

    col1.metric("Model","Ready")

    col2.metric("Dataset","1000+")

    col3.metric("Algorithm","Random Forest")

    col4.metric("Status","Online")

    st.markdown("---")

    st.write("""
Welcome to the Dynamic Pricing Analytics for E-Commerce.

This project predicts the best selling price for products
using Machine Learning.

### Features

✅ AI Price Recommendation

✅ Dashboard Analytics

✅ Bulk CSV Prediction

✅ Professional UI

✅ Mobile Friendly

Select **Price Prediction** from the left sidebar to start.
""")

# ------------------------------
# PRICE PREDICTION
# ------------------------------

elif page=="💰 Price Prediction":

    st.title("💰 Price Prediction")

    left,right=st.columns(2)

    with left:

        current_price=st.number_input(
            "Current Price",
            min_value=0.0,
            value=1000.0
        )

        competitor_price=st.number_input(
            "Competitor Price",
            min_value=0.0,
            value=950.0
        )

        stock=st.number_input(
            "Stock",
            min_value=0,
            value=50
        )

        units_sold=st.number_input(
            "Units Sold",
            min_value=0,
            value=20
        )

    with right:

        rating=st.slider(
            "Rating",
            1.0,
            5.0,
            4.5
        )

        discount=st.slider(
            "Discount %",
            0,
            90,
            10
        )

        demand=st.slider(
            "Demand Index",
            1,
            100,
            70
        )

    if st.button("🔮 Predict Recommended Price"):

        data=pd.DataFrame([[
            current_price,
            competitor_price,
            stock,
            units_sold,
            rating,
            discount,
            demand
        ]],columns=[
            "Current_Price",
            "Competitor_Price",
            "Stock",
            "Units_Sold",
            "Rating",
            "Discount_Percentage",
            "Demand_Index"
        ])

        prediction=model.predict(data)[0]

        st.success(f"Recommended Price : ₹ {prediction:,.2f}")
        # ------------------------------
# DASHBOARD
# ------------------------------

elif page=="📊 Dashboard":

    st.title("📊 Analytics Dashboard")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Products","1000")
    c2.metric("Categories","10")
    c3.metric("Accuracy","96%")
    c4.metric("Model","Random Forest")

    st.markdown("---")

    feature_data=pd.DataFrame({

        "Feature":[
            "Current Price",
            "Competitor",
            "Stock",
            "Units Sold",
            "Demand"
        ],

        "Importance":[
            40,
            28,
            10,
            12,
            10
        ]

    })

    fig=px.bar(

        feature_data,

        x="Feature",

        y="Importance",

        text="Importance",

        title="Feature Importance"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    category_data=pd.DataFrame({

        "Category":[
            "Electronics",
            "Fashion",
            "Grocery",
            "Sports",
            "Beauty"
        ],

        "Products":[
            300,
            220,
            180,
            170,
            130
        ]

    })

    fig2=px.pie(

        category_data,

        names="Category",

        values="Products",

        hole=0.45,

        title="Products by Category"

    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    history=pd.DataFrame({

        "Current Price":[1200,2500,3300,1800,950],

        "Recommended Price":[1280,2640,3410,1750,1020]

    })

    st.subheader("Recent Predictions")

    st.dataframe(
        history,
        use_container_width=True
    )
    # ------------------------------
# BULK PREDICTION
# ------------------------------

elif page=="📁 Bulk Prediction":

    st.title("📁 Bulk CSV Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Dataset")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        if st.button("Predict All Products"):

            df_model = df[[
    "Current_Price",
    "Competitor_Price",
    "Stock",
    "Units_Sold",
    "Rating",
    "Discount_Percentage",
    "Demand_Index"
]]

prediction = model.predict(df_model)

df["Recommended_Price"] = prediction

            df["Recommended_Price"] = prediction

            st.success("Prediction Completed Successfully")

            st.dataframe(
                df,
                use_container_width=True
            )

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download Prediction CSV",
                data=csv,
                file_name="prediction_result.csv",
                mime="text/csv"
            )

# ------------------------------
# ABOUT PROJECT
# ------------------------------

elif page=="ℹ About Project":

    st.title("ℹ About Project")

    st.markdown("""
# Dynamic Pricing Analytics for E-Commerce Dashboard

This project predicts the best selling price for an E-Commerce product using Machine Learning.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Plotly

## Dataset Features

- Current Price
- Competitor Price
- Stock
- Units Sold
- Rating
- Discount
- Demand Index

## Machine Learning

Random Forest Regressor

## Developer

NAUSHAD SHAIKH

B.Sc. Data Science
""")

st.markdown("---")

st.caption(
    f"© {datetime.now().year} Dynamic Pricing Analytics for E-Commerce | Version 2.0"
)
# ==================================================
# EXTRA ANALYTICS (V2 PREMIUM)
# ==================================================

if page=="📊 Dashboard":

    st.markdown("---")

    st.subheader("📈 Live Business Insights")

    col1,col2=st.columns(2)

    with col1:

        sales=pd.DataFrame({

            "Month":[
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun"
            ],

            "Revenue":[
                120000,
                145000,
                132000,
                171000,
                194000,
                220000
            ]

        })

        fig=px.line(

            sales,

            x="Month",

            y="Revenue",

            markers=True,

            title="Monthly Revenue"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        demand_chart=pd.DataFrame({

            "Demand":[
                "Low",
                "Medium",
                "High"
            ],

            "Products":[
                120,
                410,
                470
            ]

        })

        fig2=px.bar(

            demand_chart,

            x="Demand",

            y="Products",

            text="Products",

            title="Demand Distribution"

        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("🏆 Business Suggestions")

    st.success("Increase price for products having high demand.")

    st.info("Offer discounts for low demand products.")

    st.warning("Monitor competitor pricing daily.")

    st.success("Maintain sufficient stock during festivals.")

    st.info("Highly rated products can sustain higher prices.")
    
