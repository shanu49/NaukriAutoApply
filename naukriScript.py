import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/mnjuser/homepage")
username = driver.find_element(By.XPATH, "//input[@id='usernameField']")
username.send_keys("Type UserID") # Type your UserID
password = driver.find_element(By.XPATH, "//input[@id='passwordField']")
password.send_keys("Type password") # Type your Password
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(5)
jobherefield = driver.find_element(By.XPATH, "//span[@class='nI-gNb-sb__placeholder']")
jobherefield.click()
enterkeyword = driver.find_element(By.XPATH, "//input[@placeholder='Enter keyword / designation / companies']")
enterkeyword.send_keys("Type your Keyword") # Type the keywords
locationfield = driver.find_element(By.XPATH, "//input[@placeholder='Enter location']")
locationfield.send_keys("Type your Location") # Type your location preferrence
searchbutton= driver.find_element(By.XPATH, "//button[@class='nI-gNb-sb__icon-wrapper']")
searchbutton.click()
time.sleep(10)
def apply_to_jobs_on_current_page():
    number_of_jobs = driver.find_elements(By.XPATH, "//div[@class='srp-jobtuple-wrapper']")
    print(f"Found {len(number_of_jobs)} jobs on the current page")

    for index, job in enumerate(number_of_jobs):
        job.find_element(By.XPATH, "div").click()
        time.sleep(5)

        window_opened = driver.window_handles
        if len(window_opened) > 1:
            driver.switch_to.window(window_opened[1])
            try:
                find_button = driver.find_element(By.XPATH, "//div[@class='styles_jhc__apply-button-container__5Bqnb']//button[@id='apply-button']")
                find_button.click()
                time.sleep(2)
                print(f"Applied to job {index + 1}")
            except NoSuchElementException:
                print("Apply button not found.")
            finally:
                driver.close()
                driver.switch_to.window(window_opened[0])
        else:
            print("No new window opened.")

apply_to_jobs_on_current_page()

pagination = driver.find_elements(By.XPATH, "//div[@class='styles_pages__v1rAK']/a")
print(len(pagination))

pagination_number = 2

while True:

    current_selected = driver.find_element(By.XPATH, "//div[@class='styles_pages__v1rAK']/a[@class='styles_selected__j3uvq']")

    for pagination_link in pagination:
        if pagination_link.text == str(pagination_number) and pagination_link != current_selected:
            pagination_link.click()
            time.sleep(5)
            break

    pagination = driver.find_elements(By.XPATH, "//div[@class='styles_pages__v1rAK']/a")

    if pagination_number > len(pagination):
        print("Reached the last page.")
        break

    apply_to_jobs_on_current_page()
    pagination_number += 1

print("Finished processing jobs.")