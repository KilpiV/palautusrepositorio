*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  v
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  sal123
    Set Password Confirmation  sal123
    Submit Credentials
    Register Should Fail With Message  Too short password
    
Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  salasana123
    Set Password Confirmation  salisana123
    Submit Credentials
    Register Should Fail With Message  Wrong password confirmation

Login After Successful Registration
    Set Username  ville
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Go To Login Page And Test New User

Login After Failed Registration
    Set Username  peetu
    Set Password  sal123
    Set Password Confirmation  sali123
    Submit Credentials
    Go To Login Page And Fail To Test New User    

*** Keywords ***
Go To Login Page And Fail To Test New User
    Go To Login Page
    Set Username  peetu
    Set Password  sal123
    Click Button  Login
    Login Page Should Be Open

Go To Login Page And Test New User
    Go To Login Page
    Set Username  ville
    Set Password  salasana123
    Click Button  Login
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  heidi  heina111
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed
    Registered Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}
    
Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
    
Submit Credentials
    Click Button  Register