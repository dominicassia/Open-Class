import time
from selenium import webdriver

def main():

    ''' The goal of this program is to open class at a specific time '''

    url = 'https://us.bbcollab.com/collab/ui/session/guest/c46033437acc4436a8a9b106accdd2a1'

    driver_path = 'C:\\Users\\Domin\\Github\\Python\\open-class\\Driver\\chromedriver.exe'

    try:

        with webdriver.Chrome(driver_path) as driver:

            driver.get(url)

    finally:

        driver.close()

        


# Call main
main()