# -*- coding: utf-8 -*-
# satplot.py
"""
@version: 2020-08-22
@author: lawortsmann
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sgp4.api import Satrec, SatrecArray, jday


def pull_satellites():
    """
    pull_satellites
    """
    url = "https://www.celestrak.com/NORAD/elements/active.txt"
    tles = pd.read_csv(url, names=['TLE'])
    tles = list(tles['TLE'])
    L1, L2 = tles[1::3], tles[2::3]
    satellites = list()
    for i in range(len(L1)):
        sat = Satrec.twoline2rv(L1[i], L2[i])
        satellites.append( sat )
    return satellites


def sgp4_simulate(satellites, dt, seconds):
    """
    sgp4_simulate
    """
    dt = pd.to_datetime(dt)
    jd, fr = jday(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    fr = fr + np.arange(seconds) / (24 * 60 * 60)
    jd = np.broadcast_to(jd, fr.shape)
    fr = np.ascontiguousarray(fr)
    jd = np.ascontiguousarray(jd)
    e, r, v = satellites.sgp4(jd, fr)
    return e, r, v


def rotation_matrix(nx, ny, nz):
    """
    rotation_matrix
    """
    r = np.sqrt(nx**2 + ny**2 + nz**2)
    nx, ny, nz = nx / r, ny / r, nz / r
    nx2 = nx * nx
    ny2 = ny * ny
    nz2 = nz * nz
    r_11 = nz + ny2 / (1 + nz)
    r_12 = ny * (ny2 + nz2 - 1) / (nx * (1 + nz))
    r_13 = nx * (1 - nz2) / (nx2 + ny2)
    r_21 = ny * (ny2 + nz2 - 1) / (nx * (1 + nz))
    r_22 = 1 - ny2 / (1 + nz)
    r_23 = ny * (1 - nz2) / (nx2 + ny2)
    r_31, r_32, r_33 = -nx, -ny, nz
    R = np.array([
        [r_11, r_12, r_13],
        [r_21, r_22, r_23],
        [r_31, r_32, r_33]
    ])
    return R


def plot_satellites(filename, cmap='bone', dt='now', seconds=5400):
    """
    plot_satellites
    """
    ## pull satellites
    satellites = pull_satellites()
    satellites = SatrecArray(satellites)

    ## simulate trajectories
    _, positions, _ = sgp4_simulate(satellites, dt, seconds)

    ## build random rotation matrix
    n = np.random.normal(size=3)
    R = rotation_matrix( *n )

    ## rotate and rescale positions
    positions = np.dot(positions, R) / 6378.137

    ## build line segments
    segments = np.concatenate([
        positions[:, :-1, None, :],
        positions[:, 1:, None, :]
    ], axis=-2)
    segments = np.reshape(segments, (-1, 2, 3))

    ## setup LineCollection
    seg = segments[..., :2]
    col = np.mean(segments[..., 2], axis=-1)
    norm = plt.Normalize(vmin=-1.5, vmax=1.5, clip=True)
    lc = LineCollection(seg, cmap=cmap, norm=norm)
    lc.set_array(col)
    lc.set_linewidth(0.25)

    ## setup figure
    fig, ax = plt.subplots(figsize=(24, 16))
    ax.add_collection(lc)
    ax.set_facecolor('black')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 2)
    plt.tight_layout(pad=0.0)
    kwargs = dict(bbox_inches='tight', pad_inches=0, transparent=True)
    plt.savefig(filename, dpi=150, **kwargs)
    # plt.show()
    plt.clf()
    return True


if __name__ == "__main__":
    from argparse import ArgumentParser
    np.warnings.simplefilter(action='ignore')

    ## arguments
    parser = ArgumentParser(description="Plot satellites")
    parser.add_argument('--verbose', help='display status', action='store_true')
    args = parser.parse_args()

    cmaps = [
        'viridis', 'magma', 'inferno', 'Purples', 'bone', 'pink', 'gray', 'binary',
        'YlOrRd', 'coolwarm', 'Spectral', 'twilight', 'twilight_shifted', 'cubehelix',
        'gnuplot', 'rainbow', 'jet', 'gist_ncar',
    ]
    filename = "/home/sbbTactics/lwortsmann/curator/sat/%s.png"
    for cmap in cmaps:
        print( cmap )
        plot_satellites(filename%cmap, cmap=cmap)
    print( "Done" )
