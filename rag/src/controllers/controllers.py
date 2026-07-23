from typing import Optional
from uuid import UUID
from datetime import datetime

from fastapi.responses import JSONResponse
from sqlalchemy import Date
from services.services import KnowledgeBaseService, SearchService
from dtos.custom_exception_dto import CustomAppException
from errors.error_codes import ErrorCode, ErrorCodeStatus
from constants.http_status import HttpStatusCode
from dtos.api_response_dto import APIResponse


class KnowledgeBaseController:

    def __init__(self):
        self.service = KnowledgeBaseService()

    async def knowledge_base_controller(
        self,
        content:str
    ) -> APIResponse:
        try:
            data= await self.service.knowledge_base_service(
                content=content
            )
            return APIResponse(
                data=data,
                code=HttpStatusCode.CREATED
            )
        except CustomAppException:
            raise
        except Exception as e:
            raise CustomAppException(
                message=f"create enrollment controller error: {str(e)}",
                code=ErrorCode.INTERNAL_SERVER_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
                
            )


class SearchController:
    def __init__(self):
        self.service = SearchService()
    async def search_controller(
        self,
        content:str,
        top_k:int
    ) -> APIResponse:
        try:
            data= await self.service.searching_service(
                content=content,
                top_k=top_k
            )
            return APIResponse(data=data,
                               code=HttpStatusCode.OK) 
        except CustomAppException:
            raise
        except Exception as e:
            raise CustomAppException(
                message=f"search controller error: {str(e)}",
                code=ErrorCode.INTERNAL_SERVER_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
                
            )