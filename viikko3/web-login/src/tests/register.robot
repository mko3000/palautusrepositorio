*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  batman
    Set Password  robin123
    Set Password Confirmation  robin123
    Submit Registeration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ck
    Set Password  kryptonite123
    Set Password Confirmation  kryptonite123
    Submit Registeration
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  superman
    Set Password  loislane
    Set Password Confirmation  loislane
    Submit Registeration
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  wonderwoman
    Set Password  amazon123
    Set Password Confirmation  amazon321
    Submit Registeration
    Register Should Fail With Message  Password confirmation didn't match password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registeration
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}


    