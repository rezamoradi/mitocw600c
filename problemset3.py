def count_sub_string_match(target, key):
    count = 0
    new_pos = 0
    pos = ()
    while target.find(key) > -1 and len(target) > 1:
        count += 1
        new_pos += target.find(key) + 1
        pos += (new_pos,)
        target = target[target.find(key) + 1:]

    return [count, pos]


def count_sub_string_match_recursive(target, key):
    if target.find(key) < 0:
        return 0
    else:
        return 1 + count_sub_string_match_recursive(target[target.find(key) + 1:], key)


def constrained_match_pair(starts1, starts2, mathch1_len):
    result = ()
    for start in starts1:
        if (start + mathch1_len + 1) in starts2:
            result += (start,)

    return result


def sub_string_match_one_sub(key, target):
    """search for all locations of key in target, with one substitution
    """
    all_answers = ()
    for miss in range(len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print('breaking key', key, 'into', key1, key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = count_sub_string_match(target, key1)[1]
        match2 = count_sub_string_match(target, key2)[1]
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrained_match_pair(match1, match2, len(key1))
        all_answers += filtered

        print('match1', match1)
        print('match2', match2)
        print('possible matches for', key1, key2, 'start at', filtered)

    return all_answers


def sub_string_match_exactly_one_sub(key, target):
    all_one_sub = sub_string_match_one_sub(key, target)
    exact_match = count_sub_string_match(target, key)[1]

    return set(all_one_sub) - set(exact_match)

if __name__ == "__main__":
    print(count_sub_string_match("atgacatgcacaagtatgcatatgacatgcacaagtatgcatatgacatgcacaagtatgcat", "atgc"))
    print(count_sub_string_match_recursive("atgacatgcacaagtatgcatatgacatgcacaagtatgcatatgacatgcacaagtatgcat", "atgc"))
    print(sub_string_match_one_sub('ATGC', 'ATGACATGCA'))
    print('=======================================')
    print(sub_string_match_exactly_one_sub('ATGC', 'ATGACATGCA'))

