***Settings***
Library       SeleniumLibrary

*** Test Cases ***
Testsocialmedia
    Open Browser    https://twitter.com/?logout=1696439921626    chrome
    Maximize Browser Window
    sleep      5s
signin
    Click Element        xpath://span[text()="Sign in"]
    ${handles} =    Get Window Handles
    Switch Window    ${handles}[0]
    sleep      5s
    Input Text    xpath://input[@autocomplete="username"]       sowji.nandyala36@gmail.com
    sleep     5s
    Click Element       xpath://span[.="Next"]/span
    sleep     5s
    Input Text        xpath://input[@data-testid="ocfEnterTextTextInput"]         NandyalaSo38377
    Sleep     2s
    Click Element      xpath://span//span[text()='Next']
    sleep     5s
    #Input Text      xpath://input[@autocomplete="current-password"]          Ammu1998@17
    Input Text     xpath://input[@name="password"]         Sowji1998@26
    sleep     5s
    Click Element       xpath://div[@data-testid="LoginForm_Login_Button"]
    #Click Element       xpath://span[text()='Log in']
    sleep     10s
profileupdation
    Click Element      xpath://span[text()='Profile']
    Sleep     5s
    Click Element      xpath://span//span[text()='Edit profile']
    sleep     2s
    ${handles} =    Get Window Handles
    Switch Window    ${handles}[0]
    ${update_profile}=         Input Text        xpath://div//input[@name="location"]         10,parappana agrahara main road
    sleep    2s
    Click Element      xpath://span//span[text()='Save']
    sleep    10s
    ${upated_profile}=        Page Should Contain Element               //div//span[@data-testid="UserLocation"]
    Log To Console           updated successfully

#    Run Keyword If       ${upated_profile} == 'True'     Log To Console    updated successfully     ELSE     Log To Console    Not updated




