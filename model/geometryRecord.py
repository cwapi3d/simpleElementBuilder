from dataclasses import dataclass


@dataclass
class GeometryRecord:
    id: int
    element_type: int
    width: int
    height: int
    length: int