import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    print("=== BẮT ĐẦU KIỂM THỬ TỰ ĐỘNG ===")
    
    # --- TEST CASE 1: ĐĂNG NHẬP THÀNH CÔNG ---
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    assert "inventory.html" in driver.current_url
    print("👉 Test Case 1: Đăng nhập thành công -> PASSED")

    # --- TEST CASE 2: THÊM SẢN PHẨM VÀO GIỎ HÀNG ---
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    
    assert cart_badge == "1"
    print("👉 Test Case 2: Thêm sản phẩm vào giỏ hàng thành công -> PASSED")

    # --- TEST CASE 3: ĐĂNG XUẤT ---
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1) # Chờ menu mở ra
    driver.find_element(By.ID, "logout_sidebar_link").click()
    
    assert "saucedemo.com" in driver.current_url
    print("👉 Test Case 3: Đăng xuất thành công -> PASSED")
    
    print("=== TẤT CẢ TEST CASES ĐỀU ĐẠT (PASSED) ===")

except Exception as e:
    print(f"❌ Có lỗi xảy ra: {e}")

finally:
    driver.quit()