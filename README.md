# Pricing-Engine

## Overview

This project implements a dynamic pricing engine that updates product prices based on current inventory and recent sales data. 

---

## Files Included

- `pricing_engine.py` – The main Python script to run the pricing logic.
- `products.csv` – Sample product inventory file.
- `sales.csv` – Sample sales data file.
- `updated_prices.csv` – The output file with adjusted prices.
- `README.md` – This file

---

## How It Works

1. **Reads Input Files:**
   - `products.csv`: Contains `sku`, `name`, `current_price`, `cost_price`, `stock`
   - `sales.csv`: Contains `sku`, `quantity_sold`

2. **Applies Rules in Precedence:**
   - Rule 1: Low Stock + High Demand  +15%
   - Rule 2: Dead Stock (stock > 200, no sales)  -30%
   - Rule 3: Overstocked (stock > 100, low sales)  -10%
   - Rule 4: Ensures minimum 20% profit over cost price

3. **Generates Output:**
   - `updated_prices.csv` with columns:
     - `sku`
     - `old_price` (with "USD" suffix)
     - `new_price` (with "USD" suffix)
