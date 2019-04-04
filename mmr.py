from typing import List

import colorlover as cl
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

import numpy as np
from nptyping import Array

CONST = np.array([127, 102, 77, 51, -51, -77, -102, -127])
COEFF = .1725

def bar_chart(input: Array[int,8,8], all_mmr: Array[int, 8]):
    # x = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5', 'Player 6', 'Player 7', 'Player 8']
    x = [mmr_to_rank(mmr) for mmr in all_mmr]
    colors = cl.scales['8']['div']['RdYlGn']

    first = go.Bar(x=x, y=input.T[0], name='First', marker={'color': colors[7]})
    second = go.Bar(x=x, y=input.T[1], name='Second', marker={'color': colors[6]})
    third = go.Bar(x=x, y=input.T[2], name='Third', marker={'color': colors[5]})
    fourth = go.Bar(x=x, y=input.T[3], name='Fourth', marker={'color': colors[4]})
    fifth = go.Bar(x=x, y=input.T[4], name='Fifth', marker={'color': colors[3]})
    sixth = go.Bar(x=x, y=input.T[5], name='Sixth', marker={'color': colors[2]})
    seventh = go.Bar(x=x, y=input.T[6], name='Seventh', marker={'color': colors[1]})
    eigth = go.Bar(x=x, y=input.T[7], name='Eigth', marker={'color': colors[0]})

    data = [first, second, third, fourth, fifth, sixth, seventh, eigth]
    layout = go.Layout(
        barmode='group',
        title='All Even',
        xaxis={'title': 'Lobby Ranks'},
        yaxis={'title': 'MMR Change'}
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='graphs/all_b1.html', auto_open=True)

def mmr_to_rank(mmr: int) -> str:
    mmr_level = int((mmr - 340) / 80)
    if mmr_level == 37:
        return "King"
    if mmr_level == 38:
        return "Queen"

    map = ["Pawn", "Knight", "Bishop", "Rook"]
    i = int((mmr_level - 1) / 9)
    x = mmr_level % 9
    x = 9 if x == 0 else x
    return "{}-{}".format(map[i], x)


def placements(avg_mmr: int, mmr: int) -> Array[int, 8]:
    out = ((avg_mmr - mmr) * COEFF + CONST).astype(int)
    out[0] = max(out[0], 15)
    out[7] = min(out[7], -15)
    return out

def all_placements(all_mmr: Array[int, 8]) -> Array[int, 8, 8]:
    avg_mmr = all_mmr.mean()
    out = np.array([placements(avg_mmr, mmr) for mmr in all_mmr])
    return out


def main():
    print('Getting mmr')
    all_mmr = np.loadtxt('input.txt')
    data = all_placements(all_mmr)

    print('Making graph')
    bar_chart(data, all_mmr)

if __name__ == '__main__':
    main()
