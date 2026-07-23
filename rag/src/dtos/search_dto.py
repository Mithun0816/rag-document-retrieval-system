from pydantic import BaseModel, Field

class SearchDTO(BaseModel):
    content : str
    top_k:int
