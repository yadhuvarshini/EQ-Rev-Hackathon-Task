from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Config
pincodes = ["600002", "600018", "600008", "110006", "110008", "122003"]
product_ids = ["B0DDZF3EGB", "LNSIN80D9X", "YRL5V0ED04"]
base_url = "https://www.swiggy.com/instamart/item/{}?storeId=1402050"
chromedriver_path = "C:/Users/yadhu/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Chrome Setup
options = Options()
options.add_argument("--start-maximized")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

results = []

for pincode in pincodes:
    driver.get("https://www.swiggy.com/")
    time.sleep(5)

    try:
        # Enter pincode
        input_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter your delivery location']")
        input_box.send_keys(pincode)
        time.sleep(3)

        # Select location from dropdown
        suggestions = driver.find_elements(By.CLASS_NAME, "_2OORn")
        for s in suggestions:
            if pincode in s.text:
                s.click()
                print(f"📍 Location selected for pincode {pincode}")
                break
        time.sleep(4)
    except:
        print(f"⚠️ Failed to select location for {pincode}")
        continue

    for pid in product_ids:
        url = base_url.format(pid)
        driver.get(url)
        time.sleep(5)

        try:
            product_name = driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[2]/div[2]').text
            brand_name = product_name.split()[0]
            mrp_price = driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]').text
            final_price = driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]').text
            seller = driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[5]/div').text

            # Click variant dropdown
            driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/button').click()
            time.sleep(2)

            variants_dropdown = driver.find_elements(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/button')

            for v in variants_dropdown:
                try:
                    size = v.find_element(By.CLASS_NAME, "Pc2gm").text
                    price = v.find_element(By.CLASS_NAME, "_16peO").text

                    # Stock check inside this variant
                    try:
                        stock_container = v.find_element(By.CLASS_NAME, "_1sAUu")
                        stock_button = stock_container.find_elements(By.CLASS_NAME, "_2zozL")
                        stock_status = "In Stock" if stock_button else "Out of Stock"
                    except:
                        stock_status = "Unknown"

                    results.append({
                        "Pincode": pincode,
                        "Product_ID": pid,
                        "Product_URL": url,
                        "Product_Name": product_name,
                        "Brand": brand_name,
                        "MRP_Price": mrp_price,
                        "Final_Selling_Price": final_price,
                        "Variant_Size": size,
                        "Variant_Price": price,
                        "Stock_Status": stock_status,
                        "Store_Address": seller
                    })
                except Exception as e:
                    print("❌ Error parsing variant:", e)

        except Exception as e:
            print(f"⚠️ Could not extract details for {pid} at {pincode}: {e}")

driver.quit()

# Save to Excel
df = pd.DataFrame(results)
df.to_excel("instamart_scraped_data.xlsx", index=False)
print("✅ Data scraping completed and saved to Excel.")
