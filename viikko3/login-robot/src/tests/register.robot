*** Settings ***
Resource  resource.robot


*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Create User  kalle  kalle123
    Output Should Contain  User with username already exists

Register With Too Short Username And Valid Password
    Create User  ka  kalle123
    Output Should Contain  Username should be contain only letters and be at least 3 characters long


Register With Valid Username And Too Short Password
    Create User  kalle  kalle12
    Output Should Contain  Password needs to have special character and be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User  kalle  kallekal
    Output Should Contain  Password needs to have special character and be at least 8 characters long
