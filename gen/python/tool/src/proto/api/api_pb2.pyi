import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicInfo(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_TO_AI_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_TO_AI_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_TO_AI_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    POSITION_TO_AI_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_TO_AI_FIELD_NUMBER: _ClassVar[int]
    IMMIGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMMIGRATION_TYPE_TO_AI_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_TO_AI_FIELD_NUMBER: _ClassVar[int]
    EDUCATION_FIELD_NUMBER: _ClassVar[int]
    EDUCATION_TO_AI_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MAJOR_TO_AI_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    code: str
    name: str
    name_to_ai: bool
    birth_date: str
    birth_date_to_ai: bool
    work_unit: str
    work_unit_to_ai: bool
    position: str
    position_to_ai: bool
    industry: str
    industry_to_ai: bool
    immigration_type: str
    immigration_type_to_ai: bool
    field: str
    field_to_ai: bool
    education: str
    education_to_ai: bool
    major: str
    major_to_ai: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., name: _Optional[str] = ..., name_to_ai: _Optional[bool] = ..., birth_date: _Optional[str] = ..., birth_date_to_ai: _Optional[bool] = ..., work_unit: _Optional[str] = ..., work_unit_to_ai: _Optional[bool] = ..., position: _Optional[str] = ..., position_to_ai: _Optional[bool] = ..., industry: _Optional[str] = ..., industry_to_ai: _Optional[bool] = ..., immigration_type: _Optional[str] = ..., immigration_type_to_ai: _Optional[bool] = ..., field: _Optional[str] = ..., field_to_ai: _Optional[bool] = ..., education: _Optional[str] = ..., education_to_ai: _Optional[bool] = ..., major: _Optional[str] = ..., major_to_ai: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FileInfo(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    CASE_CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DIR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    URL2_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_LABEL_FIELD_NUMBER: _ClassVar[int]
    AI_TEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    parent_id: str
    case_code: str
    name: str
    is_dir: bool
    size: str
    type: str
    url: str
    url2: str
    order_by: int
    upload_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    file_label: str
    ai_text: str
    def __init__(self, id: _Optional[str] = ..., parent_id: _Optional[str] = ..., case_code: _Optional[str] = ..., name: _Optional[str] = ..., is_dir: _Optional[bool] = ..., size: _Optional[str] = ..., type: _Optional[str] = ..., url: _Optional[str] = ..., url2: _Optional[str] = ..., order_by: _Optional[int] = ..., upload_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., file_label: _Optional[str] = ..., ai_text: _Optional[str] = ...) -> None: ...

class BackgroundInfo(_message.Message):
    __slots__ = ()
    AWARDS_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_REPORTS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    PAPERS_FIELD_NUMBER: _ClassVar[int]
    EXHIBITIONS_FIELD_NUMBER: _ClassVar[int]
    LEADERSHIP_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_VALUE_FIELD_NUMBER: _ClassVar[int]
    HIGH_INCOME_FIELD_NUMBER: _ClassVar[int]
    awards: _containers.RepeatedScalarFieldContainer[str]
    memberships: _containers.RepeatedScalarFieldContainer[str]
    reviews: _containers.RepeatedScalarFieldContainer[str]
    media_reports: _containers.RepeatedScalarFieldContainer[str]
    original_contributions: _containers.RepeatedScalarFieldContainer[str]
    papers: _containers.RepeatedScalarFieldContainer[str]
    exhibitions: _containers.RepeatedScalarFieldContainer[str]
    leadership: _containers.RepeatedScalarFieldContainer[str]
    business_value: _containers.RepeatedScalarFieldContainer[str]
    high_income: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, awards: _Optional[_Iterable[str]] = ..., memberships: _Optional[_Iterable[str]] = ..., reviews: _Optional[_Iterable[str]] = ..., media_reports: _Optional[_Iterable[str]] = ..., original_contributions: _Optional[_Iterable[str]] = ..., papers: _Optional[_Iterable[str]] = ..., exhibitions: _Optional[_Iterable[str]] = ..., leadership: _Optional[_Iterable[str]] = ..., business_value: _Optional[_Iterable[str]] = ..., high_income: _Optional[_Iterable[str]] = ...) -> None: ...

class RecommenderInfo(_message.Message):
    __slots__ = ()
    RECOMMENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ONLINE_INTRODUCTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    SHARED_EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_STYLE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    recommender_name: str
    birth_date: str
    work_unit: str
    position: str
    online_introduction: str
    field: str
    industry: str
    relationship: str
    shared_experience: str
    recommendation_style: str
    contact: str
    def __init__(self, recommender_name: _Optional[str] = ..., birth_date: _Optional[str] = ..., work_unit: _Optional[str] = ..., position: _Optional[str] = ..., online_introduction: _Optional[str] = ..., field: _Optional[str] = ..., industry: _Optional[str] = ..., relationship: _Optional[str] = ..., shared_experience: _Optional[str] = ..., recommendation_style: _Optional[str] = ..., contact: _Optional[str] = ...) -> None: ...

class RecommendationLetter(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ONLINE_INTRODUCTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    SHARED_EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_STYLE_FIELD_NUMBER: _ClassVar[int]
    LETTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    recommender_name: str
    birth_date: str
    work_unit: str
    position: str
    online_introduction: str
    field: str
    industry: str
    relationship: str
    shared_experience: str
    recommendation_style: str
    letter_content: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., recommender_name: _Optional[str] = ..., birth_date: _Optional[str] = ..., work_unit: _Optional[str] = ..., position: _Optional[str] = ..., online_introduction: _Optional[str] = ..., field: _Optional[str] = ..., industry: _Optional[str] = ..., relationship: _Optional[str] = ..., shared_experience: _Optional[str] = ..., recommendation_style: _Optional[str] = ..., letter_content: _Optional[str] = ..., create_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RecommendationLetterSimple(_message.Message):
    __slots__ = ()
    RECOMMENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    LETTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    recommender_name: str
    work_unit: str
    position: str
    field: str
    relationship: str
    letter_content: str
    def __init__(self, recommender_name: _Optional[str] = ..., work_unit: _Optional[str] = ..., position: _Optional[str] = ..., field: _Optional[str] = ..., relationship: _Optional[str] = ..., letter_content: _Optional[str] = ...) -> None: ...

class GetRecommendLetterRequest(_message.Message):
    __slots__ = ()
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_INFO_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDER_INFOS_FIELD_NUMBER: _ClassVar[int]
    basic_info: BasicInfo
    background_info: BackgroundInfo
    recommender_infos: _containers.RepeatedCompositeFieldContainer[RecommenderInfo]
    def __init__(self, basic_info: _Optional[_Union[BasicInfo, _Mapping]] = ..., background_info: _Optional[_Union[BackgroundInfo, _Mapping]] = ..., recommender_infos: _Optional[_Iterable[_Union[RecommenderInfo, _Mapping]]] = ...) -> None: ...

class GetRecommendLetterResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        DATA_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        data: _containers.RepeatedCompositeFieldContainer[RecommendationLetter]
        total: int
        def __init__(self, data: _Optional[_Iterable[_Union[RecommendationLetter, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GetRecommendLetterResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GetRecommendLetterResponse.Result, _Mapping]] = ...) -> None: ...

class GenerateApplicationMaterialsRequest(_message.Message):
    __slots__ = ()
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_INFO_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_LETTERS_FIELD_NUMBER: _ClassVar[int]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    basic_info: BasicInfo
    background_info: BackgroundInfo
    recommendation_letters: _containers.RepeatedCompositeFieldContainer[RecommendationLetterSimple]
    file_list: _containers.RepeatedCompositeFieldContainer[FileInfo]
    def __init__(self, basic_info: _Optional[_Union[BasicInfo, _Mapping]] = ..., background_info: _Optional[_Union[BackgroundInfo, _Mapping]] = ..., recommendation_letters: _Optional[_Iterable[_Union[RecommendationLetterSimple, _Mapping]]] = ..., file_list: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ...) -> None: ...

class GenerateApplicationMaterialsResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        PERSONAL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
        US_PLAN_FIELD_NUMBER: _ClassVar[int]
        FILE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        personal_statement: str
        us_plan: str
        file_directory: _containers.RepeatedCompositeFieldContainer[FileInfo]
        def __init__(self, personal_statement: _Optional[str] = ..., us_plan: _Optional[str] = ..., file_directory: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GenerateApplicationMaterialsResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GenerateApplicationMaterialsResponse.Result, _Mapping]] = ...) -> None: ...

class EvaluateCaseRequest(_message.Message):
    __slots__ = ()
    PERSONAL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    US_PLAN_FIELD_NUMBER: _ClassVar[int]
    FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    personal_statement: str
    us_plan: str
    file_list: _containers.RepeatedCompositeFieldContainer[FileInfo]
    def __init__(self, personal_statement: _Optional[str] = ..., us_plan: _Optional[str] = ..., file_list: _Optional[_Iterable[_Union[FileInfo, _Mapping]]] = ...) -> None: ...

class EvaluateCaseResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        EVALUATION_REPORT_FIELD_NUMBER: _ClassVar[int]
        evaluation_report: str
        def __init__(self, evaluation_report: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: EvaluateCaseResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[EvaluateCaseResponse.Result, _Mapping]] = ...) -> None: ...

