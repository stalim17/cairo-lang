from enum import Enum, auto
from typing import Optional

import marshmallow_dataclass

from starkware.starkware_utils.validated_dataclass import ValidatedMarshmallowDataclass


class Mode(Enum):
    ALWAYS_FAIL = auto()
    PROB_FAIL = auto()
    SAFE = auto()


class SwitchStrategy(Enum):
    OPERATIONS = auto()
    TIME = auto()
    NO_SWITCH = auto()


@marshmallow_dataclass.dataclass(frozen=True)
class AdversarialParams(ValidatedMarshmallowDataclass):
    p_fail: float = 0.1
    min_ops: int = 5
    max_ops: int = 20
    min_time: float = 5.0
    max_time: float = 20.0
    strategy: SwitchStrategy = SwitchStrategy.OPERATIONS
    initial_mode: Optional[Mode] = None
