import datetime
from typing import Union, TypedDict


class ResultDict(TypedDict):
    number: str
    name: str
    surname: str
    result: Union[str, datetime.timedelta]
