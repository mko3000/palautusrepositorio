*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register User  batman  robin123  robin123
    Submit Registeration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register User  ck  kryptonite123  kryptonite123
    Submit Registeration
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Register User  superman  loislane  loislane
    Submit Registeration
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Register User  wonderwoman  amazon123  amazon321
    Submit Registeration
    Register Should Fail With Message  Password confirmation didn't match password

Login After Successful Registration
    Register User  aquaman  atlantis123  atlantis123
    Submit Registeration
    Go To Login Page
    Set Username  aquaman
    Set Password  atlantis123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Register User  flash  speed  speed
    Submit Registeration
    Go To Login Page
    Set Username  flash
    Set Password  speed
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

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

Register User
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password_confirmation}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login


    