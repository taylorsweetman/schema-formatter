from dataclasses import dataclass
from enum import Enum


@dataclass
class ColumnSchema:
    name: str
    type: str


class Mode(Enum):
    PG = "postgres"
    MS = "mysql"