class SubmitTaskRequest(_message.Message):
    __slots__ = ()
    GET_RECOMMEND_LETTER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GENERATE_APPLICATION_MATERIALS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EVALUATE_CASE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
    get_recommend_letter_request: GetRecommendLetterRequest
    generate_application_materials_request: GenerateApplicationMaterialsRequest
    evaluate_case_request: EvaluateCaseRequest
    callback_url: str
    def __init__(self, get_recommend_letter_request: _Optional[_Union[GetRecommendLetterRequest, _Mapping]] = ..., generate_application_materials_request: _Optional[_Union[GenerateApplicationMaterialsRequest, _Mapping]] = ..., evaluate_case_request: _Optional[_Union[EvaluateCaseRequest, _Mapping]] = ..., callback_url: _Optional[str] = ...) -> None: ...

class SubmitTaskResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        task_id: str
        def __init__(self, task_id: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: SubmitTaskResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[SubmitTaskResponse.Result, _Mapping]] = ...) -> None: ...

class Task(_message.Message):
    __slots__ = ()
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    GET_RECOMMEND_LETTER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_APPLICATION_MATERIALS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EVALUATE_CASE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    status: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    error_message: str
    progress: float
    get_recommend_letter_response: GetRecommendLetterResponse
    generate_application_materials_response: GenerateApplicationMaterialsResponse
    evaluate_case_response: EvaluateCaseResponse
    def __init__(self, task_id: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error_message: _Optional[str] = ..., progress: _Optional[float] = ..., get_recommend_letter_response: _Optional[_Union[GetRecommendLetterResponse, _Mapping]] = ..., generate_application_materials_response: _Optional[_Union[GenerateApplicationMaterialsResponse, _Mapping]] = ..., evaluate_case_response: _Optional[_Union[EvaluateCaseResponse, _Mapping]] = ...) -> None: ...

class TaskQueryRequest(_message.Message):
    __slots__ = ()
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class TaskQueryResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        TASK_FIELD_NUMBER: _ClassVar[int]
        task: Task
        def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: TaskQueryResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[TaskQueryResponse.Result, _Mapping]] = ...) -> None: ...

