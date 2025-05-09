import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Accept dynamic section input
section = sys.argv[1] if len(sys.argv) > 1 else "Billing"

# Auto-install correct chromedriver
chromedriver_autoinstaller.install()

# Set up headless browser
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.set_window_size(1280, 1024)

try:
    driver.get("https://demos.creative-tim.com/material-dashboard/pages/dashboard")
    time.sleep(3)

    # Clean up input to match href
    section_url = section.lower().replace(" ", "-")
    xpath = f"//a[contains(@href, '{section_url}.html')]"
    print(f"🔍 Looking for: {xpath}")

    link = driver.find_element(By.XPATH, xpath)
    link.click()
    print(f"✅ Clicked on section: {section}")

    time.sleep(2)
    os.makedirs("screenshots", exist_ok=True)
    screenshot_path = f"screenshots/{section_url}_page.png"
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot saved: {screenshot_path}")

except Exception as e:
    print(f"❌ Error: {e}")
    driver.save_screenshot("screenshots/error.png")

finally:
    driver.quit()