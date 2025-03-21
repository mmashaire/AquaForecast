AquaForecast 🐟📈  
Sales Forecasting & Data Analysis for a Seafood Wholesaler *(Synthetic Data)*

---

📌 Overview

**AquaForecast** is a data analytics and forecasting project simulating weekly seafood sales for a wholesaler.  
It demonstrates how time series forecasting and product-specific analysis can support smarter inventory and procurement decisions in the seafood industry.

Built as a portfolio project using **synthetic data**, this simulates the type of dataset a real wholesale business might handle. It features forecasts for specific product types like **Salmon Fillet (with cut types and weight classes)**.

---

🔧 Features

✅ Synthetic dataset generator for realistic seafood sales (2022–2024)  
✅ Forecasting with [Facebook Prophet](https://facebook.github.io/prophet/)  
✅ Exploratory Data Analysis & visualizations  
✅ Holiday-aware forecasting (e.g., Christmas, Midsummer, etc.)  
✅ Drill-down into **product-level forecasts** (Salmon Fillet A/B/C etc.)  
✅ Clean modular code in Python (scripts + notebooks)

---

## 📂 Project Structure

```
AquaForecast/
│
├── data/                # Synthetic CSV datasets (not tracked in GitHub)
├── notebooks/           # Jupyter Notebooks for exploration & modeling
├── scripts/             # Python scripts (data generation, modeling)
├── requirements.txt     # Python dependencies
└── README.md            # You're reading it!
```

---

## 📊 Tools & Libraries

- Python 3.10+
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Prophet](https://facebook.github.io/prophet/)
- Jupyter Notebook

---

⚙️ How to Run

1. Clone the repo:

   git clone https://github.com/mmashaire/AquaForecast.git
   cd AquaForecast

2. Set up a virtual environment:

   python -m venv venv
   venv\Scripts\activate  # (Windows)

3. Install dependencies:

   pip install -r requirements.txt


4. Run data generation script (optional):

   python scripts/generate_synthetic_data.py

5. Open notebooks for analysis:
   
   jupyter notebook


---

🚫 Disclaimer

This project uses **synthetic data only**. No real company data is used or exposed.  
It is intended for **educational and portfolio purposes** only.

---

📬 Contact

Made by [@mmashaire](https://github.com/mmashaire)  
Feel free to fork, learn from it, or reach out!

---
