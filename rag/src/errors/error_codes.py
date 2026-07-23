
# errors/error_codes.py
from enum import Enum

class ErrorCode(str, Enum):
    DATABASE_ERROR = "DatabaseErrorErrorCode"
    INTERNAL_SERVER_ERROR = "InternalServerErrorCode"
    USER_NOT_FOUND = "UserNotFoundErrorCode"
    VALIDATION_ERROR = "ValidationErrorCode"
    # ✅ Add this:
    DATA_DUPLICATE = "DuplicateDataErrorCode"

# If you use a dict mapping to numeric IDs / app-specific IDs
ErrorCodeStatus = {
    ErrorCode.DATABASE_ERROR: 50001,
    ErrorCode.INTERNAL_SERVER_ERROR: 50000,
    ErrorCode.USER_NOT_FOUND: 40401,
    ErrorCode.VALIDATION_ERROR: 40001,
    # ✅ Add a mapping for your new code:
    ErrorCode.DATA_DUPLICATE: 40901,
}
