

import csv

def read_csv_to_dict(file_path, key_column):
    data_dict = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_dict[row[key_column]] = row
    return data_dict

def apply_pricing_rules(products, sales):
    updated_data = []
    for sku, product in products.items():
        current_price = float(product['current_price'])
        cost_price = float(product['cost_price'])
        stock = int(product['stock'])
        quantity_sold = int(sales.get(sku, {'quantity_sold': '0'})['quantity_sold'])

        new_price = current_price
        rule_applied = None

        # Rule 1
        if stock < 20 and quantity_sold > 30:
            new_price = current_price * 1.15
            rule_applied = "Rule 1"
        # Rule 2
        elif stock > 200 and quantity_sold == 0:
            new_price = current_price * 0.70
            rule_applied = "Rule 2"
        # Rule 3
        elif stock > 100 and quantity_sold < 20:
            new_price = current_price * 0.90
            rule_applied = "Rule 3"

        # Rule 4 – Ensure minimum 20% profit margin
        min_allowed_price = cost_price * 1.2
        if new_price < min_allowed_price:
            new_price = min_allowed_price
            rule_applied += " + Rule 4" if rule_applied else "Rule 4"

        new_price = round(new_price, 2)
        updated_data.append({
            'sku': sku,
            'old_price': f"{current_price:.2f} USD",
            'new_price': f"{new_price:.2f} USD"
        })

    return updated_data

def write_updated_prices(file_path, updated_data):
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['sku', 'old_price', 'new_price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in updated_data:
            writer.writerow(row)

# File paths
products_file = '/products.csv'
sales_file = '/sales.csv'
output_file = '/updated_prices.csv'

# Run the pricing engine
products = read_csv_to_dict(products_file, 'sku')
sales = read_csv_to_dict(sales_file, 'sku')
updated_prices = apply_pricing_rules(products, sales)
write_updated_prices(output_file, updated_prices)