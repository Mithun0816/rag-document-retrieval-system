from typing import Any, Dict, List
from repositories.repo import KnowledgeBaseRepository
from dtos.custom_exception_dto import CustomAppException
from errors.error_codes import ErrorCode, ErrorCodeStatus
from constants.http_status import HttpStatusCode
from utility.utilities import Utility
from utility.utilities import UtilityAbstract
 
class KnowledgeBaseService:
    def __init__(self):
        self.repo = KnowledgeBaseRepository()
 
    async def knowledge_base_service(
        self,
        content:str
    ) -> Dict[str]:
        try:
            embed_model=UtilityAbstract()
            nodes=Utility.split_into_chunks(content, embed_model)
            print("after chunking")
            data=Utility.generate_embeddings(nodes,embed_model)
            print("after embedding")
            data = self.repo.create_kb(
                content=content,
                results=data
            )
            return {
                "content":data["content"]
            }
           
        except CustomAppException:
            raise
        except Exception as e:
            raise CustomAppException(
                message=f"Service error creating kb: {str(e)}",
                code=ErrorCode.INTERNAL_SERVER_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
                error_code_id=ErrorCodeStatus[ErrorCode.INTERNAL_SERVER_ERROR]
            )
 # services/search_service.py

class SearchService:
    def __init__(self):
        self.repo = KnowledgeBaseRepository()
       

    async def searching_service(self, content: str, top_k:int) -> Dict[str, Any]:
        try:
            embed_model = UtilityAbstract()
            query_embedding: List[float] = embed_model._get_text_embedding(content)
            rows = self.repo.search_similar(query_embedding=query_embedding, top_k=top_k)

            contexts = [r["content_chunk"] for r in rows]
            context_text = "\n\n---\n\n".join(contexts)

            prompt = f"""
                        Use ONLY the context to answer the question. If context is insufficient, say so briefly and answer conservatively.

                        Context:
                        {context_text}

                        Question:
                        {content}

                        Answer:
                        """.strip()

            answer_text: str = Utility.llm(prompt)
            return {
                "query": content,
                "answer": answer_text,
                "contexts": contexts,           
                "top_k": len(contexts),
            }

        except CustomAppException:
            raise
        except Exception as e:
            raise CustomAppException(
                message=f"searching conetnt service error: {str(e)}",
                code=ErrorCode.INTERNAL_SERVER_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
               
            )