```markdown
# 🛒 Swiggy Instamart Product Variant Scraper (Selenium-based)

A Python-based web scraping script that automates the extraction of product details from Swiggy Instamart using Selenium. It captures key product information such as brand, MRP, final price, seller details, variant sizes, their prices, and stock availability — all location-specific (by pincode).

---

## 🚀 Features

- Automates location (pincode) setting on Swiggy.
- Fetches detailed product information including:
  - Product Name
  - Brand
  - MRP
  - Final Selling Price
  - Seller Details
  - Variant Sizes
  - Variant Prices
  - Stock Availability
- Stores the extracted data in a structured CSV file using `pandas`.

---

## 📂 Output Example (`product_variant_data.csv`)

| Pincode | Product_Name                          | Brand     | MRP | Selling_Price | Seller         | Variant_Size | Variant_Price | Stock_Status |
|---------|----------------------------------------|-----------|-----|----------------|----------------|--------------|----------------|---------------|
| 600001  | Too Yumm! B2G1 Potato Chips - Indian Masala | Too Yumm | 70  | 49             | Kwickbox Retail Pvt Ltd - Parrys | 84 g | 49 70        | In Stock     |
| 600001  | Too Yumm! B2G1 Potato Chips - Indian Masala | Too Yumm | 70  | 49             | Kwickbox Retail Pvt Ltd - Parrys | 84 g x 3 | 141 210     | Out of Stock |

---

## 🧰 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (match your Chrome version)

### Python Packages:
```bash
pip install selenium pandas
```

---

## 🔧 Setup & Usage

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/swiggy-product-scraper.git
cd swiggy-product-scraper
```

2. **Download ChromeDriver**:
   - [Download here](https://sites.google.com/chromium.org/driver/)
   - Place it in a known directory and update the path in the script.

3. **Edit and Run the Script**:
   - Open `scraper.py`
   - Set your desired:
     - `pincode`
     - `product_url`
   - Run:
```bash
python scraper.py
```

4. **Output**:
   - A CSV file named `product_variant_data.csv` will be saved in the same directory.

---

## 📌 Notes

- Ensure Swiggy’s product URL is valid and accessible.
- The script waits for elements using basic `time.sleep()` (could be optimized using `WebDriverWait`).
- Swiggy frequently updates their frontend — if selectors break, they may need to be updated.

---

## 🧑‍💻 Author

- **Your Name**  
- GitHub: [@yourusername](https://github.com/yadhuvarshini/)

---

## 📃 License

MIT License. Free to use and modify for personal or commercial use.
```

Let me know if you'd like help creating a logo, GIF demo, or turning this into a pip-installable package too.
