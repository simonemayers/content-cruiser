from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
starting_url = 'https://canvas.stiegleredtech.org/'


driver.get(starting_url)

# Fill login information manually or automate this with extreme care for your credentials security
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

# Find the username field, clear it and enter the username
username_field = driver.find_element(By.ID, 'pseudonym_session_unique_id')
username_field.clear()
username_field.send_keys(username)

# Find the password field, clear it and enter the password
password_field = driver.find_element(By.ID, 'pseudonym_session_password')
password_field.clear()
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, '.Button.Button--login')
login_button.click()

# Wait 5 seconds for the page to load
driver.implicitly_wait(10)

next_page_exists = True
total_words = 0
previous_url = ""

while next_page_exists:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    user_content = soup.find_all(class_='user_content')


    if previous_url == driver.current_url:
        print("End of course reached")
        break

    #find elemt by class name
    discussion_section = driver.find_elements(By.CLASS_NAME, 'discussion-section')

    if discussion_section:
        print('skipping discussion section')
        print(f"Current url: {driver.current_url}")
    else:
        for content in user_content:
            words = content.get_text().split()
            total_words += len(words)
            print(f"Current total words count: {total_words}")
            print(f"Current url: {driver.current_url}")

    previous_url = driver.current_url

    try:
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-describedby="msf0-next-desc"]')))
        next_button.click()


    except:
        print("End of course reached")
        print(f"Current url: {driver.current_url}")
        next_page_exists = False

# driver.quit()


