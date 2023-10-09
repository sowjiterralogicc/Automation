***Settings***
Library       SeleniumLibrary


*** Test Cases ***
searching_for_flight
    Open Browser    https://www.makemytrip.com/    chrome
    Maximize Browser Window
    sleep     5s
#signin
#    ${handles} =    Get Window Handles
#    Switch Window    ${handles}[0]
#    sleep    10s
#    Input Text      xpath://input[@id="username"]        6309479867
#    sleep     5s
#    Click ELement     xpath://span[text()='Continue']
#    sleep       20s

from_to_flight
     sleep     10s
     Click Element       Xpath://input[@id="fromCity"]
     sleep     5s
     Input Text          Xpath://input[@placeholder="From"]          Bengaluru, India
     Sleep      3
     Click Element       Xpath:(//p[@class="font14 appendBottom5 blackText"])[1]

     Click Element       Xpath://input[@id="toCity"]
     Input Text          Xpath://input[@placeholder="To"]          HYDERABAD
     Sleep     3
     Click Element       Xpath:(//p[@class="font14 appendBottom5 blackText"])[1]
     Click Element       Xpath:(//div[@class="dateInnerCell"])[10]
     Click Element       Xpath://a[text()='Search']
inside_make_my_trip
     ${hanldes}     Get Window Handles
     Switch Window       ${hanldes}[0]
     Wait Until Element Is Visible      Xpath://div[@class="commonOverlay "]/div/div/button     timeout=10s
     Sleep      5
     Click Element       Xpath://div[@class="commonOverlay "]/div/div/button
     Sleep     15s
     Click Element       Xpath:(//span[text()='View Prices'])[1]
     Click Element       Xpath:(//button[text()='Book Now'])[1]
     Sleep     5
     ${hanldes}     Get Window Handles
     Switch Window       ${hanldes}[1]
flight_details
     sleep     5s
     Execute JavaScript       window.scrollTo(0,2500)
     Sleep      5
     Click Element       Xpath://input[@name="cb_gst_info"]/..

     Execute JavaScript       window.scrollTo(0,1500)
     Sleep     3

     Click Element       Xpath:(//input[@type="radio"])[2]/..
     Execute JavaScript       window.scrollTo(0,1750)
     Sleep    5
     Click Element        Xpath://button[text()='+ ADD NEW ADULT']
     Click Element        Xpath://input[@placeholder="First & Middle Name"]
     Input Text          Xpath://input[@placeholder="First & Middle Name"]         sowjanya
     Press Keys          Xpath://input[@placeholder="First & Middle Name"]        TAB
     Input Text          Xpath://input[@placeholder="Last Name"]         N
     Click Element        Xpath:(//label)[5]
     Sleep     5
     Click Element            Xpath://input[@placeholder="Mobile No"]
     Sleep     3
     Input Text            Xpath://input[@placeholder="Mobile No"]         6309479867
     Sleep     3
     Click Element         Xpath://input[@placeholder="Email"]
     Sleep     3
     Input Text           Xpath://input[@placeholder="Email"]         sowji9937@gmail.com
     Sleep     3

     Execute JavaScript         window.scrollTo(0,2500)
     Sleep    10
     Double Click Element        Xpath://button[text()='Continue']
     Sleep     5
     Click Element         Xpath://button[text()='CONFIRM']
     Sleep     5
     Click Element         Xpath://button[text()='PROCEED']
     Sleep     5
     Execute JavaScript       window.scrollTo(0,2500)

     Click Element            Xpath://span[text()='Skip to add-ons']
     Sleep     5
     Execute JavaScript         window.scrollTo(0,2500)
     Click Element            Xpath://button[text()='Proceed to pay']
     Sleep    10
     ${final_price}=         Get Text             Xpath://div[@class="fare__summary__card append-bottom20 font14 makeFlex column"]
     Log To Console         ${final_price}

# Click Element Xpath://button[@class="lato-black button buttonPrimary extraPadBtn fontSize16 "]

    Sleep    10



































































#***Settings***
#Library       SeleniumLibrary
#
#*** Test Cases ***
#Testsocialmedia
#    Open Browser    https://www.expedia.com/    chrome
#    Maximize Browser Window
#    sleep      5s
#    Click Element       xpath://a//span[text()='Flights']
#    sleep      2s
#    Click Element       xpath://a//span[text()='One-way']
#    sleep      10s
#        #Wait Until Element Is Visible    xpath://div[@class="uitk-field has-floatedLabel-label has-icon"]/button[@aria-label="Leaving from"]    timeout=20s
#    Click Element    xpath://div[@class="uitk-field has-floatedLabel-label has-icon"]/button[@aria-label="Leaving from"]
#    sleep      5s
#    ${handles} =    Get Window Handles
#    Switch Window    ${handles}[0]
#    Log To Console        get into window
#    Wait Until Element Is Visible    xpath://input[@data-stid="origin_select-menu-input"]    timeout=10s
#    Input Text    xpath://input[@data-stid="origin_select-menu-input"]    Bangaluru
#    sleep     10s
#    # Click on the specific suggestion
#    Click Element    xpath://li//div//button[@aria-label="Bengaluru (BLR - Kempegowda Intl.) Near Bangalore Palace, Bengaluru, Karnataka, India"]
#    sleep     5s
#    Click Element     xpath://button[@aria-label="Going to"]
#    ${handles} =    Get Window Handles
#    Switch Window    ${handles}[0]
#    sleep     5s
#    Input Text    xpath://input[@data-stid="destination_select-menu-input"]    Kerala
#    sleep      10s
#    Click Element          xpath://li//div//button[@aria-label="Cochin (COK - Cochin Intl.) Near Kochi, Kerala, India"]
#    sleep      5s
#    Click Element       xpath://button[@data-stid="uitk-date-selector-input1-default"]
#    sleep       10s
#    Click ELement       xpath://div[@class="uitk-date-number uitk-date-number-today uitk-type-300 uitk-type-regular"]
#    sleep       5s
#    Click Element       xpath:(//div[@class="uitk-day-button uitk-day-selectable uitk-day-clickable"])[3]
#    sleep       5s
#    Click Element       xpath://button[@data-stid="apply-date-selector"]
#    sleep       5s
#    Click Element       xpath://button[@id="search_button"]
#    sleep       10s
#    Click Element       xpath://button[@stid="FLIGHTS_DETAILS_AND_FARES-index-1-leg-0-fsr-FlightsActionButton"]
#    sleep       5s
#    Click Element       xpath://button[@stid="select-button"]
#    sleep      5s
#    ${handles} =    Get Window Handles
#    Switch Window    ${handles}[0]
#    sleep      10s
#    Click Element      xpath://button[@data-stid="goto-checkout-button"]
#    sleep      5s
#    Click Element      xpath://select[@class="cko-field title-id-name gb-whitelist"]
#    sleep     2s
#    Select From List By Value       xpath://option[@value='3_Mrs.']
#    sleep     2s
#    Input Text        xpath://input[@id="firstname[0]"]        sow
#    sleep     2s
#    Input Text        xpath://input[@data-tealeaf-name="middleName"]       janya
#    sleep     2s
#    Input Text       xpath://input[@id="lastname[0]"]            Na
#    sleep     2s




#https://github.com/robotframework/SeleniumLibrary/issues/1857