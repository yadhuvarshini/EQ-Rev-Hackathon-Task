import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

Cservice = webdriver.ChromeService(executable_path="C:/Users/yadhu/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

pincode = "600001"
product_url = "https://www.swiggy.com/instamart/item/N5SBE9SBEE?storeId=1402050"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Cservice)

driver.get("https://www.swiggy.com/")
time.sleep(5)

try:
    pincode_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your delivery location']")
    pincode_input.send_keys(pincode)
    time.sleep(2)

    suggestions = driver.find_elements(By.CLASS_NAME, "_2OORn")
    for s in suggestions:
        if "Chennai, Tamil Nadu 600001, India" in s.text:
            print("Clicked on suggestion:", s.text)
            s.click()
            break
    time.sleep(5)
except:
    print("Location input failed. Continuing...")

driver.get(product_url)
time.sleep(7)

variant_info = []

try:
    product_name = driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[2]/div[2]').text
    brandName = product_name[0:8]
    MRP_Price = driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]').text
    Final_Selling_Price = driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]').text
    Seller_details = driver.find_element(By.XPATH,'//*[@id="product-details-page-container"]/div/div[2]/div[5]/div').text

    print("Product Name:", product_name)
    print("MRP Price:", MRP_Price)
    print("Final Selling Price:", Final_Selling_Price)
    print("Seller Details:", Seller_details)

    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="product-details-page-container"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div/button').click()
    print("Clicked on variants button")
    time.sleep(5)

    variants_dropdown = driver.find_elements(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div')

    for v in variants_dropdown:
        sizes = v.find_elements(By.CLASS_NAME, "Pc2gm")
        prices = v.find_elements(By.CLASS_NAME, "_16peO")

        for i in range(len(sizes)):
            try:
                size_text = sizes[i].text
            except:
                size_text = "Unknown"

            try:
                price_text = prices[i].text
            except:
                price_text = "Unknown"

            try:
                stock_container = v.find_elements(By.CLASS_NAME, "_1sAUu")[i]
                stock_button = stock_container.find_elements(By.CLASS_NAME, "_2zozL")
                stock_status = "In Stock" if stock_button else "Out of Stock"
            except:
                stock_status = "Unknown"

            variant_info.append({
                "Pincode": pincode,
                "Product_Name": product_name,
                "Brand": brandName,
                "MRP": MRP_Price,
                "Selling_Price": Final_Selling_Price,
                "Seller": Seller_details,
                "Variant_Size": size_text,
                "Variant_Price": price_text,
                "Stock_Status": stock_status
            })

except Exception as e:
    print("❌ Error extracting product details:", e)

driver.quit()

# Save to CSV
df = pd.DataFrame(variant_info)
df.to_csv("product_variant_data.csv", index=False)
print("✅ Data saved to product_variant_data.csv")
