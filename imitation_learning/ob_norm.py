"""Observation norm used by behavioral cloning agents and the shared autonomy agent."""
import numpy as np
import gin


@gin.configurable
def bc_mean():
    return np.array([0.0024,  0.7034,  0.0347, -0.2975, -0.0375, -0.0126,
                     0.0528,  0.0550,  -0.0248, -1.0000, -0.0947, -0.7991,
                     -0.0927, -0.6008, -0.0884, -0.3996, -0.0877, -0.1998,
                     -0.0865,  0.0000, -0.0876,  0.1998, -0.0892,  0.3996,
                     -0.0901,  0.6008, -0.0882,  0.7991, -0.0827,  1.0000,
                     -0.0851], dtype=np.float32)


@gin.configurable
def bc_std():
    return np.array([0.3812, 0.4952, 0.6652, 0.3537, 0.5616, 0.4115, 0.2236,
                     0.2279, 0.5270, 0.0000, 0.1382, 0.0000, 0.1300, 0.0000,
                     0.1248, 0.0000, 0.1140, 0.0000, 0.1124, 0.0000, 0.1058,
                     0.0000, 0.1059, 0.0000, 0.1081, 0.0000, 0.1262, 0.0000,
                     0.1441, 0.0000, 0.1496], dtype=np.float32)
