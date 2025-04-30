import time
import pyautogui 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

try:
   
    driver.get("https://mail.google.com/")
    print(" Opening Gmail...")

    
    wait.until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys("test@gmail.com", Keys.ENTER)
    print(" Email entered.")
    wait.until(EC.presence_of_element_located((By.NAME, "Passwd"))).send_keys("test@123", Keys.ENTER)
    print(" Password entered.")

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Compose']")))
    print(" Inbox loaded.")


    time.sleep(5)
    try:
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        print(" Simulated keyboard input.")
    except Exception as e:
        print(" Keyboard input failed:", e)

    
    try:
        no_thanks_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='No thanks']")))
        no_thanks_btn.click()
        print(" 'No thanks' clicked.")
    except:
        print(" 'No thanks' button not shown.")

  
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='More']"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#spam')]"))).click()
    print("📁 Spam folder opened.")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Spam')]")))

   
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search mail']")))
    search_box.clear()
    search_box.send_keys('subject:"Verify your Email address for your site account" in:spam', Keys.ENTER)
    print("🔍 Search executed.")

    try:
        email_xpath = "//span[contains(text(),'your site')]/ancestor::tr"
        email_row = wait.until(EC.presence_of_element_located((By.XPATH, email_xpath)))
        driver.execute_script("arguments[0].click();", email_row)
        print("✅ Email clicked")
    except Exception as e:
        print("❌ Email not found or not clickable:", e)
        driver.save_screenshot("email_click_failed.png")
        raise


    try:
        link_xpath = "//a[.//span[contains(text(),'Click')]]"
        verification_link = wait.until(EC.element_to_be_clickable((By.XPATH, link_xpath)))
        driver.execute_script("arguments[0].click();", verification_link)
        print("✅ Link clicked")
    except Exception as e:
        print("❌ Link not found:", e)
        driver.save_screenshot("link_click_failed.png")

except Exception as e:
    print("❌ Error:", e)
    driver.save_screenshot("final_error.png")

finally:
    driver.quit()
