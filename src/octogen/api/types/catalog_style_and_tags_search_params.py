# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CatalogStyleAndTagsSearchParams"]


class CatalogStyleAndTagsSearchParams(TypedDict, total=False):
    type: Required[str]

    styles: Required[SequenceNotStr[str]]

    tags: Required[SequenceNotStr[str]]

    compact_mode: Optional[Literal["compact", "medium"]]

    limit: int
