import colorlover as cl
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

import numpy as np
from nptyping import Array

def bar_chart(input: Array[int,8,8], all_mmr: Array[int, 8]):
    x = np.array([mmr_to_rank(mmr) for mmr in all_mmr])
    places = ['First', 'Second', 'Thrid', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eight']
    colors = cl.scales['8']['div']['RdYlGn']
    colors.reverse()

    data = [go.Bar(x=x, y=y, name=places[i], marker={'color': colors[i]}) for i,y in enumerate(input.T)]
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

def title_and_filename(x: Array[str, 8]) -> (str, str):
    pass
