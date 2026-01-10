# [DRAFT] API Endpoints
## TRAINS
GET api/v1/trains --> To search for trains from route A->route B
GET api/v1/trains/{train_id} -->To search for trains availability for a certain class

## BOOKINGS
POST api/v1/bookings/{train_id} --> To book a train for train_id
GET api/v1/bookings -->To get the list of booking for the user
GET api/v1/bookings/{booking_id} -->To describe a booking_id

## Login & SignUp
POST api/v1/login --> To login with username and password
POST api/v1/logout --> Logs out of the current session
POST api/v1/signup -->To sign up with userid and other information



