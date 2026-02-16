import streamlit as st

st.set_page_config(page_title="FOB vs FTZ Simulator", layout="wide")
DAYS_IN_YEAR = 360


# ======================================================
# CUSTOM STYLING (PROFESSIONAL LOOK)
# ======================================================

st.markdown("""
<style>

/* ======= MAIN TITLE ======= */
.main-title {
    text-align:center;
    font-size:28px;
    font-weight:600;
    color:#0F172A;
}

.sub-text {
    text-align:center;
    color:#475569;
    font-size:15px;
    max-width:750px;
    margin:auto;
    line-height:1.6;
}

.section-header {
    font-size:18px;
    font-weight:600;
    color:#1E293B;
    padding:8px 0px;
}

.column-header {
    font-size:13px;
    font-weight:600;
    color:#334155;
}

/* ======= INPUT FIELD STYLING ======= */

/* Reduce input height */
div[data-baseweb="input"] > div {
    height: 30px !important;
}

/* Add black border */
/*div[data-baseweb="input"] {
    border: 0.2px solid black !important;
    border-radius: 8px !important;
    
}*/
         
          
/* Reduce padding inside input */
div[data-baseweb="input"] input {
    padding: 4px 8px !important;
    font-size: 14px !important;
}

/* Remove large spacing between rows */
.block-container {
    padding-top: 1.9rem !important;
}

/* Tighten column vertical alignment */
[data-testid="column"] {
    display: flex;
    align-items: center;
}

/* Button styling (keep yours but slightly refined) */
.stButton>button {
    background-color:#0E7490;
    color:white;
    font-weight:600;
    border-radius:6px;
    height:38px;
}

.stButton>button:hover {
    background-color:#0E7490;
    color:white;
}

hr {
    margin-top:6px;
    margin-bottom:6x;
}
            
/* ===============================
   FOB INPUT BACKGROUND
   =============================== */
input[aria-label^="fob"] {
    background-color: #EAF2FB !important;
}

/* ===============================
   FTZ INPUT BACKGROUND
   =============================== */
input[aria-label^="ftz"] {
    background-color: #E9F7EF !important;
}

/* Keep border clean */
div[data-baseweb="input"] > div {
    border: 1px solid #CBD5E1 !important;
    border-radius: 6px !important;
}

/* Remove default grey background */
div[data-baseweb="input"] > div {
    background-color: transparent !important;
}



  



/* ==========================================
   REMOVE RED FOCUS BORDER (STREAMLIT 1.47)
   ========================================== */

/* Remove red focus ring from stNumberInput wrapper */
[data-testid="stNumberInput"] > div:focus-within {
    box-shadow: none !important;
    border: none !important;
}

/* Remove red outline from inner BaseWeb input */
[data-baseweb="input"]:focus-within {
    box-shadow: none !important;
    border-color: none !important;
}

/* Remove browser default outline */
input:focus {
    outline: none !important;
    box-shadow: none !important;
}

/* Remove red focus from stepper buttons */
button:focus {
    outline: none !important;
    box-shadow: none !important;
}          


</style>
""", unsafe_allow_html=True)


# ======================================================
# HEADER
# ======================================================

#st.markdown('<div class="main-title">Cash-to-Cash Simulator</div>', unsafe_allow_html=True)
#st.write(st.__version__)
# left, center, right = st.columns([2, 1, 2])
# with center:
#     st.image("mas_logo.jpg", width=140)

import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_base64 = get_base64_image("mas_logo.jpg")