class TaskCancelRequest(_message.Message):
    __slots__ = ()
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class TaskCancelResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class PassportStatusQueryRequest(_message.Message):
    __slots__ = ()
    VISA_CASE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PASSPORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SURNAME_FIELD_NUMBER: _ClassVar[int]
    VISA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_BROWSER_FIELD_NUMBER: _ClassVar[int]
    visa_case_number: str
    passport_number: str
    surname: str
    visa_type: str
    show_browser: bool
    def __init__(self, visa_case_number: _Optional[str] = ..., passport_number: _Optional[str] = ..., surname: _Optional[str] = ..., visa_type: _Optional[str] = ..., show_browser: _Optional[bool] = ...) -> None: ...

class PassportStatusQueryResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        CAPTCHA_RECOGNIZED_FIELD_NUMBER: _ClassVar[int]
        FINAL_URL_FIELD_NUMBER: _ClassVar[int]
        PAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
        HTML_FILE_FIELD_NUMBER: _ClassVar[int]
        SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_DIR_FIELD_NUMBER: _ClassVar[int]
        QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
        HAS_DATA_FIELD_NUMBER: _ClassVar[int]
        RESULT_DATA_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        success: bool
        message: str
        captcha_recognized: str
        final_url: str
        page_title: str
        html_file: str
        screenshot: str
        output_dir: str
        query_result: str
        has_data: bool
        result_data: str
        error_message: str
        def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., captcha_recognized: _Optional[str] = ..., final_url: _Optional[str] = ..., page_title: _Optional[str] = ..., html_file: _Optional[str] = ..., screenshot: _Optional[str] = ..., output_dir: _Optional[str] = ..., query_result: _Optional[str] = ..., has_data: _Optional[bool] = ..., result_data: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: PassportStatusQueryResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[PassportStatusQueryResponse.Result, _Mapping]] = ...) -> None: ...

class DataSourceSearchTask(_message.Message):
    __slots__ = ()
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    search_query: str
    data_source: str
    parent_task_id: str
    def __init__(self, search_query: _Optional[str] = ..., data_source: _Optional[str] = ..., parent_task_id: _Optional[str] = ...) -> None: ...

class SearchResult(_message.Message):
    __slots__ = ()
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    source: str
    title: str
    url: str
    content: str
    relevance_score: float
    def __init__(self, source: _Optional[str] = ..., title: _Optional[str] = ..., url: _Optional[str] = ..., content: _Optional[str] = ..., relevance_score: _Optional[float] = ...) -> None: ...

class ParallelSearchResult(_message.Message):
    __slots__ = ()
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    MERGED_RESULT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchResult]
    merged_result: str
    completed_at: _timestamp_pb2.Timestamp
    def __init__(self, results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]] = ..., merged_result: _Optional[str] = ..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OutputFileInfo(_message.Message):
    __slots__ = ()
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    is_directory: bool
    size: int
    modified_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ..., is_directory: _Optional[bool] = ..., size: _Optional[int] = ..., modified_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListOutputFilesRequest(_message.Message):
    __slots__ = ()
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ListOutputFilesResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        FILES_FIELD_NUMBER: _ClassVar[int]
        CURRENT_PATH_FIELD_NUMBER: _ClassVar[int]
        files: _containers.RepeatedCompositeFieldContainer[OutputFileInfo]
        current_path: str
        def __init__(self, files: _Optional[_Iterable[_Union[OutputFileInfo, _Mapping]]] = ..., current_path: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: ListOutputFilesResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[ListOutputFilesResponse.Result, _Mapping]] = ...) -> None: ...

class DownloadOutputFileRequest(_message.Message):
    __slots__ = ()
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    AS_ZIP_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    as_zip: bool
    def __init__(self, file_path: _Optional[str] = ..., as_zip: _Optional[bool] = ...) -> None: ...

class DownloadOutputFileResponse(_message.Message):
    __slots__ = ()
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    content_type: str
    file_content: bytes
    file_size: int
    def __init__(self, file_name: _Optional[str] = ..., content_type: _Optional[str] = ..., file_content: _Optional[bytes] = ..., file_size: _Optional[int] = ...) -> None: ...

