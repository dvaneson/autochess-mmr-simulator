from lib import all_placements, bar_chart

import numpy as np

def main():
    print('Getting mmr')
    all_mmr = np.loadtxt('input.txt')
    for row in all_mmr:
        data = all_placements(row)

        print(f"Making graph for {row}")
        bar_chart(data, row)

if __name__ == '__main__':
    main()
