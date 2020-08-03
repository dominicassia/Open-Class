import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def main():

    ''' The goal of this program is to open class at a specific time '''

    url = 'https://us.bbcollab.com/collab/ui/session/guest/c46033437acc4436a8a9b106accdd2a1'

    driver_path = 'C:\\Users\\Domin\\Github\\Python\\open-class\\Driver\\chromedriver.exe'

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

        if h == 8 and m > 20:

            sleepM =  ( 60 - m ) + 20
            sleepS = 60 - s

            print('\tSleep: ', sleepM, ' min ', sleepS, ' sec \n' )

            totalTime = ( 60 * sleepM )  + sleepS

            print('\tSec:', totalTime )

            time.sleep( totalTime )

        elif h == 9 and m < 20:
            
            sleepM =  20 - m 
            sleepS = 60 - s

            print('\tSleep: ', sleepM, ' min ', sleepS, ' sec \n' )

            totalTime = ( 60 * sleepM )  + sleepS

            print('\tSec:', totalTime )

            time.sleep( totalTime )

            if h < 9:
                
                sleepH =  9 - h 
                sleepM =  25 - m 
                sleepS = 60 - s

                # if m < 0:

                #     sleepH -= 1
                #     sleepM = -1 * ( m ) + 25

                print('\tSleep: ', sleepH, ' hrs ', sleepM, ' min ', sleepS, ' sec \n' )

                totalTime = ( 3600 * (sleepH)) + ( 60 * sleepM )  + sleepS

                print('\tSec:', totalTime )

                time.sleep( totalTime )

        # elif h > 9:

        #     exit()

        driver.refresh()

        try:
            element = driver.find_element_by_id('guest-name')

            element.send_keys('Dom A')
            element.send_keys(Keys.RETURN)

        except NoSuchElementException:

            print('Incorrect Element')

            try:
                element = driver.find_element_by_name('guestName')

                element.send_keys('Dom A')
                element.send_keys(Keys.RETURN)

            except NoSuchElementException:

                print('Incorrect Class')
            
        # Sleep until 11:50am
        time.sleep(9100)

        driver.close()
        exit()

# Call main
if __name__ == "__main__":
    main()