class EvaluationResult(_message.Message):
    __slots__ = ()
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    category: str
    score: int
    description: str
    def __init__(self, category: _Optional[str] = ..., score: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class GeneratePlanRequest(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    MARITAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    EDUCATION_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    GRADUATED_SCHOOL_FIELD_NUMBER: _ClassVar[int]
    SPOUSE_EDUCATION_FIELD_NUMBER: _ClassVar[int]
    SPOUSE_MAJOR_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_AGE_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_STATUS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    WECHAT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RESIDENCE_FIELD_NUMBER: _ClassVar[int]
    POLITICAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    MILITARY_SERVICE_FIELD_NUMBER: _ClassVar[int]
    HAS_CRIMINAL_RECORD_FIELD_NUMBER: _ClassVar[int]
    IMMIGRATION_INTENT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    VISA_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_CATEGORY_DESC_FIELD_NUMBER: _ClassVar[int]
    US_IMMIGRATION_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    US_IMMIGRATION_APPLY_DATE_FIELD_NUMBER: _ClassVar[int]
    US_IMMIGRATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    APPLIED_US_IMMIGRATION_FIELD_NUMBER: _ClassVar[int]
    APPLIED_US_VISA_FIELD_NUMBER: _ClassVar[int]
    US_VISA_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    US_VISA_CATEGORY_DESC_FIELD_NUMBER: _ClassVar[int]
    US_VISA_STATUS_FIELD_NUMBER: _ClassVar[int]
    US_VISA_VALID_FIELD_NUMBER: _ClassVar[int]
    US_VISA_RESULT_FIELD_NUMBER: _ClassVar[int]
    B_VISA_VALIDITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    EVUS_STATUS_DESC_FIELD_NUMBER: _ClassVar[int]
    EVUS_LAST_UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    VISA_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    APPLY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_JOB_FIELD_NUMBER: _ClassVar[int]
    CURRENT_EMPLOYER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    WORK_EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_INFO_FIELD_NUMBER: _ClassVar[int]
    CORE_ASSETS_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    AWARDS_FIELD_NUMBER: _ClassVar[int]
    HAS_NATIONAL_OR_INTERNATIONAL_AWARD_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_OR_INTERNATIONAL_AWARD_NAME_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_OR_INTERNATIONAL_AWARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_PROVINCIAL_OR_ASSOCIATION_AWARD_FIELD_NUMBER: _ClassVar[int]
    PROVINCIAL_OR_ASSOCIATION_AWARD_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVINCIAL_OR_ASSOCIATION_AWARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACADEMIC_ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_ACADEMIC_PAPER_CITATION_FIELD_NUMBER: _ClassVar[int]
    CITATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_CORE_JOURNAL_OR_CONFERENCE_PAPER_FIELD_NUMBER: _ClassVar[int]
    CORE_JOURNAL_OR_CONFERENCE_PAPER_TYPES_FIELD_NUMBER: _ClassVar[int]
    CORE_JOURNAL_OR_CONFERENCE_PAPER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_RECOGNITION_FIELD_NUMBER: _ClassVar[int]
    HAS_MEDIA_RECOGNITION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_PLATFORM_TYPES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_PLATFORM_OTHER_FIELD_NUMBER: _ClassVar[int]
    MEDIA_RECOGNITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROFESSIONAL_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    HAS_NATIONAL_OR_INTERNATIONAL_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_ROLES_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    JUDGE_EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_ROLES_FIELD_NUMBER: _ClassVar[int]
    REVIEW_ROLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    HAS_BREAKTHROUGH_THEORY_OR_TECH_FIELD_NUMBER: _ClassVar[int]
    BREAKTHROUGH_THEORY_OR_TECH_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEADERSHIP_FIELD_NUMBER: _ClassVar[int]
    HAS_LANDMARK_PROJECT_OR_CASE_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_PROJECT_OR_CASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    HIGH_SALARY_FIELD_NUMBER: _ClassVar[int]
    COMMERCIAL_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ECONOMIC_ACHIEVEMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    HAS_INVENTION_PATENT_FIELD_NUMBER: _ClassVar[int]
    INVENTION_PATENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_SOFTWARE_COPYRIGHT_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_COPYRIGHT_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_NATIONAL_OR_INTERNATIONAL_PROJECT_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_OR_INTERNATIONAL_PROJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_INTERNATIONAL_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    INTERNATIONAL_ACTIVITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    HAS_SOCIAL_TITLE_OR_HONOR_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_TITLE_OR_HONOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_TITLE_OR_HONOR_OTHER_FIELD_NUMBER: _ClassVar[int]
    HAS_SPECIAL_ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_ACHIEVEMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    HAS_US_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    US_DOCUMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_INDUSTRY_VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IMMIGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    member_id: int
    name: str
    gender: str
    age: int
    marital_status: str
    education: str
    major: str
    graduated_school: str
    spouse_education: str
    spouse_major: str
    children_count: int
    has_children: bool
    children_age: str
    children_status: str
    phone: str
    email: str
    wechat: str
    account_location: str
    current_residence: str
    political_status: str
    military_service: bool
    has_criminal_record: bool
    immigration_intent: str
    application_date: str
    visa_type: str
    application_category: str
    application_category_desc: str
    us_immigration_category: str
    us_immigration_apply_date: str
    us_immigration_result: str
    applied_us_immigration: bool
    applied_us_visa: bool
    us_visa_category: str
    us_visa_category_desc: str
    us_visa_status: str
    us_visa_valid: bool
    us_visa_result: str
    b_visa_validity_type: str
    evus_status: str
    evus_status_desc: str
    evus_last_update_date: str
    visa_status: str
    result: str
    apply_type: str
    current_job: str
    current_employer: str
    current_position: str
    work_experience: str
    company_info: str
    core_assets: str
    supplement_info: str
    awards: str
    has_national_or_international_award: bool
    national_or_international_award_name: str
    national_or_international_award_count: int
    has_provincial_or_association_award: bool
    provincial_or_association_award_name: str
    provincial_or_association_award_count: int
    academic_achievements: str
    has_academic_paper_citation: bool
    citation_count: int
    has_core_journal_or_conference_paper: bool
    core_journal_or_conference_paper_types: str
    core_journal_or_conference_paper_count: int
    media_recognition: str
    has_media_recognition: bool
    media_platform_types: str
    media_platform_other: str
    media_recognition_count: int
    professional_membership: str
    has_national_or_international_association: bool
    association_roles: str
    association_count: int
    judge_experience: str
    review_roles: str
    review_role_count: int
    original_contribution: str
    has_breakthrough_theory_or_tech: bool
    breakthrough_theory_or_tech_count: int
    leadership: str
    has_landmark_project_or_case: bool
    landmark_project_or_case_count: int
    high_salary: str
    commercial_success: str
    economic_achievement_types: str
    has_invention_patent: bool
    invention_patent_count: int
    has_software_copyright: bool
    software_copyright_count: int
    has_national_or_international_project: bool
    national_or_international_project_count: int
    has_international_activity: bool
    international_activity_types: str
    has_social_title_or_honor: bool
    social_title_or_honor_types: str
    social_title_or_honor_other: str
    has_special_achievement: bool
    special_achievement_types: str
    has_us_document: bool
    us_document_types: str
    business_industry_value: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    immigration_type: str
    def __init__(self, id: _Optional[int] = ..., member_id: _Optional[int] = ..., name: _Optional[str] = ..., gender: _Optional[str] = ..., age: _Optional[int] = ..., marital_status: _Optional[str] = ..., education: _Optional[str] = ..., major: _Optional[str] = ..., graduated_school: _Optional[str] = ..., spouse_education: _Optional[str] = ..., spouse_major: _Optional[str] = ..., children_count: _Optional[int] = ..., has_children: _Optional[bool] = ..., children_age: _Optional[str] = ..., children_status: _Optional[str] = ..., phone: _Optional[str] = ..., email: _Optional[str] = ..., wechat: _Optional[str] = ..., account_location: _Optional[str] = ..., current_residence: _Optional[str] = ..., political_status: _Optional[str] = ..., military_service: _Optional[bool] = ..., has_criminal_record: _Optional[bool] = ..., immigration_intent: _Optional[str] = ..., application_date: _Optional[str] = ..., visa_type: _Optional[str] = ..., application_category: _Optional[str] = ..., application_category_desc: _Optional[str] = ..., us_immigration_category: _Optional[str] = ..., us_immigration_apply_date: _Optional[str] = ..., us_immigration_result: _Optional[str] = ..., applied_us_immigration: _Optional[bool] = ..., applied_us_visa: _Optional[bool] = ..., us_visa_category: _Optional[str] = ..., us_visa_category_desc: _Optional[str] = ..., us_visa_status: _Optional[str] = ..., us_visa_valid: _Optional[bool] = ..., us_visa_result: _Optional[str] = ..., b_visa_validity_type: _Optional[str] = ..., evus_status: _Optional[str] = ..., evus_status_desc: _Optional[str] = ..., evus_last_update_date: _Optional[str] = ..., visa_status: _Optional[str] = ..., result: _Optional[str] = ..., apply_type: _Optional[str] = ..., current_job: _Optional[str] = ..., current_employer: _Optional[str] = ..., current_position: _Optional[str] = ..., work_experience: _Optional[str] = ..., company_info: _Optional[str] = ..., core_assets: _Optional[str] = ..., supplement_info: _Optional[str] = ..., awards: _Optional[str] = ..., has_national_or_international_award: _Optional[bool] = ..., national_or_international_award_name: _Optional[str] = ..., national_or_international_award_count: _Optional[int] = ..., has_provincial_or_association_award: _Optional[bool] = ..., provincial_or_association_award_name: _Optional[str] = ..., provincial_or_association_award_count: _Optional[int] = ..., academic_achievements: _Optional[str] = ..., has_academic_paper_citation: _Optional[bool] = ..., citation_count: _Optional[int] = ..., has_core_journal_or_conference_paper: _Optional[bool] = ..., core_journal_or_conference_paper_types: _Optional[str] = ..., core_journal_or_conference_paper_count: _Optional[int] = ..., media_recognition: _Optional[str] = ..., has_media_recognition: _Optional[bool] = ..., media_platform_types: _Optional[str] = ..., media_platform_other: _Optional[str] = ..., media_recognition_count: _Optional[int] = ..., professional_membership: _Optional[str] = ..., has_national_or_international_association: _Optional[bool] = ..., association_roles: _Optional[str] = ..., association_count: _Optional[int] = ..., judge_experience: _Optional[str] = ..., review_roles: _Optional[str] = ..., review_role_count: _Optional[int] = ..., original_contribution: _Optional[str] = ..., has_breakthrough_theory_or_tech: _Optional[bool] = ..., breakthrough_theory_or_tech_count: _Optional[int] = ..., leadership: _Optional[str] = ..., has_landmark_project_or_case: _Optional[bool] = ..., landmark_project_or_case_count: _Optional[int] = ..., high_salary: _Optional[str] = ..., commercial_success: _Optional[str] = ..., economic_achievement_types: _Optional[str] = ..., has_invention_patent: _Optional[bool] = ..., invention_patent_count: _Optional[int] = ..., has_software_copyright: _Optional[bool] = ..., software_copyright_count: _Optional[int] = ..., has_national_or_international_project: _Optional[bool] = ..., national_or_international_project_count: _Optional[int] = ..., has_international_activity: _Optional[bool] = ..., international_activity_types: _Optional[str] = ..., has_social_title_or_honor: _Optional[bool] = ..., social_title_or_honor_types: _Optional[str] = ..., social_title_or_honor_other: _Optional[str] = ..., has_special_achievement: _Optional[bool] = ..., special_achievement_types: _Optional[str] = ..., has_us_document: _Optional[bool] = ..., us_document_types: _Optional[str] = ..., business_industry_value: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., immigration_type: _Optional[str] = ...) -> None: ...

class GeneratePlanResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        PLAN_FIELD_NUMBER: _ClassVar[int]
        PLAN_URL_FIELD_NUMBER: _ClassVar[int]
        EVALUATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
        plan: str
        plan_url: str
        evaluation_results: _containers.RepeatedCompositeFieldContainer[EvaluationResult]
        def __init__(self, plan: _Optional[str] = ..., plan_url: _Optional[str] = ..., evaluation_results: _Optional[_Iterable[_Union[EvaluationResult, _Mapping]]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESULT_EN_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GeneratePlanResponse.Result
    result_en: GeneratePlanResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GeneratePlanResponse.Result, _Mapping]] = ..., result_en: _Optional[_Union[GeneratePlanResponse.Result, _Mapping]] = ...) -> None: ...

class VisaHistoryRecord(_message.Message):
    __slots__ = ()
    VISA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_DATE_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    visa_type: str
    issue_date: str
    expiry_date: str
    work_unit: str
    position: str
    def __init__(self, visa_type: _Optional[str] = ..., issue_date: _Optional[str] = ..., expiry_date: _Optional[str] = ..., work_unit: _Optional[str] = ..., position: _Optional[str] = ...) -> None: ...

class ExtendedBasicInfo(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_TO_AI_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_TO_AI_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_FIELD_NUMBER: _ClassVar[int]
    WORK_UNIT_TO_AI_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    POSITION_TO_AI_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_TO_AI_FIELD_NUMBER: _ClassVar[int]
    IMMIGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMMIGRATION_TYPE_TO_AI_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELD_TO_AI_FIELD_NUMBER: _ClassVar[int]
    EDUCATION_FIELD_NUMBER: _ClassVar[int]
    EDUCATION_TO_AI_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MAJOR_TO_AI_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_CARD_FIELD_NUMBER: _ClassVar[int]
    ID_CARD_START_DATE_FIELD_NUMBER: _ClassVar[int]
    ID_CARD_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    PASSPORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PASSPORT_START_DATE_FIELD_NUMBER: _ClassVar[int]
    PASSPORT_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    IMMIGRATION_TYPE_OTHER_FIELD_NUMBER: _ClassVar[int]
    VISA_HISTORY_FIELD_NUMBER: _ClassVar[int]
    RESUME_FILE_URL_FIELD_NUMBER: _ClassVar[int]
    id: int
    code: str
    name: str
    name_to_ai: bool
    birth_date: str
    birth_date_to_ai: bool
    work_unit: str
    work_unit_to_ai: bool
    position: str
    position_to_ai: bool
    industry: str
    industry_to_ai: bool
    immigration_type: str
    immigration_type_to_ai: bool
    field: str
    field_to_ai: bool
    education: str
    education_to_ai: bool
    major: str
    major_to_ai: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    id_card: str
    id_card_start_date: str
    id_card_expiry: str
    passport_number: str
    passport_start_date: str
    passport_expiry: str
    immigration_type_other: str
    visa_history: _containers.RepeatedCompositeFieldContainer[VisaHistoryRecord]
    resume_file_url: str
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., name: _Optional[str] = ..., name_to_ai: _Optional[bool] = ..., birth_date: _Optional[str] = ..., birth_date_to_ai: _Optional[bool] = ..., work_unit: _Optional[str] = ..., work_unit_to_ai: _Optional[bool] = ..., position: _Optional[str] = ..., position_to_ai: _Optional[bool] = ..., industry: _Optional[str] = ..., industry_to_ai: _Optional[bool] = ..., immigration_type: _Optional[str] = ..., immigration_type_to_ai: _Optional[bool] = ..., field: _Optional[str] = ..., field_to_ai: _Optional[bool] = ..., education: _Optional[str] = ..., education_to_ai: _Optional[bool] = ..., major: _Optional[str] = ..., major_to_ai: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., id_card: _Optional[str] = ..., id_card_start_date: _Optional[str] = ..., id_card_expiry: _Optional[str] = ..., passport_number: _Optional[str] = ..., passport_start_date: _Optional[str] = ..., passport_expiry: _Optional[str] = ..., immigration_type_other: _Optional[str] = ..., visa_history: _Optional[_Iterable[_Union[VisaHistoryRecord, _Mapping]]] = ..., resume_file_url: _Optional[str] = ...) -> None: ...

class SaveBasicInfoRequest(_message.Message):
    __slots__ = ()
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    basic_info: ExtendedBasicInfo
    case_id: str
    def __init__(self, basic_info: _Optional[_Union[ExtendedBasicInfo, _Mapping]] = ..., case_id: _Optional[str] = ...) -> None: ...

class SaveBasicInfoResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        CASE_ID_FIELD_NUMBER: _ClassVar[int]
        BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
        case_id: str
        basic_info: ExtendedBasicInfo
        def __init__(self, case_id: _Optional[str] = ..., basic_info: _Optional[_Union[ExtendedBasicInfo, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: SaveBasicInfoResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[SaveBasicInfoResponse.Result, _Mapping]] = ...) -> None: ...

class GetBasicInfoRequest(_message.Message):
    __slots__ = ()
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    case_id: str
    def __init__(self, case_id: _Optional[str] = ...) -> None: ...

class GetBasicInfoResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
        basic_info: ExtendedBasicInfo
        def __init__(self, basic_info: _Optional[_Union[ExtendedBasicInfo, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GetBasicInfoResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GetBasicInfoResponse.Result, _Mapping]] = ...) -> None: ...

class SaveBasicInfoDraftRequest(_message.Message):
    __slots__ = ()
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    basic_info: ExtendedBasicInfo
    case_id: str
    def __init__(self, basic_info: _Optional[_Union[ExtendedBasicInfo, _Mapping]] = ..., case_id: _Optional[str] = ...) -> None: ...

class SaveBasicInfoDraftResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        CASE_ID_FIELD_NUMBER: _ClassVar[int]
        SAVED_AT_FIELD_NUMBER: _ClassVar[int]
        case_id: str
        saved_at: _timestamp_pb2.Timestamp
        def __init__(self, case_id: _Optional[str] = ..., saved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: SaveBasicInfoDraftResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[SaveBasicInfoDraftResponse.Result, _Mapping]] = ...) -> None: ...

class UploadResumeFileRequest(_message.Message):
    __slots__ = ()
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    case_id: str
    file_name: str
    file_content: bytes
    file_type: str
    def __init__(self, case_id: _Optional[str] = ..., file_name: _Optional[str] = ..., file_content: _Optional[bytes] = ..., file_type: _Optional[str] = ...) -> None: ...

class UploadResumeFileResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        FILE_URL_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        file_url: str
        file_name: str
        def __init__(self, file_url: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: UploadResumeFileResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[UploadResumeFileResponse.Result, _Mapping]] = ...) -> None: ...

