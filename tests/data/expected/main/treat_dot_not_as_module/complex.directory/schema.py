# generated by datamodel-codegen:
#   filename:  complex.directory/schema.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class ExtType(BaseModel):
    ExtType: Optional[Any] = Field(None, title='ExtType')
