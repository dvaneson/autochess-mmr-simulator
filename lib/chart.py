import colorlover as cl
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

import numpy as np
from nptyping import Array

# Constants
PLACE = ['First', 'Second', 'Thrid', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth']
NUM = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'All']
COLOR = cl.scales['8']['div']['RdYlGn']
COLOR.reverse()

# Make a bar chart with the provided data
def bar_chart(input: Array[int,8,8], all_mmr: Array[int, 8]):
    x = np.array([mmr_to_rank(mmr) for mmr in all_mmr])

    title, filename = title_and_filename(x)
    data = [go.Bar(x=x, y=y, text=y,textposition='auto', name=PLACE[i], marker={'color': COLOR[i]}) for i,y in enumerate(input.T)]
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
    if mmr < 500:
        return "Pawn-1"
        
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
    unique, counts = np.unique(ranks, return_counts=True)
    # Handle differently if one of each rank
    if unique.size == ranks.size:
        bottom = unique[0]
        top = unique[-1]
        title = f"{bottom} to {top}"
        filename = f"graphs/{bottom[0]}{bottom[-1]}_to_{top[0]}{top[-1]}.html"
        return title, filename

    title = ''
    filename = ''
    for rank, count in zip(unique, counts):
        title = title + f"{NUM[count-1]} {rank}, "
        filename = filename + f"{NUM[count-1]}_{rank[0]+rank[-1]}_"

    # Remove extra , and _. Format filename
    title = title[:-2]
    filename = 'graphs/' + filename[:-1].lower() + '.html'

    return title, filename
