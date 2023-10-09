***Settings***
Library       SeleniumLibrary

*** Test Cases ***
TestAmazonLogin
    Open Browser    https://wynk.in/music    chrome
    Maximize Browser Window
LoginTowynk
    sleep      2s
    Click Element       xpath://div[text()='Login']
    sleep      2s
    Input Text         xpath://input[@data-testid="loginInputNumber"]             6309479867
    sleep      2s
    Click Element      xpath://button[@data-testid="loginSendOtpButton"]
    Sleep      10s
    Click Element        xpath:(//span[@class="w-6 h-6 dark:text-white"])[2]
soundquality
    sleep     5s
    Click Element        xpath://span[text()='Sound Quality']
    sleep     2s
    Page Should Contain Element              xpath://div[text()='Sound Quality']
    sleep       2s
    Log To Console           Qualitycheck
    sleep       2s
    Click Element         xpath:(//li[@class="sound-quality-modal_soundQuality__item__rsRrU cursor-pointer dark:hover:bg-wynk-dark-background hover:bg-wynk-light-background dark:bg-transparent bg-wynk-gray3"])[2]
playsongs
    sleep    2s
    Click Element       xpath://div[text()='Telugammayi']
    sleep     2s
    Click Element       xpath://span[text()='Play Now']
    sleep     2s
    Click ELement      xpath://span[text()='Wynk Music']
    sleep     5s
    FOR    ${i}    IN RANGE    0    6500    50
        Execute JavaScript    window.scrollTo(0, ${i})
        Sleep    1s    # Add a short pause between scrolls
    END
recentlyplayed
    sleep     10s
    Wait Until Element Is Visible    xpath://a[@title="Recently Played"]/div/span/span    timeout=10
    Click Element    xpath://a[@title="Recently Played"]/div/span/span
    sleep      10s
    Log To Console         shown recently played list successfully















































#import time
#
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#import time
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
#driver=webdriver.Chrome(r"C:\Users\Sowjanya N-3147\Downloads\chromedriver_win32 (1)\chromedriver")
#driver.get('https://wynk.in/music')
#driver.maximize_window()
#
#def wynk_login():
#    try:
#        driver.find_element_by_xpath("//span[@class='hover:opacity-60 cursor-pointer flex ']").click()
#        time.sleep(2)
#        ele=driver.find_element_by_xpath("//input[@placeholder='Enter Mobile Number']").send_keys("**********")
#
#        driver.find_element_by_xpath("//button[@type='submit']").click()
#        time.sleep(20)
#        driver.find_element_by_xpath("//button[@data-testid='loginVerifyOtpButton']").click()
#        time.sleep(2)
#        print("Wynk website login successful.. !!!!")
#    except:
#        print("login fail..")
#
#
#def search_telugu_songs():
#
#    driver.find_element_by_xpath("//input[@type='search']").click()
#    driver.implicitly_wait(5)
#    ac=ActionChains(driver)
#    time.sleep(4)
#    ac.send_keys("telugu").send_keys(Keys.ENTER).perform()
#    time.sleep(2)
#
#    driver.find_element_by_xpath("//div[@class='scroll-width-none scroll-smooth zapSearch_zapSearchTabMenu__EHwWs']/button[2]").click()
#    time.sleep(2)
#
#def letter_with_r():
#    actions = driver.find_element_by_xpath("//body")
#    for i in range(1000):
#        actions.send_keys(Keys.SPACE)
#    loadMoreButton = driver.find_element_by_xpath("//div[@class='inset-0 h-screen overflow-y-auto fixed bg-white dark:bg-wynk-dark-background pt-[3.70rem] sm:pt-[4.45rem]']")
#
#    total_songs=driver.find_elements_by_xpath("//div[@class='flex justify-between items-center']")
#    print("Total all telugu songs: ",len(total_songs))
#
#    c=0
#    for i in total_songs:
#        a=i.text
#        s=a.splitlines()[0]
#        if s.startswith("R"):
#            c=c+1
#            print(s)
#    print("Total songs starting with 'R':",c)
#
#wynk_login()
#search_telugu_songs()
#letter_with_r()
