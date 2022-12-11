from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "title", "year"]
    class GenreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    DRAMA: Book.GenreType
    GENRE_FIELD_NUMBER: _ClassVar[int]
    HORROR: Book.GenreType
    ISBN: int
    ISBN_FIELD_NUMBER: _ClassVar[int]
    THRILLER: Book.GenreType
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.GenreType
    title: str
    year: int
    def __init__(self, ISBN: _Optional[int] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.GenreType, str]] = ..., year: _Optional[int] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: Book
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["statusCode"]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    statusCode: str
    def __init__(self, statusCode: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: int
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[int] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book", "statusCode"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    book: Book
    statusCode: str
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ..., statusCode: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventoryNo", "status"]
    class StatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    avail: InventoryItem.StatusType
    book: Book
    inventoryNo: int
    status: InventoryItem.StatusType
    taken: InventoryItem.StatusType
    def __init__(self, inventoryNo: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.StatusType, str]] = ...) -> None: ...
