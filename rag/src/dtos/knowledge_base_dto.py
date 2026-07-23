from pydantic import BaseModel, Field, field_validator

class KnowledgeBaseDTO(BaseModel):
    content : str
    