class AwardInfo(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    case_id: str
    title: str
    year: str
    level: str
    status: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., case_id: _Optional[str] = ..., title: _Optional[str] = ..., year: _Optional[str] = ..., level: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAwardRequest(_message.Message):
    __slots__ = ()
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    case_id: str
    title: str
    year: str
    level: str
    def __init__(self, case_id: _Optional[str] = ..., title: _Optional[str] = ..., year: _Optional[str] = ..., level: _Optional[str] = ...) -> None: ...

class CreateAwardResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        AWARD_FIELD_NUMBER: _ClassVar[int]
        award: AwardInfo
        def __init__(self, award: _Optional[_Union[AwardInfo, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: CreateAwardResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[CreateAwardResponse.Result, _Mapping]] = ...) -> None: ...

class ListAwardsRequest(_message.Message):
    __slots__ = ()
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    case_id: str
    status: str
    def __init__(self, case_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class ListAwardsResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        AWARDS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        awards: _containers.RepeatedCompositeFieldContainer[AwardInfo]
        total: int
        def __init__(self, awards: _Optional[_Iterable[_Union[AwardInfo, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: ListAwardsResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[ListAwardsResponse.Result, _Mapping]] = ...) -> None: ...

class UpdateAwardRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    title: str
    year: str
    level: str
    def __init__(self, award_id: _Optional[str] = ..., title: _Optional[str] = ..., year: _Optional[str] = ..., level: _Optional[str] = ...) -> None: ...

class UpdateAwardResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        AWARD_FIELD_NUMBER: _ClassVar[int]
        award: AwardInfo
        def __init__(self, award: _Optional[_Union[AwardInfo, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: UpdateAwardResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[UpdateAwardResponse.Result, _Mapping]] = ...) -> None: ...

class DeleteAwardRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    def __init__(self, award_id: _Optional[str] = ...) -> None: ...

class DeleteAwardResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class LockAwardRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    def __init__(self, award_id: _Optional[str] = ...) -> None: ...

class LockAwardResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        AWARD_FIELD_NUMBER: _ClassVar[int]
        award: AwardInfo
        def __init__(self, award: _Optional[_Union[AwardInfo, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: LockAwardResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[LockAwardResponse.Result, _Mapping]] = ...) -> None: ...

class UnlockAwardRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    def __init__(self, award_id: _Optional[str] = ...) -> None: ...

class UnlockAwardResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        AWARD_FIELD_NUMBER: _ClassVar[int]
        award: AwardInfo
        def __init__(self, award: _Optional[_Union[AwardInfo, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: UnlockAwardResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[UnlockAwardResponse.Result, _Mapping]] = ...) -> None: ...

class AwardFileInfo(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    award_id: str
    name: str
    size: str
    type: str
    url: str
    category: str
    status: str
    upload_progress: int
    description: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., award_id: _Optional[str] = ..., name: _Optional[str] = ..., size: _Optional[str] = ..., type: _Optional[str] = ..., url: _Optional[str] = ..., category: _Optional[str] = ..., status: _Optional[str] = ..., upload_progress: _Optional[int] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UploadAwardFileRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    file_content: bytes
    file_name: str
    file_type: str
    def __init__(self, award_id: _Optional[str] = ..., file_content: _Optional[bytes] = ..., file_name: _Optional[str] = ..., file_type: _Optional[str] = ...) -> None: ...

class UploadAwardFileResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        FILE_FIELD_NUMBER: _ClassVar[int]
        file: AwardFileInfo
        def __init__(self, file: _Optional[_Union[AwardFileInfo, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: UploadAwardFileResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[UploadAwardFileResponse.Result, _Mapping]] = ...) -> None: ...

class DeleteAwardFileRequest(_message.Message):
    __slots__ = ()
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class DeleteAwardFileResponse(_message.Message):
    __slots__ = ()
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class ListAwardFilesRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    def __init__(self, award_id: _Optional[str] = ...) -> None: ...

class ListAwardFilesResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        FILES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        files: _containers.RepeatedCompositeFieldContainer[AwardFileInfo]
        total: int
        def __init__(self, files: _Optional[_Iterable[_Union[AwardFileInfo, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: ListAwardFilesResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[ListAwardFilesResponse.Result, _Mapping]] = ...) -> None: ...

class SearchAwardMaterialsRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    search_query: str
    def __init__(self, award_id: _Optional[str] = ..., search_query: _Optional[str] = ...) -> None: ...

class SearchAwardMaterialsResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
        RETRIEVED_FILES_FIELD_NUMBER: _ClassVar[int]
        MERGED_RESULT_FIELD_NUMBER: _ClassVar[int]
        search_results: _containers.RepeatedCompositeFieldContainer[SearchResult]
        retrieved_files: _containers.RepeatedCompositeFieldContainer[AwardFileInfo]
        merged_result: str
        def __init__(self, search_results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]] = ..., retrieved_files: _Optional[_Iterable[_Union[AwardFileInfo, _Mapping]]] = ..., merged_result: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: SearchAwardMaterialsResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[SearchAwardMaterialsResponse.Result, _Mapping]] = ...) -> None: ...

class RequiredFileItem(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    IS_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    description: str
    is_required: bool
    is_uploaded: bool
    category: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., description: _Optional[str] = ..., is_required: _Optional[bool] = ..., is_uploaded: _Optional[bool] = ..., category: _Optional[str] = ...) -> None: ...

class GetAwardRequiredFilesRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    def __init__(self, award_id: _Optional[str] = ...) -> None: ...

class GetAwardRequiredFilesResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        REQUIRED_FILES_FIELD_NUMBER: _ClassVar[int]
        AI_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        CHECKLIST_PROMPT_FIELD_NUMBER: _ClassVar[int]
        IS_COMPLETE_FIELD_NUMBER: _ClassVar[int]
        MISSING_ITEMS_FIELD_NUMBER: _ClassVar[int]
        ANALYSIS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        required_files: _containers.RepeatedCompositeFieldContainer[RequiredFileItem]
        ai_suggestion: str
        checklist_prompt: str
        is_complete: bool
        missing_items: _containers.RepeatedScalarFieldContainer[str]
        analysis_message: str
        def __init__(self, required_files: _Optional[_Iterable[_Union[RequiredFileItem, _Mapping]]] = ..., ai_suggestion: _Optional[str] = ..., checklist_prompt: _Optional[str] = ..., is_complete: _Optional[bool] = ..., missing_items: _Optional[_Iterable[str]] = ..., analysis_message: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GetAwardRequiredFilesResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GetAwardRequiredFilesResponse.Result, _Mapping]] = ...) -> None: ...

class AwardChatMessage(_message.Message):
    __slots__ = ()
    ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    award_id: str
    content: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., award_id: _Optional[str] = ..., content: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SaveAwardChatMessagesRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    messages: _containers.RepeatedCompositeFieldContainer[AwardChatMessage]
    def __init__(self, award_id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[AwardChatMessage, _Mapping]]] = ...) -> None: ...

class SaveAwardChatMessagesResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        SAVED_COUNT_FIELD_NUMBER: _ClassVar[int]
        SAVED_IDS_FIELD_NUMBER: _ClassVar[int]
        saved_count: int
        saved_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, saved_count: _Optional[int] = ..., saved_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: SaveAwardChatMessagesResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[SaveAwardChatMessagesResponse.Result, _Mapping]] = ...) -> None: ...

class GetAwardChatMessagesRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    page: int
    page_size: int
    cursor: str
    def __init__(self, award_id: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class GetAwardChatMessagesResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        PAGE_FIELD_NUMBER: _ClassVar[int]
        PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        HAS_MORE_FIELD_NUMBER: _ClassVar[int]
        NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
        messages: _containers.RepeatedCompositeFieldContainer[AwardChatMessage]
        total: int
        page: int
        page_size: int
        has_more: bool
        next_cursor: str
        def __init__(self, messages: _Optional[_Iterable[_Union[AwardChatMessage, _Mapping]]] = ..., total: _Optional[int] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., has_more: _Optional[bool] = ..., next_cursor: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GetAwardChatMessagesResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GetAwardChatMessagesResponse.Result, _Mapping]] = ...) -> None: ...

class DeleteAwardChatMessagesRequest(_message.Message):
    __slots__ = ()
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    award_id: str
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, award_id: _Optional[str] = ..., message_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteAwardChatMessagesResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
        deleted_count: int
        def __init__(self, deleted_count: _Optional[int] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: DeleteAwardChatMessagesResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[DeleteAwardChatMessagesResponse.Result, _Mapping]] = ...) -> None: ...

class GetModuleGuideRequest(_message.Message):
    __slots__ = ()
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    case_id: str
    module: str
    def __init__(self, case_id: _Optional[str] = ..., module: _Optional[str] = ...) -> None: ...

class GetModuleGuideResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        GUIDE_TEXT_FIELD_NUMBER: _ClassVar[int]
        FROM_CACHE_FIELD_NUMBER: _ClassVar[int]
        guide_text: str
        from_cache: bool
        def __init__(self, guide_text: _Optional[str] = ..., from_cache: _Optional[bool] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GetModuleGuideResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GetModuleGuideResponse.Result, _Mapping]] = ...) -> None: ...

