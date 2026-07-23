## DESCRIPTION
This api fetches the data from the knowledge base according to the user query

## HTTP METHOD
POST

## API ENDPOINT
api/search

## REQUEST HEADERS
```json
{
    "Content-Type": "application/json",
}
```

## REQUEST PAYLOAD
```json
{
    "user_query":"How to gain muscles? What service to choose?"
}
```

## SUCCESS RESPONSE
```json
{
    "data":{
        
            
                {
                    "result":"There is service called muscle gaining package for 3 months and on doing it you can gain the muscles . if you want i will provide you the package details."

                }
            
        
    },
    "request_id": "d5a25895-0160-4ff1-96f1-bbc53c0e3253",
    "timestamp": "d5a25895-0160-4ff1-96f1-bbc53c0e3253",
    "message":"answer for the query fetched successfully",
    "errors":[],
    "status_code":201,
}

```



## ERROR RESPONSE
```json
{
    "data":{},
    "request_id":"d5a25895-0160-4ff1-96f1-bbc53c0e3253",
    "timestamp":"d5a25895-0160-4ff1-96f1-bbc53c0e3253",
    "message":"The request of gym consultation service faied",
    "errors":["Internet traffic error","Unexpected error found","Service not available try after some time"],
    "status_code":400
}

