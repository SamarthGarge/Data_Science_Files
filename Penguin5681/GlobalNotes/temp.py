from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Amazon website
driver.get("https://www.amazon.com")

# Wait for the page to load
time.sleep(3)  # Adjust the sleep time as necessary

# Execute JavaScript to create and show an alert
driver.execute_script('alert("Amazon website opened successfully");')

# Optional: Wait to see the alert before closing the browser
time.sleep(5)  # Adjust the sleep time as necessary

# Close the browser
driver.quit()