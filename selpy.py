# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# import os

# # Setup headless Chrome
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# # Start the browser
# driver = webdriver.Chrome(options=options)
# driver.get("https://adminlte.io")
# time.sleep(3)

# # Create screenshot directory
# os.makedirs("screenshots", exist_ok=True)

# # Save screenshot
# screenshot_path = "screenshots/adminlte.png"
# driver.save_screenshot(screenshot_path)
# print(f"✅ Screenshot saved to {screenshot_path}")

# driver.quit()