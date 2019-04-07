import colorlover as cl
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

import numpy as np
from nptyping import Array

# Make a bar chart with the provided data
def bar_chart(input: Array[int,8,8], all_mmr: Array[int, 8]):
    x = np.array([mmr_to_rank(mmr) for mmr in all_mmr])
    places = ['First', 'Second', 'Thrid', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth']
    colors = cl.scales['8']['div']['RdYlGn']
    colors.reverse()

    title, filename = title_and_filename(x)
    data = [go.Bar(x=x, y=y, name=places[i], marker={'color': colors[i]}) for i,y in enumerate(input.T)]
    layout = go.Layout(
        barmode='group',
        title=title,
        xaxis={'title': 'Lobby Ranks'},
        yaxis={'title': 'MMR Change'}
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename=filename, auto_open=True)

# Convert mmr to rank
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

# Generate a title and filename based on the ranks
def title_and_filename(ranks: Array[str, 8]) -> (str, str):
    numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
    unique, counts = np.unique(ranks, return_counts=True)

    title = ''
    filename = ''
    for rank, count in zip(unique, counts):
        title = title + "{count} {rank}, ".format(count=numbers[count-1], rank=rank)
        filename = filename + "{count}_{rank}_".format(count=numbers[count-1], rank=rank[0]+rank[-1])

    # Remove extra , and _. Format filename
    title = title[:-2]
    filename = 'graphs/' + filename[:-1].lower() + '.html'

    return title, filename