class CreateCaseRequest(_message.Message):
    __slots__ = ()
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    basic_info: ExtendedBasicInfo
    def __init__(self, basic_info: _Optional[_Union[ExtendedBasicInfo, _Mapping]] = ...) -> None: ...

class CreateCaseResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        CASE_ID_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        case_id: str
        created_at: _timestamp_pb2.Timestamp
        def __init__(self, case_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: CreateCaseResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[CreateCaseResponse.Result, _Mapping]] = ...) -> None: ...

class GetCaseRequest(_message.Message):
    __slots__ = ()
    CASE_ID_FIELD_NUMBER: _ClassVar[int]
    case_id: str
    def __init__(self, case_id: _Optional[str] = ...) -> None: ...

class GetCaseResponse(_message.Message):
    __slots__ = ()
    class Result(_message.Message):
        __slots__ = ()
        CASE_ID_FIELD_NUMBER: _ClassVar[int]
        BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
        AWARDS_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        case_id: str
        basic_info: ExtendedBasicInfo
        awards: _containers.RepeatedCompositeFieldContainer[AwardInfo]
        created_at: _timestamp_pb2.Timestamp
        updated_at: _timestamp_pb2.Timestamp
        def __init__(self, case_id: _Optional[str] = ..., basic_info: _Optional[_Union[ExtendedBasicInfo, _Mapping]] = ..., awards: _Optional[_Iterable[_Union[AwardInfo, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    result: GetCaseResponse.Result
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ..., result: _Optional[_Union[GetCaseResponse.Result, _Mapping]] = ...) -> None: ...
