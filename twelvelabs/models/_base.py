from pydantic import BaseModel, Field, RootModel
from typing import List, Optional, TypeVar, Any


class ModelMixin:
    def __str__(self):
        return repr(self)


class Object(ModelMixin, BaseModel):
    id: str = Field(alias="_id")

    def __hash__(self) -> int:
        return self.id.__hash__()
    
    def __eq__(self, other: Any):
        if not isinstance(other, type(self)):
            return False
        return self.id == other.id


class ObjectWithTimestamp(ModelMixin, BaseModel):
    id: str = Field(alias="_id")
    created_at: str
    updated_at: Optional[str] = None


class PageInfo(BaseModel):
    limit_per_page: int
    page: int
    total_page: int
    total_results: int


class TokenPageInfo(BaseModel):
    limit_per_page: int
    total_results: int
    page_expires_at: str
    next_page_token: Optional[str] = None
    prev_page_token: Optional[str] = None


T = TypeVar("T")


class RootModelList(RootModel[List[T]]):
    """
    See https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types
    """

    def __init__(self, _list: List[T]):
        super().__init__(root=_list)

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

    def __len__(self):
        return len(self.root)
