# Django IMDB
**RESTful movie API made with Python &amp; Django**

A RESTful movie API with custom actions, token implementation
and authorization.

There are three different roles in this API:
* Admin
* User
* Anonymous

Each role has different restrictions.

## API Endpoints ##

> Read the documentation -
**/docs**

https://djimdb.herokuapp.com/docs/

> Get authorization -
**/auth**

The API service will respond with a token, if the payload sent is valid.

_Payload_
```
{
    username:
    password:
}
```

> Movie List - (Need authorization)
**/movies**

_You first need to authorize yourself with a valid header payload._

_Payload_
```
{
    Authorization: Token XXX
}
```


> Ratings List - (Need authorization)
**/ratings**

_You first need to authorize yourself with a valid header payload._

_Payload_
```
{
    Authorization: Token XXX
}
```

> User List - (Need authorization)
**/users**

_You first need to authorize yourself with a valid header payload._

_Payload_
```
{
    Authorization: Token XXX
}
```