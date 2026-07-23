from fastapi import APIRouter, Query, Body, Depends
from fastapi.responses import JSONResponse
from uuid import UUID
from dtos.api_response_dto import APIResponse
from dtos.knowledge_base_dto import KnowledgeBaseDTO
from controllers.controllers import KnowledgeBaseController, SearchController
from dtos.custom_exception_dto import CustomAppException
from dtos.search_dto import SearchDTO
from errors.error_codes import ErrorCode, ErrorCodeStatus
from constants.http_status import HttpStatusCode

router = APIRouter(prefix="/api", tags=["KnowledgeBase"])

def get_controller():
    return KnowledgeBaseController()

@router.post("/kb")
async def knowedge_base_router(
    request: KnowledgeBaseDTO = Body(...)
):
    try:
        controller = KnowledgeBaseController()
        result = await controller.knowledge_base_controller(
            content=request.content
        )
        return JSONResponse(
            content=result.to_dict(),
            status_code=HttpStatusCode.CREATED
        )
    except CustomAppException:
        raise
    except Exception as e:
        raise CustomAppException(
            message=f"Router error creating knowledge base: {str(e)}",
            code=ErrorCode.INTERNAL_SERVER_ERROR,
            status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
            error_code_id=ErrorCodeStatus[ErrorCode.INTERNAL_SERVER_ERROR]
        )



@router.post("/search")
async def search_router(
    request: SearchDTO= Body(...)
):
    try:
        controller = SearchController()
        result = await controller.search_controller(
            
            content=request.content,
            top_k=request.top_k
            
        )
        return JSONResponse(
            content=result,
            status_code=HttpStatusCode.OK
        )
    except CustomAppException:
        raise
    except Exception as e:
        raise CustomAppException(
            message=f"Router error on searching: {str(e)}",
            code=ErrorCode.INTERNAL_SERVER_ERROR,
            status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
            error_code_id=ErrorCodeStatus[ErrorCode.INTERNAL_SERVER_ERROR]
        )