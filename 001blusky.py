
from bluesky import RunEngine
RE = RunEngine({})
from bluesky.plans import count,scan
from bluesky.callbacks import LivePlot

from ophyd.sim import noisy_det




