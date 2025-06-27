import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Config ---
st.set_page_config(page_title="Celo Insights", layout="wide")

# --- Sidebar ---
st.sidebar.title("About")
st.sidebar.info(
    "Celo Ecosystem Insights Dashboard\n\n"
    "Data source: [Your Data Source](#)\n"
    "Built with Streamlit."
)

# --- Main Title ---
st.title("📊 Celo Ecosystem Insights")
st.markdown("Track current cUSD balances on the Celo blockchain")

# --- Load Data ---
@st.cache_data
def load_balances_data():
    df = pd.read_csv("data/celo_balances.csv")
    return df

balances_df = load_balances_data()

# --- Metrics Row ---
col1, col2 = st.columns(2)
with col1:
    total_balance = balances_df['balance'].sum()
    st.metric("Total cUSD Balance", f"${total_balance:,.2f}")
with col2:
    st.metric("Tracked Addresses", f"{balances_df['address'].nunique()}")

st.divider()

# --- Bar Chart of Top Addresses ---
st.subheader("🏦 Top 20 Addresses by Balance")
top_balances = balances_df.sort_values("balance", ascending=False).head(20).copy()
top_balances['short_address'] = top_balances['address'].apply(lambda x: x[:6] + '...' + x[-4:])

# Create custom color palette - each bar gets its own color
colors = [
    '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
    '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9',
    '#F8C471', '#82E0AA', '#F1948A', '#AED6F1', '#D7BDE2',
    '#F9E79F', '#A9DFBF', '#F5B7B1', '#D2B4DE', '#AED6F1'
]

# Create bar chart with individual colors
fig = go.Figure()

# Add each bar individually with its own color
for i, row in top_balances.iterrows():
    fig.add_trace(go.Bar(
        x=[row['short_address']],
        y=[row['balance']],
        name=row['short_address'],
        marker_color=colors[i % len(colors)],  # Cycle through colors
        text=f"${row['balance']/1000000:.1f}M" if row['balance'] >= 1000000 else f"${row['balance']/1000:.0f}K",
        textposition='outside',
        textfont=dict(size=11, color='black'),
        hovertemplate=f'<b>Full Address:</b> {row["address"]}<br><b>Balance:</b> $%{{y:,.2f}}<extra></extra>',
        showlegend=False
    ))

# Update layout with corrected syntax
fig.update_layout(
    title=dict(
        text="Top 20 Addresses by cUSD Balance",
        font=dict(size=16, color='#374151'),
        x=0.02,
        xanchor='left'
    ),
    xaxis=dict(
        title=dict(
            text="Address",
            font=dict(size=12, color='#6b7280')
        ),
        tickangle=-45,
        tickfont=dict(size=10, color='#6b7280'),
        showgrid=False,
        showline=False,
        zeroline=False
    ),
    yaxis=dict(
        title=dict(
            text="Balance (cUSD)",
            font=dict(size=12, color='#6b7280')
        ),
        tickfont=dict(size=10, color='#6b7280'),
        showgrid=True,
        gridcolor='#f3f4f6',
        gridwidth=1,
        showline=False,
        zeroline=False,
        tickformat='$,.0f'
    ),
    plot_bgcolor='white',
    paper_bgcolor='white',
    height=500,
    margin=dict(l=80, r=40, t=80, b=120),
    font=dict(family="Arial, sans-serif")
)

# Ensure text labels don't get clipped
fig.update_traces(cliponaxis=False)

st.plotly_chart(fig, use_container_width=True)

with st.expander("Show Top 20 Table"):
    st.dataframe(
        top_balances[["address", "balance"]].reset_index(drop=True)
    )

st.download_button(
    "Download Top 20 as CSV",
    top_balances.to_csv(index=False),
    file_name="top20_celo_balances.csv",
    mime="text/csv"
)

st.divider()

# --- Token Flows Table ---
st.subheader("🔁 Token Inflows and Outflows")
styled_df = balances_df[['address', 'tokens_in', 'tokens_out', 'balance_changed']]
styled_df = styled_df.sort_values("balance_changed", ascending=False)
styled_df = styled_df.reset_index(drop=True)
styled_df = styled_df.style.background_gradient(
    subset=['balance_changed'], cmap='RdYlGn'
)
st.dataframe(
    styled_df,
    use_container_width=True
)

# --- Download Data ---
st.download_button(
    "Download Data as CSV",
    balances_df.to_csv(index=False),
    file_name="celo_balances.csv",
    mime="text/csv"
)