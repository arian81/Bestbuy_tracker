from selenium import webdriver
from time import sleep
from pushover import Client
from selenium.webdriver.chrome.options import Options


def send_available_notif(message):
    client = Client("Enter Client ID", api_token="Enter Token ID") #Go to pushover.com to create and account and get the credintials
    client.send_message(message, title="Item Available. Buy Now!!!!!")


def in_stock(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.BinaryLocation = "/usr/bin/chromium-browser"
    driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome(driver_path="/usr/bin/chromedriver")
    driver.get(url)
    time_out_counter = 0
    while True:
        sleep(10)
        availability = driver.find_elements_by_class_name("availabilityMessage_1MO75")
        try:
            online_availability = availability[0].text
            physical_availability = availability[1].text
            print(physical_availability)
            if physical_availability == "Available for free store pickup":
                # send_available_notif("Item is available in some store. Check it out. \n https://bit.ly/2Vixbll")
                print("Item is available in some store. Check it out. \n https://bit.ly/2Vixbll")
                while True:
                    try:
                        locations = driver.find_elements_by_class_name("col-xs-7_2wdRy")
                        availability = driver.find_elements_by_class_name("col-xs-5_13fKW.clearFloat_3JGAC")
                        for i in range(3):
                            if availability[i].text == "Pick Up Here":
                                # send_available_notif("It's available in richmond hill store go get it")
                                print(f"It's available in {locations[i].text} store go get it")
                                driver.close()
                                exit()
                        print("Not available anywhere nearby yet.")
                        driver.refresh()
                        sleep(60)
                    except IndexError:
                        print(f"Timed out {time_out_counter} times. Trying again.")
        except IndexError:
            print(f"Timed out {time_out_counter} times. Trying again.")
        driver.refresh()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        usr_input = ("Enter the URL to the product page         >>  ")
        in_stock(usr_input)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
