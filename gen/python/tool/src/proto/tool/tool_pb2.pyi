from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from openapi.v3 import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UseAIAgentRequest(_message.Message):
    __slots__ = ()
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    def __init__(self, prompt: _Optional[str] = ...) -> None: ...

class UseAIAgentResponse(_message.Message):
    __slots__ = ()
    RESULT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_URLS_FIELD_NUMBER: _ClassVar[int]
    result: str
    output_file_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, result: _Optional[str] = ..., output_file_urls: _Optional[_Iterable[str]] = ...) -> None: ...
