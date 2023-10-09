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















































