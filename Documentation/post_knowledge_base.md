## DESCRIPTION
This api adds the content as chunks in the knowlege base 

## HTTP METHOD
POST

## API ENDPOINT
api/knowledge_base

## REQUEST HEADERS
```json
{
    "Content-Type": "application/json",
}
```

## REQUEST PAYLOAD
```json
{
    "content":"""gym consultation system service
The gym consultation system service is a crucial component of the gym membership process. It helps ensure that all members receive the same level of care and attention, regardless of whether they are new or returning members. The consultation system service includes:
Health Assessments: Assessments to evaluate the member's health status and fitness level.
Personalized Training Plans: Tailored plans based on the member's specific fitness goals and health background.
Regular Check-Ins: Ongoing evaluations to track progress and make necessary adjustments to the training plan.
Communication: Regular communication with the personal trainer to discuss progress and any changes in the training plan.
Safety and Compliance: Ensuring that the training plan is safe and compliant with the member's health and fitness goals.
This service is essential for building trust and ensuring that members receive the best possible training experience."""
    
}
```

## SUCCESS RESPONSE
```json
{
    "data":{
        "gym_kb_details":
        {
            
                {
                    "kb_id":"49895305054",
                    "content_chunk":"gym consultation system service
The gym consultation system service is a crucial component of the gym membership process.",
                    "chunk_embeddings":[0.89, -0.12,0.82,0.7687],

                },

                {
                    "kb_id":"49895305055",
                    "content_chunk":"It helps ensure that all members receive the same level of care and attention, regardless of whether they are new or returning members.",
                    "chunk_embeddings":[0.99, -0.2,0.2,0.7687],

                },

                {
                    "kb_id":"49895305056",
                    "content_chunk":"whether they are new or returning members. The consultation system service includes:
                    Health Assessments: Assessments to evaluate the member's health status and fitness level.",
                    "chunk_embeddings":[0.19, -0.1,0.768,0.7687],

                },

                {
                    "kb_id":"49895305057",
                    "content_chunk":"This service is essential for building trust and ensuring that members receive the best possible training experience.",
                    "chunk_embeddings":[0.49, -0.124,0.382,0.37687],

                }

            
        }
    },
    "request_id": "d5a25895-0160-4ff1-96f1-bbc53c0e3253",
    "timestamp": "d5a25895-0160-4ff1-96f1-bbc53c0e3253",
    "message":"the content chunks added in knowledge base  successfully",
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


```