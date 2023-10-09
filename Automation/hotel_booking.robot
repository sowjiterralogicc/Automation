***Settings***
Library       SeleniumLibrary

*** Test Cases ***
Testhotel_booking
    Open Browser    https://www.oyorooms.com/    chrome
    Maximize Browser Window
entercity
    sleep      10s
    Input Text    xpath://div//form[@class="autoCompleteDesktop__searchContainer"]/input[@placeholder="Search by city, hotel, or neighborhood"]    Coorg
    sleep      5s
    Press Key     xpath://div//form[@class="autoCompleteDesktop__searchContainer"]/input[@placeholder="Search by city, hotel, or neighborhood"]    \\13
    sleep      5s
    Click Element       xpath://div[@class="oyo-row oyo-row--no-spacing datePickerDesktop datePickerDesktop--home"]
datepicker
    sleep     10s
    Click Element       xpath://td[@class="DateRangePicker__Date DateRangePicker__Date--is-selected DateRangePicker__Date--today DateRangePicker__Date--today--is-selected"]
    sleep      2s
    Click Element       xpath://td[@class="DateRangePicker__Date DateRangePicker__Date--weekend"]//span[text()='7']
    sleep     2s
    Click Element       xpath://div[@class="oyo-row oyo-row--no-spacing guestRoomPicker guestRoomPicker--home "]
    sleep      2s
    Click Element       xpath://button[text()='Add Room']
    sleep      2s
    Click Element       xpath://button[text()='Search']
selecthotel
    Sleep      5s
    Click Element       xpath://a//h3[@title="OYO Coorg Mandarin"]
    Sleep      2s
    ${after_click_handles}=    Get Window Handles
    ${new_window_handle}=    Set Variable    ${after_click_handles}[1]
    Log To Console    The title of the new window is: ${new_window_handle}
    sleep       2s
    SeleniumLibrary.Switch Window    ${new_window_handle}
    sleep      5s
    Wait Until Element Is Visible    xpath://button//span[text()='Continue to Book']    timeout=10s
    scroll element into view         xpath://button//span[text()='Continue to Book']
    Click Element       xpath://button//span[text()='Continue to Book']
detailsverification
    sleep     15s
    Input Text       xpath:(//input[@class="textInput__input"])[1]           Sowjanya
    sleep    2s
    Input Text       xpath:(//input[@class="textInput__input"])[2]           sowji9937@gmail.com
    sleep    2s
    Input Text       xpath://input[@aria-label="input"]                 6309479867
    sleep    2s
    Click Element      xpath://button//span[text()='Send passcode']
    sleep      10s
    ${element_found}=      Page Should Contain Element    xpath://span[text()='Payable Amount']
    Log To Console         Payment details confirmed successfully
    # Verify the result based on whether the element is found or not
#    Run Keyword If       ${element_found} == 'True'     Log To Console    Payment details page verified successfully     ELSE     Log To Console    Payment details page not verified





