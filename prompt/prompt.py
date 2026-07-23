import boto3
import json

class BedrockEmailGenerator:
    

    def __init__ (self, model_id, region_name,aws_access_key_id, aws_secret_access_key):
        self.model_id = model_id
        self.region_name = region_name
        self.bedrock_runtime = boto3.client(
        service_name='bedrock-runtime',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        )

        self.system_prompt = self.get_system_prompt()

    def get_system_prompt(self):

        return """
            <role> You are an intelligent AI academic notes assistant designed to help students understand the study materials effectively.
    You act as knowledgeable tutor who explains concepts clearly simplifies complex topics and supports learning with structured responses
</role>

<objective>
to analyze the user provided documents of notes or the question asked by the user and generate accurate, clear and well structured explanations , summaries and key points or answers
that answers that enhance the student understanding and learning
</objective>

<instructions>
1. Read the user's query carefully and if they provide name respond with their name 
2. Identify the requested scenario ( explanation, sumamry, key points and question & answers)
3. If the user uploaded the notes use that as a primary source of data
4. Explain the  requested concepts in a simple language with the examples  and also include the user name who uploaded that notes and what notes you are using to provide the answers
5. Highlight the important terms and definitions of the requested topics
6.If needed provide the examples to explain the concepts 
7. Keep the response informative
8. Maintain clarity and structure as heading -> content from the notes provided -> extra examples to understand
</instructions>

<constraints>
1. Do not generate information irrelevant to the topics
2. If the irrelevant question asked send response as " It is a irrelevant topic "
3. Avoid assumptions and fabricated facts
4. Keep explanations student friendly
5. Avoid overly technical jargons unless requested
</constraints>


"""
    def fixed_size_chunking(self,text,chunk_size=100,overlap=20):
        chunks=[]
        start=0
        while start<len(text):
            end=start+chunk_size
            chunk=text[start:end]
            chunks.append(chunk)
            start=end-overlap
        
        return chunks
    
    def send_answer(self,user_query,max_tokens=1000,temperature=0.7):

        chunks=self.fixed_size_chunking(user_query,chunk_size=100,overlap=20)
        final_output=[]

        for chunk in chunks:

            request_body={
                "messages" :[
                    {
                        "role":"user",
                        "content":[
                            {"text":user_query}
                        ]
                    }
                ],
                "system":[
                    {"text":self.system_prompt}
                ],
                "inferenceConfig":{
                    "max_new_tokens":max_tokens,
                    "temperature":temperature
                }
            }
            try:

                response=self.bedrock_runtime.invoke_model (
                modelId=self.model_id,
                body=json.dumps(request_body),
                contentType='application/json',
                accept='application/json'
            )

                response_body=json.loads(response['body'].read())
                text= response_body['output']['message']['content'][0]['text']
                final_output.append(text)
            except Exception as e:
                return f"error generating the explanation : {str(e)}"
        return "\n".join(final_output)


if __name__=="__main__":
    # Credentials passed directly
import os

aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")

    generator = BedrockEmailGenerator(
    model_id=model_id,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key



    )

    user_query = "Give me a detailed explanation of Java recursion"
    content = generator.send_answer(user_query)
    print(content)
