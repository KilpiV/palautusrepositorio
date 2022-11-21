*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  heidi  salasana123
    Output Should Contain  User with username heidi already exists

Register With Too Short Username And Valid Password
    Input Credentials  e  salasana333
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  ville  sala1
    Output Should Contain  Password must be atleast 8 character long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  salasana
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  heidi  heidi123
    Input New Command