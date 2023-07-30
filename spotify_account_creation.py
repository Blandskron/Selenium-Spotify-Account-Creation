import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to generate a random email
def generate_random_email():
    characters = string.ascii_letters + string.digits
    email_random = ''.join(random.choice(characters) for _ in range(25)) + "@gmail.com"
    return email_random

# Set the maximum number of retries for the main process
MAX_RETRIES = 3

while True:
    try:
        driver_path = 'chromedriver.exe'  # Replace with the location of your Chrome driver
        driver = webdriver.Chrome(executable_path=driver_path)

        # URL of the form to be filled
        url = 'https://www.spotify.com/cl/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F'
        driver.get(url)

        # Locating form elements by their CSS, ID, or XPATH selectors
        email = driver.find_element(By.ID, "email")
        password = driver.find_element(By.ID, "password")
        displayname = driver.find_element(By.ID, "displayname")
        day = driver.find_element(By.ID, "day")
        month = driver.find_element(By.ID, "month")
        year = driver.find_element(By.ID, "year")
        female = driver.find_element(By.XPATH, '//span[contains(., "Mujer")]')
        driver.execute_script("arguments[0].scrollIntoView();", female)

        # Fill the form with random details
        random_email = generate_random_email()
        email.send_keys(random_email)
        password.send_keys("77777777777777")
        displayname.send_keys("fgit6ituert5ututudrftu")
        day.send_keys("7")
        month.send_keys("Marzo")
        year.send_keys("2005")
        female.click()

        # Click the button to create the account
        button = driver.find_element(By.CLASS_NAME, 'Button-sc-qlcn5g-0.kHvryD')
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

        # Wait for account creation and access another link
        time.sleep(20)

        url_another_link = 'https://open.spotify.com/artist/5PY9XPrDFuvO0nJMaRhIY7'
        driver.get(url_another_link)

        time.sleep(10)

        # Perform some actions on the accessed page
        span_element = driver.find_element(By.XPATH,'//span[contains(@class, "ButtonInner-sc-14ud5tc-0") and contains(@class, "gGxSiT") and contains(@class, "encore-bright-accent-set")]')
        span_element.click()

        time.sleep(5)

        # Perform some more actions on the accessed page
        boton_secondary = driver.find_element(By.CSS_SELECTOR, '[data-encore-id="buttonSecondary"]')
        boton_secondary.click()

        time.sleep(600)

        # Successfully completed the process, quit the driver
        driver.quit()
        

    except Exception as e:
        # Exception handling: Print the error message and restart the process if retries left
        print("An exception occurred:", e)
        driver.quit()

        if MAX_RETRIES <= 0:
            print("Maximum retries reached. Exiting...")
            

        MAX_RETRIES -= 1

# End of the script, driver has been quit
