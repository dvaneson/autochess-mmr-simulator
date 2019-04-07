import numpy as np
from nptyping import Array

CONST = np.array([127, 102, 77, 51, -51, -77, -102, -127])
COEFF = .1725

# Calculate the placements for a player given the average of the lobby
def placements(avg_mmr: int, mmr: int) -> Array[int, 8]:
    out = ((avg_mmr - mmr) * COEFF + CONST).astype(int)
    out[0] = max(out[0], 15)
    out[7] = min(out[7], -15)
    return out

# Calculate the lobby average and the mmr change for every placement and every player
def all_placements(all_mmr: Array[int, 8]) -> Array[int, 8, 8]:
    avg_mmr = all_mmr.mean()
    out = np.array([placements(avg_mmr, mmr) for mmr in all_mmr])
    return out
