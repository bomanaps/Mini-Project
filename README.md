# Mini-Project
# 📊 Celo Ecosystem Insights Dashboard

This is a minimal Streamlit dashboard that visualizes real-time cUSD balance distribution across top addresses on the Celo blockchain.

---

## 🔍 Features

- View the **total cUSD balance** across tracked accounts.
- Explore the **top 20 holders** of cUSD using a bar chart.
- Analyze **token inflows, outflows, and net balance changes** in an interactive table.

---

## 📁 Data Source

The data is fetched from a [Dune Analytics](https://dune.com/queries/5354328) query and saved as a CSV file:  
`data/celo_balances.csv`

Expected columns:

- `address`
- `balance`
- `tokens_in`
- `tokens_out`
- `balance_changed`

---

## How to Run

1. Clone the repo and navigate to the project directory.

2. Create a Python environment and install dependencies:
   ```bash
   pip install streamlit pandas matplotlib

