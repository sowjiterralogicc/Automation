*** Settings ***
Library      SeleniumLibrary
Library      Collections

#*** Variables ***
#${Youtube_URL} https://www.youtube.com/@RajiRaji-nd4sg
#${Browser} chrome

*** Test Cases ***
Lanch The YouTube Browser
     Open Browser      https://www.youtube.com/@RajiRaji-nd4sg    Chrome
     Maximize Browser Window
     Click Element      xpath:(//yt-button-shape[.='Sign in'])[1]
     Sleep     5s
     Input Text        id:identifierId          sowjanya.n@terralogic.com
     Click Element       xpath://span[.='Next']
     Sleep     5s
     Input Text          name:Passwd          Ammu1998@17
     Click Element       xpath://span[.='Next']
     Sleep       15s

     Wait Until Element Is Visible       xpath://div[@id='subscribe-button']//yt-smartimation/yt-button-shape/button      timeout=10
     Click Element       xpath://div[@id='subscribe-button']//yt-smartimation/yt-button-shape/button

     ${channel_name}=      Get Text       xpath://div[@id='meta']//div[@id='text-container']
     Log To Console      ${\n}Name of the Channel: ${channel_name}

     ${links}=    Get All Links
     ${links_count}=      Get Length     ${links}
     Log To Console     ${\n}Total Links in the URL: ${links_count}

     ${all_elements}=     Get Webelements     xpath://*
     ${elements_count}=      Get Length      ${all_elements}
     Log To Console      ${\n}Total Elements in the URL: ${elements_count}
     sleep      5s
     Click ELement       xpath://span[@id="video-title"]
     sleep     5s
     Click ELement      xpath:(//div[@class="yt-spec-touch-feedback-shape__fill"])[21]
     sleep     10s
     #${all_elements}=       Get Webelements       xpath:(//span[@class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap yt-core-attributed-string--text-alignment-center yt-core-attributed-string--word-wrapping"])[1]
     ${num_likes}=      Get Text    xpath:(//span[@class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap yt-core-attributed-string--text-alignment-center yt-core-attributed-string--word-wrapping"])[1]
     Log To Console      ${\n}Total likes: ${num_likes}