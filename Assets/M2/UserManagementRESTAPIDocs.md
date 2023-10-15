# Retrieve authenticated user

Get the details corresponding to a particular user.

**URL** : `/eduser/<id>`

**Method** : `GET`

## On Success

**Code** : `200 OK`

**Body**
```json
{
    "user_token": string,
    "first_name": string,
    "last_name": "string,
    "phn": long,
    "dob": string
}
```

## On Failure

**Body**
```json
{
	"error_message": string
}
```
# Register user

Get the details corresponding to a particular user.

**URL** : `/eduser/`

**Method** : `POST`

**Payload**: 
```json
{
    "user_token": string,
    "first_name": string,
    "last_name": "string,
    "phn": long,
    "dob": string
}
```

## On Success

**Code** : `200 OK`

## On Failure

**Body**
```json
{
	"error_message": string
}
```
