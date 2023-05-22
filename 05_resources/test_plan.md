Log In Page Tests

|  Email Address  |  Password  | Expected result                                |
---------------------------------------------------------------------------------
| Signed up       | Valid      | Log in, moved to Logged In Page                |
| Signed up       | Invalid    | Failed log in                                  |
| Signed up       | Blank      | Passwrod must be specified                     |
| Unknown         | Valid      | Failed log in                                  |
| Unknown         | Invalid    | Failed log in                                  |
| Unknown         | Blank      | Password must be specified                     |
| Blank           | Valid      | Email address must be specified                |
| Blank           | Invalid    | Email address must be specified                |
| Blank           | Blank      | Email address and password muver be specified  |

Sign Up Page Tests

|  Email Address  |  Password  | Expected result                                |
---------------------------------------------------------------------------------
| Unknown         | Valid      | Signed up, return to Log In Page               |
| Unknown         | Invalid    | Failed sign up                                 |
| Unknown         | Blank      | Password must be specified                     |
| Known           | Valid      | Failed sign up                                 |
| Known           | Invalid    | Failed sign up                                 |
| Known           | Blank      | Password must be specified                     |
| Blank           | Valid      | Email address must be specified                |
| Blank           | Invalid    | Email address must be specified                |
| Blank           | Blank      | Email address and password muver be specified  |

Logged In Page tests
|  Action         |  Axpected result                     |
----------------------------------------------------------
|  Click Log Out  | Logged out, returned to Log In Page  |