st.markdown(f"""
<div style="text-align:center; margin-top:5px;">
    <h3 style="margin-bottom:1px;">
        Cash-to-Cash Simulator
    </h3>
    <img src="data:image/jpg;base64,{logo_base64}" 
         width="150" 
         style="display:block; margin:auto;">
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-text">
An interactive financial simulator designed to compare FOB and FTZ supply chain models across Cash-to-Cash Cycle, Inventory Efficiency, and Profitability Performance Metrics.
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# INPUT SECTION HEADER
# ======================================================

st.markdown('<div class="section-header">Data Inputs</div>', unsafe_allow_html=True)
# st.caption("Please enter all required values below.")
# st.subheader("Data Inputs",help=("Please Enter Your Inputs"
        
#     ),)

#st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# COLUMN HEADERS (FORMATTED)
# ======================================================

h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13 = st.columns(13)

h1.markdown('<div class="column-header">Model</div>', unsafe_allow_html=True)
h2.markdown('<div class="column-header">LDP ($)</div>', unsafe_allow_html=True)
h3.markdown('<div class="column-header">PO Payment Terms</div>', unsafe_allow_html=True)
h4.markdown('<div class="column-header">PO → DC</div>', unsafe_allow_html=True)
h5.markdown('<div class="column-header">DC → Store</div>', unsafe_allow_html=True)
h6.markdown('<div class="column-header">Customer Turns</div>', unsafe_allow_html=True)
h7.markdown('<div class="column-header">Store → Customer</div>', unsafe_allow_html=True)
h8.markdown('<div class="column-header">FTZ Payment Terms</div>', unsafe_allow_html=True)
h9.markdown('<div class="column-header">Lead Time</div>', unsafe_allow_html=True)
h10.markdown('<div class="column-header">In Stock %</div>', unsafe_allow_html=True)
h11.markdown('<div class="column-header">Out of Stock %</div>', unsafe_allow_html=True)
h12.markdown('<div class="column-header">Avg Inventory (Units)</div>', unsafe_allow_html=True)
h13.markdown('<div class="column-header">Gross Profit ($)</div>', unsafe_allow_html=True)

#st.markdown("<hr>", unsafe_allow_html=True)



# ======================================================
# FOB ROW
# ======================================================

#st.markdown('<div class="fob-row">', unsafe_allow_html=True)
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = st.columns(13)

#c1.markdown("**FOB (Current)**")
c1.markdown('<div class="column-header">FOB (Current)</div>', unsafe_allow_html=True)
fob_landed = c2.number_input("", value=2.00, key="fob_landed",label_visibility="collapsed")
fob_po_terms = c3.number_input("", value=60, key="fob_po",label_visibility="collapsed")
fob_po_dc = c4.number_input("", value=60, key="fob_podc",label_visibility="collapsed")
fob_dc_store = c5.number_input("", value=14, key="fob_dcstore",label_visibility="collapsed")
fob_turns = c6.number_input("", value=4, key="fob_turns",label_visibility="collapsed")

# fob_store_customer = DAYS_IN_YEAR / fob_turns
# fob_store_customer = c7.number_input("", value=fob_store_customer)

fob_store_customer = int(DAYS_IN_YEAR / fob_turns)
fob_store_customer = c7.number_input("", value=fob_store_customer, step=1, format="%d",label_visibility="collapsed")


c8.markdown(" ")
fob_lead_time = c9.number_input("", value=74, key="fob_lead",label_visibility="collapsed")
fob_instock = c10.number_input("", value=92.0, key="fob_in",label_visibility="collapsed")
fob_outstock = c11.number_input("", value=8.0, key="fob_out",label_visibility="collapsed")
#fob_avg_inventory = c12.number_input("", value=25000, key="fob_avg_inv",format="%d",step=1,label_visibility="collapsed")
fob_avg_inventory = c12.text_input(
    "",
    value=f"{25000:,}",
    key="fob_avg_inv",
    label_visibility="collapsed"
)

# Convert back to number
fob_avg_inventory = int(fob_avg_inventory.replace(",", ""))

#fob_gross_profit_input = c13.number_input("", value=300000, key="fob_gp",format="%d",step=1,label_visibility="collapsed")
fob_gross_profit_input = c13.text_input(
    "",
    value=f"{300000:,}",
    key="fob_gp",
    label_visibility="collapsed"
)

# Convert back to number
fob_gross_profit_input = int(fob_gross_profit_input.replace(",", ""))
#st.markdown('</div>', unsafe_allow_html=True)
# ======================================================
# FTZ ROW
# ======================================================
#st.markdown('<div class="ftz-row">', unsafe_allow_html=True)
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = st.columns(13)

#c1.markdown("**FTZ (Proposed)**")
c1.markdown('<div class="column-header">FTZ (Proposed)</div>', unsafe_allow_html=True)
ftz_landed = c2.number_input("", value=2.10, key="ftz_landed",label_visibility="collapsed")
c3.markdown(" ")
ftz_po_dc = c4.number_input("", value=7, key="ftz_podc",label_visibility="collapsed")
ftz_dc_store = c5.number_input("", value=7, key="ftz_dcstore",label_visibility="collapsed")
ftz_turns = c6.number_input("", value=12, key="ftz_turns",label_visibility="collapsed")

ftz_store_customer = int(DAYS_IN_YEAR / ftz_turns)
ftz_store_customer = c7.number_input("", value=ftz_store_customer, step=1, format="%d",label_visibility="collapsed")

ftz_po_terms = c8.number_input("", value=14, key="ftz_terms",label_visibility="collapsed")

ftz_lead_time = c9.number_input("", value=14, key="ftz_lead",label_visibility="collapsed")
ftz_instock = c10.number_input("", value=96.0, key="ftz_in",label_visibility="collapsed")
ftz_outstock = c11.number_input("", value=4.0, key="ftz_out",label_visibility="collapsed")
#ftz_avg_inventory = c12.number_input("", value=8333, key="ftz_avg_inv",format="%d",step=1, label_visibility="collapsed")
ftz_avg_inventory = c12.text_input(
    "",
    value=f"{8333:,}",
    key="ftz_avg_inv",
    label_visibility="collapsed"
)

# Convert back to number
ftz_avg_inventory = int(ftz_avg_inventory.replace(",", ""))

#ftz_gross_profit_input = c13.number_input("", value=290000, key="ftz_gp",format="%d",step=1, label_visibility="collapsed")
ftz_gross_profit_input = c13.text_input(
    "",
    value=f"{290000:,}",
    key="ftz_gp",
    label_visibility="collapsed"
)

# Convert back to number
ftz_gross_profit_input = int(ftz_gross_profit_input.replace(",", ""))
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# COMMON INPUTS
# ======================================================
st.markdown('<div class="section-header">Common Data Inputs</div>', unsafe_allow_html=True)


#st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# COLUMN HEADERS (FORMATTED)
# ======================================================

h1, h2, h3 = st.columns(3)

DAYS_IN_YEAR = h1.number_input("Days in Year", value=360, key="DAYS_IN_YEAR", disabled=True)
#annual_units = h2.number_input("Annual Unit Sales", value=100000, key="annual_units",format="%d", step=1)
annual_units = h2.text_input(
    "Annual Unit Sales",
    value=f"{100000:,}",
    key="annual_units"
)

# Convert back to number
annual_units= int(annual_units.replace(",", ""))

selling_price = h3.number_input("Selling Price per Unit ($)", value=5.0, key="selling_price")

##annual_units = st.number_input("Annual Unit Sales", value=100000)
#selling_price = st.number_input("Selling Price per Unit ($)", value=5.00)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# CALCULATE BUTTON
# ======================================================

calculate = st.button("Calculate")

# ======================================================
# CALCULATIONS
# ======================================================

def calculate_model(landed, po_terms, po_dc, dc_store, turns):
    store_to_customer = DAYS_IN_YEAR / turns
    inventory_days = po_dc + dc_store + store_to_customer
    c2c = inventory_days - po_terms

    revenue = selling_price * annual_units
    cogs = landed * annual_units
    gross_profit = revenue - cogs

    avg_inventory_units = annual_units / turns
    avg_inventory_value = avg_inventory_units * landed
    gmroi = gross_profit / avg_inventory_value if avg_inventory_value != 0 else 0

    return gmroi, c2c





# ======================================================
# RESULTS (Excel Style Layout)
# ======================================================

if calculate:

    # fob_gmroi, fob_c2c = calculate_model(
    #     fob_landed, fob_po_terms, fob_po_dc, fob_dc_store, fob_turns
    # )

    # ftz_gmroi, ftz_c2c = calculate_model(
    #     ftz_landed, ftz_po_terms, ftz_po_dc, ftz_dc_store, ftz_turns
    # )

     
    # FOB Calculations
    # -------------------------------

    # Inventory Days
    fob_inventory_days = fob_lead_time + fob_store_customer

    # Cash to Cash Cycle
    fob_c2c = fob_inventory_days - fob_po_terms

    # Average Inventory Value
    fob_avg_inventory_value = fob_avg_inventory * fob_landed

    # GMROI (using user input gross profit)
    if fob_avg_inventory_value != 0:
        fob_gmroi = fob_gross_profit_input / fob_avg_inventory_value
    else:
        fob_gmroi = 0


    # -------------------------------
    # FTZ Calculations
    # -------------------------------

    # Inventory Days
    ftz_inventory_days = ftz_lead_time + ftz_store_customer

    # Cash to Cash Cycle
    ftz_c2c = ftz_inventory_days - ftz_po_terms

    # Average Inventory Value
    ftz_avg_inventory_value = ftz_avg_inventory * ftz_landed

    # GMROI (using user input gross profit)
    if ftz_avg_inventory_value != 0:
        ftz_gmroi = ftz_gross_profit_input / ftz_avg_inventory_value
    else:
        ftz_gmroi = 0

    st.markdown("<br>", unsafe_allow_html=True)

    # Header Row
    col1, col2, col3 = st.columns([2, 2, 2])

    col1.markdown("")

    col2.markdown("""
        <div style="
            background-color:#0E7490;
            color:white;
            padding:8px;
            text-align:center;
            font-weight:600;
            border-radius:4px;">
            Cash to Cash Cycle
        </div>
    """, unsafe_allow_html=True)

    col3.markdown("""
        <div style="
            background-color:#FACC15;
            color:black;
            padding:8px;
            text-align:center;
            font-weight:600;
            border-radius:4px;">
            GMROI (Gross Margin Return on Investment)
        </div>
    """, unsafe_allow_html=True)

    # FOB Row
    col1, col2, col3 = st.columns([2, 2, 2])

    col1.markdown("**FOB Model (Current)**")
    col2.markdown(f"""
        <div style="
            padding:8px;
            text-align:center;
            border:1px solid #CBD5E1;
            border-radius:4px;">
            {fob_c2c:.0f}
        </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
        <div style="
            padding:8px;
            text-align:center;
            border:1px solid #CBD5E1;
            border-radius:4px;">
            {fob_gmroi:.2f}
        </div>
    """, unsafe_allow_html=True)

    # FTZ Row
    col1, col2, col3 = st.columns([2, 2, 2])

    col1.markdown("**FTZ Model (Proposed)**")
    col2.markdown(f"""
        <div style="
            padding:8px;
            text-align:center;
            border:1px solid #CBD5E1;
            border-radius:4px;">
            {ftz_c2c:.0f}
        </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
        <div style="
            padding:8px;
            text-align:center;
            border:1px solid #CBD5E1;
            border-radius:4px;">
            {ftz_gmroi:.2f}
        </div>
    """, unsafe_allow_html=True)



import matplotlib.pyplot as plt
import numpy as np

if calculate:
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<div class="section-header">Operational & Cash Flow Impact</div>', unsafe_allow_html=True)


    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # =====================================================
    # 1️⃣ Lead Time vs Safety Stock
    # =====================================================
   
    with col1:

        # --- Real Demand ---
        daily_demand = annual_units / DAYS_IN_YEAR
        demand_std = daily_demand * 0.2
        z = 1.65  # 95% service level

        # --- Use FOB values for visualization ---
        lead_time = fob_lead_time

        safety_stock = z * demand_std * np.sqrt(lead_time)

        reorder_point = daily_demand * lead_time + safety_stock

        cycle_stock = fob_avg_inventory * 2
        max_inventory = cycle_stock + safety_stock

        # --- Create Sawtooth Pattern ---
        cycle_days = int(max_inventory / daily_demand)
        total_days = cycle_days * 3

        days = np.arange(0, total_days)
        inventory = max_inventory - (daily_demand * (days % cycle_days))

        fig, ax = plt.subplots(figsize=(4,3))

        ax.plot(days, inventory, linewidth=1.8)

        # Safety stock line
        ax.axhline(safety_stock, linestyle="--")

        # Reorder point line
        ax.axhline(reorder_point, linestyle=":")

        # Plot Inventory (Sawtooth)
        ax.plot(days, inventory, 
                linewidth=1.8, 
                label="FOB Inventory Level")

        # Safety Stock Line
        ax.axhline(safety_stock, 
                linestyle="--", 
                label="FOB Safety Stock")

        # Reorder Point Line
        ax.axhline(reorder_point, 
                linestyle=":", 
                label="FOB Reorder Point")

        # Add Value Labels
        ax.text(days[-1], safety_stock, 
                f"{int(safety_stock)}", 
                fontsize=7, 
                verticalalignment='bottom')

        ax.text(days[-1], reorder_point, 
                f"{int(reorder_point)}", 
                fontsize=7, 
                verticalalignment='bottom')

        ax.text(0, max_inventory, 
                f"{int(max_inventory)}", 
                fontsize=7, 
                verticalalignment='bottom')

        # Formatting
        ax.set_title("FOB Stock Control Chart (Days)", fontsize=9)
        ax.set_xlabel("Time (Days)", fontsize=8)
        ax.set_ylabel("Inventory (Units)", fontsize=8)
        ax.tick_params(axis='both', labelsize=7)

        ax.legend(fontsize=7, loc="upper right")


        st.pyplot(fig)


    

    

    # =====================================================
    # 2️⃣ MOQ / Inventory Value
    # =====================================================
    with col2:

        models = ["FOB", "FTZ"]
        avg_inventory_values = [
            fob_avg_inventory * fob_landed,
            ftz_avg_inventory * ftz_landed
        ]

        fig2, ax2 = plt.subplots(figsize=(4,3))

        ax2.bar(models, avg_inventory_values)

        ax2.set_title("Working Capital", fontsize=8)
        ax2.set_ylabel("Inventory Value ($)", fontsize=8)
        ax2.tick_params(axis='both', labelsize=7)

        st.pyplot(fig2)


    # =====================================================
    # 3️⃣ Cash-to-Cash Timeline
    # =====================================================
    with col3:

        fig3, ax3 = plt.subplots(figsize=(4,3))

        ax3.hlines(1, 0, fob_c2c, linewidth=4)
        ax3.hlines(0.6, 0, ftz_c2c, linewidth=4)

        # Set Y-axis labels
        ax3.set_yticks([1, 0.6])
        ax3.set_yticklabels(["FOB", "FTZ"], fontsize=8)

        ax3.set_ylim(0, 1.5)
        # ax3.set_yticks([])
        ax3.set_title("C2C Comparison", fontsize=8)
        ax3.set_xlabel("Days", fontsize=8)
        ax3.tick_params(axis='x', labelsize=7)

        st.pyplot(fig3)

# ======================================================
# EQUATIONS SECTION (COLLAPSABLE)
# ======================================================

with st.expander("📘 View Model Equations & Financial Logic"):

    st.markdown("### 🔹 Inventory & Demand Equations")

    st.latex(r"""
    Daily\ Demand = \frac{Annual\ Unit\ Sales}{Days\ in\ Year}
    """)

    st.latex(r"""
    Store\ to\ Customer\ (Days) = \frac{Days\ in\ Year}{Customer\ Turns}
    """)

    st.latex(r"""
    Lead\ Time = PO\to DC + DC\to Store
    """)

    st.markdown("---")

    st.markdown("### 🔹 Safety Stock & Reorder Point")

    st.latex(r"""
    Safety\ Stock = Z \times \sigma_d \times \sqrt{Lead\ Time}
    """)

    st.latex(r"""
    Reorder\ Point = (Daily\ Demand \times Lead\ Time) + Safety\ Stock
    """)

    st.markdown("---")

    st.markdown("### 🔹 Financial & Profitability Equations")

    st.latex(r"""
    Revenue = Selling\ Price \times Annual\ Unit\ Sales
    """)

    st.latex(r"""
    COGS = Landed\ Cost \times Annual\ Unit\ Sales
    """)

    st.latex(r"""
    Gross\ Profit = Revenue - COGS
    """)

    st.latex(r"""
    Average\ Inventory\ Value = Average\ Inventory\ Units \times Landed\ Cost
    """)

    st.latex(r"""
    GMROI = \frac{Gross\ Profit}{Average\ Inventory\ Value}
    """)

    st.markdown("---")

    st.markdown("### 🔹 Cash Conversion Cycle (C2C)")

    st.latex(r"""
    Inventory\ Days = Lead\ Time + Store\ to\ Customer
    """)

    st.latex(r"""
    Cash\ to\ Cash\ Cycle = Inventory\ Days - PO\ Payment\ Terms
    """)

    st.markdown("---")

    st.markdown("### 🔹 Working Capital Impact")

    st.latex(r"""
    Working\ Capital = Average\ Inventory\ Units \times Landed\ Cost
    """)

    st.markdown(
        """
        **Interpretation:**  
        Longer lead time and higher MOQ increase safety stock and average inventory,
        which increases working capital and extends the cash-to-cash cycle.
        """
    )
    st.markdown("---")

    st.markdown("### 🔹 Safety Stock & Reorder Point (Stock Control Chart)")

    st.latex(r"""
    \sigma_d = Daily\ Demand \times Demand\ Variability\%
    """)

    st.latex(r"""
    Safety\ Stock = Z \times \sigma_d \times \sqrt{Lead\ Time}
    """)

    st.latex(r"""
    Reorder\ Point = (Daily\ Demand \times Lead\ Time) + Safety\ Stock
    """)

    st.latex(r"""
    Cycle\ Stock = 2 \times Average\ Inventory
    """)

    st.latex(r"""
    Maximum\ Inventory = Cycle\ Stock + Safety\ Stock
    """)

    st.latex(r"""
    Inventory(t) = Maximum\ Inventory - (Daily\ Demand \times t)
    """)

    st.markdown(
        """
        **Interpretation:**  
        The saw-tooth inventory pattern is generated by continuous daily consumption.  
        When inventory reaches the Reorder Point, a new order is placed, which arrives after the Lead Time.  
        Safety Stock protects against demand variability during the Lead Time.
        """
    )

    



