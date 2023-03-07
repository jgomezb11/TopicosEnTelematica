from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProductExistRequest(_message.Message):
    __slots__ = ["name_product"]
    NAME_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    name_product: str
    def __init__(self, name_product: _Optional[str] = ...) -> None: ...

class ProductExistResponse(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    def __init__(self, product_id: _Optional[int] = ...) -> None: ...
