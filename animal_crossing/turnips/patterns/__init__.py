import enum
from animal_crossing.turnips.patterns import decrease
from animal_crossing.turnips.patterns import decrease_spike_decrease
from animal_crossing.turnips.patterns import decrease_spike_low
from animal_crossing.turnips.patterns import high_low


class PATTERNS(enum.Enum):
    HIGH_LOW = "high, decrease, high, decrease, high"
    DECREASE_SPIKE_LOW = "decrease, spike, low"
    DECREASE = "decrease"
    DESCREASE_SPIKE_DECREASE = "decrease, spike, decrease"


ALL_PATTERNS = {
    PATTERNS.HIGH_LOW: high_low.pattern,
    PATTERNS.DECREASE_SPIKE_LOW: decrease_spike_low.pattern,
    PATTERNS.DECREASE: decrease.pattern,
    PATTERNS.DESCREASE_SPIKE_DECREASE: decrease_spike_decrease.pattern,
}