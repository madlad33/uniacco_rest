# UniAcco REST API
- Endpoint 1: https://uniacco-rest.herokuapp.com/create/ to create new users.
- Endpoint 2: https://uniacco-rest.herokuapp.com/token/ to generate JWT token after authentication.
- Endpoint 3: https://uniacco-rest.herokuapp.com/accounts/login/ to signup using Google OAuth2.0 from server side.
- Login to admin panel to see history of the ip addresses in UserLoginHistory model.
- Select the respective records and choose the action "export" to export the records in csv format.
- Every time an user authenticates a POST request is made to the url  https://encrusxqoan0b.x.pipedream.net/ with JSON data of body: Body: {“user”: user_id, “ip”: ip_address}