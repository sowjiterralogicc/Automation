***Settings***
Library       SeleniumLibrary

*** Test Cases ***
TestAmazonLogin
    Open Browser    https://www.amazon.in/    chrome
    Maximize Browser Window
    Mouse Over       xpath://span[text()='Hello, sign in']
    Click Element    xpath://a[@rel='nofollow']/span
    Sleep            5s
    Input Text       xpath://input[@type='email']    ramesh345.reddy@gmail.com
    Sleep            2s
    Click Element     xpath://input[@class='a-button-input']
    sleep            2s
    Input Text       xpath://input[@type='password']     Ammu1998@17
    Click ELement     xpath://input[@id='signInSubmit']
Search_for_items
    sleep         2s
    Input Text        xpath://input[@name='field-keywords']      shoes for women sneakers
    Press Key        xpath://input[@name='field-keywords']  \\13  # \\13 represents the "Enter" key
    Sleep            2s
    ${before_click_handles}=    Get Window Handles
    sleep           5s
    Click ELement      xpath://*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[2]/div/span/a/div/img
    sleep           2s
    ${after_click_handles}=    Get Window Handles
    ${new_window_handle}=    Set Variable    ${after_click_handles}[1]
    Log To Console    The title of the new window is: ${new_window_handle}
    sleep       2s
    SeleniumLibrary.Switch Window    ${new_window_handle}
    sleep       5s
    Click Element     xpath://input[@id='add-to-cart-button']
    sleep       5s
    Click Element     xpath://input[@name='proceedToRetailCheckout']
Address_validation
    sleep       5s
    Wait Until Element Is Visible    xpath://input[@data-testid='Address_selectShipToThisAddress']    timeout=10s
    Scroll Element Into View    xpath://input[@data-testid='Address_selectShipToThisAddress']
    Click Element    xpath://input[@data-testid='Address_selectShipToThisAddress']
    sleep       5s
    Wait Until Element Is Visible    xpath://span//input[@name='ppw-widgetEvent:SetPaymentPlanSelectContinueEvent']    timeout=10s
    scroll element into view         xpath://span//input[@name='ppw-widgetEvent:SetPaymentPlanSelectContinueEvent']
    Click Element    xpath://span//input[@name='ppw-widgetEvent:SetPaymentPlanSelectContinueEvent']
    Wait Until Element Is Visible    xpath://input[@aria-labelledby="bottomSubmitOrderButtonId-announce"]    timeout=10s
    scroll element into view         xpath://input[@aria-labelledby="bottomSubmitOrderButtonId-announce"]
    Click Element    xpath://input[@aria-labelledby="bottomSubmitOrderButtonId-announce"]
    Sleep      10s
    # Validate whether the order was placed successfully
    ${order_placed}=    Page Should Contain Element    Order placed, thank you!
    Log To Console       Order placed, thank you!
#    Run Keyword If       ${order_placed} == 'True'     Log To Console    order placed successfully     ELSE     Log To Console    order failed


