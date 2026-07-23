# repository/repo.py
from sqlalchemy.orm import Session
from sqlalchemy import select, text
from models.models import KnowledgeBase
from dtos.custom_exception_dto import CustomAppException
from errors.error_codes import ErrorCode, ErrorCodeStatus
from constants.http_status import HttpStatusCode
from database.database import Database


class KnowledgeBaseRepository:
    def __init__(self):
        self.db_instance = Database()
        
    def create_kb(self, content: str, results: list) -> dict:
        try:
           
            with self.db_instance.SessionLocal() as db_session:
                with db_session.begin():  
                    for text, embedding in results:
                        node = KnowledgeBase(
                            content_chunk=text,
                            chunk_embedding=embedding
                        )
                        db_session.add(node)

            return {"content": "The KB creation was successful. Check the database"}

        except CustomAppException:
            raise
        except Exception as e:
            raise CustomAppException(
                message=f"Database error creating kb: {str(e)}",
                code=ErrorCode.DATABASE_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
                error_code_id=ErrorCodeStatus[ErrorCode.DATABASE_ERROR],
            )

    def search_similar(self, query_embedding: list[float], top_k: int = 3) -> list[dict]:
        try:
            with self.db_instance.SessionLocal() as db:
                table = KnowledgeBase.__table__.name
                sql = text(f"""
                    
                SELECT
            kb_id AS id,
            content_chunk AS content,
        chunk_embedding <=> (:query)::vector AS distance
        FROM {table}
        ORDER BY distance ASC
        LIMIT :top_k

                """)
                rows = db.execute(sql, {"query": query_embedding, "top_k": int(top_k)}).fetchall()

                out = []
                for row in rows:
                    m = row._mapping
                    out.append({
                        "kb_id": m["id"],
                        "content_chunk": m["content"],
                        "distance": float(m["distance"]),
                    })
                return out
        
        except CustomAppException:
            raise
        except Exception as e:
            raise CustomAppException(
                message=f"Database error on retrieval: {str(e)}",
                code=ErrorCode.DATABASE_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
                error_code_id=ErrorCodeStatus[ErrorCode.DATABASE_ERROR],
            )
