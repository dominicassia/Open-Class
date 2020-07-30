import time
from selenium import webdriver

def main():

    ''' The goal of this program is to open class at a specific time '''

    url = 'https://us.bbcollab.com/collab/ui/session/guest/c46033437acc4436a8a9b106accdd2a1'

    driver_path = 'C:\\Users\\Domin\\Github\\Python\\open-class\\Driver\\chromedriver.exe'

    print(time.localtime())

    with webdriver.Chrome(driver_path) as driver:

        # Go to the webpage
        driver.get(url)

        driver.maximize_window()

        # Take the time
        takeTime = time.localtime()

        h = takeTime[3]
        m = takeTime[4]
        s = takeTime[5] 

        print('\n> Current time:\t', h, ':', m, ':', s, '\n')

        





        #     if 

        #     # Enter a guest name
        #     element = driver.find_element_by_id('guest-name')

        #     element.send_keys('Dom A', Keys.Enter)

        #     # Sleep until 11:50am
        #     time.sleep(8700)



        


# Call main
if __name__ == "__main__":
    main()