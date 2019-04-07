from lib import all_placements, bar_chart

import numpy as np

def main():
    print('Getting mmr')
    all_mmr = np.loadtxt('input.txt')
    data = all_placements(all_mmr)

    print('Making graph')
    bar_chart(data, all_mmr)

if __name__ == '__main__':
    main()
