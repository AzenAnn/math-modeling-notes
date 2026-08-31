from __future__ import annotations

from enum import StrEnum


class Provenance(StrEnum):
    PAPER_EXPLICIT = "PAPER_EXPLICIT"
    PAPER_DERIVED = "PAPER_DERIVED"
    AI_INFERRED = "AI_INFERRED"
    EXTERNAL_REFERENCE = "EXTERNAL_REFERENCE"
    HEURISTIC = "HEURISTIC"


def weakest_provenance(values: list[str]) -> str:
    order = {
        Provenance.PAPER_EXPLICIT: 5,
        Provenance.PAPER_DERIVED: 4,
        Provenance.EXTERNAL_REFERENCE: 3,
        Provenance.HEURISTIC: 2,
        Provenance.AI_INFERRED: 1,
    }
    valid = [Provenance(v) for v in values if v in Provenance._value2member_map_]
    if not valid:
        return Provenance.AI_INFERRED
    return str(min(valid, key=lambda item: order[item]))
