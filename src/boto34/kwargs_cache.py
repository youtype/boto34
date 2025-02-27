from collections.abc import Mapping
from typing import Any, Generic, TypeVar

_T = TypeVar("_T")
KwargsType = Mapping[str, Any]


class KwargsCache(Generic[_T]):
    def __init__(self) -> None:
        self._cache: dict[int, _T] = {}

    @staticmethod
    def get_cache_key(kwargs: KwargsType) -> int:
        return hash(tuple(sorted(kwargs.items())))

    def get(self, kwargs: Mapping[str, Any]) -> _T | None:
        return self._cache.get(self.get_cache_key(kwargs))

    def set(self, kwargs: Mapping[str, Any], value: _T) -> None:
        self._cache[self.get_cache_key(kwargs)] = value

    def get_first(self) -> _T | None:
        return next(iter(self._cache.values()), None)

    def clear(self) -> None:
        self._cache.clear()
