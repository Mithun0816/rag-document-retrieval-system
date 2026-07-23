from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, text
from sqlalchemy.dialects.postgresql import UUID 
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

from database.base import Base



class KnowledgeBase(Base):
    __tablename__="knowledge_base_3481"
    kb_id = Column(String, server_default=text("gen_random_uuid()"), unique=True, index=True, primary_key=True)
    content_chunk=Column(String,nullable=False)
    chunk_embedding=Column(Vector,nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    created_by = Column(String, default="SYSTEM", nullable=False)
    modified_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    modified_by = Column(String, default="SYSTEM", nullable=False)