from turnips.patterns import decrease
from turnips.patterns import decrease_spike_decrease
from turnips.patterns import decrease_spike_low
from turnips.patterns import high_low


all_patterns = {
    "high, descreasing, high, decreasing, high": high_low.pattern,
    "descreasing, spike, low": decrease_spike_low.pattern,
    "decreasing": decrease.pattern,
    "decreasing, spike, decreasing": decrease_spike_decrease.pattern,
}