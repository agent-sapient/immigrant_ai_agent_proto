from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from openapi.v3 import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Model(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_UNSPECIFIED: _ClassVar[Model]
    GPT_4O: _ClassVar[Model]
    GPT_5_1: _ClassVar[Model]
    CLAUDE_SONNET_4_5: _ClassVar[Model]
    GPT_4O_MINI: _ClassVar[Model]
MODEL_UNSPECIFIED: Model
GPT_4O: Model
GPT_5_1: Model
CLAUDE_SONNET_4_5: Model
GPT_4O_MINI: Model

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

class BatchUseAIAgentRequest(_message.Message):
    __slots__ = ()
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    models: _containers.RepeatedScalarFieldContainer[Model]
    def __init__(self, prompt: _Optional[str] = ..., models: _Optional[_Iterable[_Union[Model, str]]] = ...) -> None: ...

class ModelResult(_message.Message):
    __slots__ = ()
    MODEL_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_URLS_FIELD_NUMBER: _ClassVar[int]
    model: Model
    result: str
    output_file_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model: _Optional[_Union[Model, str]] = ..., result: _Optional[str] = ..., output_file_urls: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchUseAIAgentResponse(_message.Message):
    __slots__ = ()
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ModelResult]
    def __init__(self, results: _Optional[_Iterable[_Union[ModelResult, _Mapping]]] = ...) -> None: ...
