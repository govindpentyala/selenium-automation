from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Open Expedia flight booking page
driver.get("https://www.expedia.com/Flights")

# Maximize the browser window
driver.maximize_window()

# Wait for the page to load
time.sleep(3)

# Enter the 'from' city
from_input = driver.find_element(By.ID, "location-field-leg1-origin")
from_input.click()
from_input.send_keys("New York")
from_input.send_keys(Keys.RETURN)

# Enter the 'to' city
to_input = driver.find_element(By.ID, "location-field-leg1-destination")
to_input.click()
to_input.send_keys("Los Angeles")
to_input.send_keys(Keys.RETURN)

# Select the departure date
departure_date = driver.find_element(By.ID, "d1-btn")
departure_date.click()
driver.find_element(By.XPATH, "//button[@data-day='25']").click()  # Select a specific date
driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']").click()

# Click search button
search_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-button']")
search_button.click()

# Wait for the results page to load
time.sleep(10)

# Close the browser
driver.quit()
