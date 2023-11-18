*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  batman  robin123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  nalle123
    Output Should Contain  User with username already exists
    
Register With Too Short Username And Valid Password
    Input Credentials  ck  kryptonite123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  132E124  sala1234
    Output Should Contain  Username can contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  batman  robin12
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  batman  clarkkent
    Output Should Contain  Password can't contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command