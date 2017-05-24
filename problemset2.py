# to get n McNuggets with packs of size min, mid and max
def mcnuggets(n, min_pac, mid_pac, max_pac):
    if n < min_pac:
        return False
    for pac in [max_pac, mid_pac, min_pac]:
        if n % pac == 0:
            # print((n//pac) * (str(pac) + ','), end='')
            return True

    if mcnuggets(n - max_pac, min_pac, mid_pac, max_pac):
        # print(max_pac, end=',')
        return True
    elif mcnuggets(n - mid_pac, min_pac, mid_pac, max_pac):
        # print(mid_pac, end=',')
        return True
    elif mcnuggets(n - min_pac, min_pac, mid_pac, max_pac):
        print(min_pac, end=',')
        return True
    else:
        return False
    # return mcnuggets(n - max_pac, min_pac, mid_pac, max_pac, max_pac) or \
    #        mcnuggets(n - mid_pac, min_pac, mid_pac, max_pac, mid_pac) or \
    #        mcnuggets(n - min_pac, min_pac, mid_pac, max_pac, min_pac)


def max_unbuyable_mcnuggets(min_pac, mid_pac, max_pac):
    i = 1
    while i < 200:
        if not False in map(lambda x: mcnuggets(x, min_pac=min_pac, mid_pac=mid_pac, max_pac=max_pac), range(i, i+min_pac)):
            for j in range(i-1, i-min_pac-1, -1):
                if not mcnuggets(j, min_pac, mid_pac, max_pac):
                    return j
        i += min_pac


if __name__ == "__main__":
    print(max_unbuyable_mcnuggets(6, 9, 20))
    print(max_unbuyable_mcnuggets(5, 7, 13))
    print(max_unbuyable_mcnuggets(9, 13, 20))
