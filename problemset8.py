# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#


def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    result = {}
    inputFile = open(filename)
    for line in inputFile:
        key_value = line.split(',')
        result[key_value[0].strip()] = (int(key_value[1].strip()), int(key_value[2].strip()))

    return result


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2


def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#


def sort_compared(subjects, item_list, comparator):
    """
    Returns a list of subject keys sorted based on comparator. maximum first
    :param subjects: a dictionary of subjects (str -> (value, work))
    :param item_list: list of keys to compare
    :param comparator: caparator function
    :rtype: list
    """

    result = item_list.copy()

    j = 1
    while j < len(result):
        for i in range(len(result) - j):
            if not subjects[result[i]][WORK] <= subjects[result[i+1]][WORK]:
                temp = result[i]
                result[i] = result[i+1]
                result[i+1] = temp

        j += 1

    j = 1
    while j < len(result):
        for i in range(len(result) - j):
            if not comparator(subjects[result[i]], subjects[result[i+1]]):
                temp = result[i]
                result[i] = result[i+1]
                result[i+1] = temp

        j += 1

    return result


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

    result = {}
    subjects_copy = subjects.copy()
    remaining_work = maxWork
    possible = True

    while possible:
        possible_answers = list(filter(lambda x: subjects_copy[x][WORK] <= remaining_work, subjects_copy))
        if len(possible_answers) > 0:
            max_key = sort_compared(subjects_copy, possible_answers, comparator)[0]
            result[max_key] = subjects_copy[max_key]
            del subjects_copy[max_key]
            remaining_work -= result[max_key][WORK]

        else:
            possible = False

    return result


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects


def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#


def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#


def dp_val_advisor(subjects, sorted_items, maxWork, i, memory):

    if (sorted_items[i], maxWork) in memory:
        return memory[(sorted_items[i], maxWork)]

    if i == 0:
        if subjects[sorted_items[i]][WORK] > maxWork:
            memory[(sorted_items[i], maxWork)] = 0
            return 0
        else:
            memory[(sorted_items[i], maxWork)] = subjects[sorted_items[i]][VALUE]
            return subjects[sorted_items[i]][VALUE]

    without_i = dp_val_advisor(subjects, sorted_items, maxWork, i - 1, memory)
    if subjects[sorted_items[i]][WORK] > maxWork:
        memory[(sorted_items[i], maxWork)] = without_i
        return without_i
    else:
        with_i = subjects[sorted_items[i]][VALUE] \
                 + dp_val_advisor(subjects, sorted_items, maxWork - subjects[sorted_items[i]][WORK], i - 1, memory)
        result = max(without_i, with_i)
        memory[(sorted_items[i], maxWork)] = result
        return result


def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    possible_answers = list(filter(lambda x: subjects[x][WORK] <= maxWork, subjects))
    possible_answers = sort_compared(subjects, possible_answers, cmpValue)
    memory = {}
    dp_val_advisor(subjects, possible_answers, maxWork, len(possible_answers) - 1, memory)

    # Find path to the best answer
    available_work = maxWork
    path = []
    for i in range(len(possible_answers)-1, 0, -1):
        bottom_branch = dp_val_advisor(subjects, possible_answers, available_work, i, memory)
        top_branch = dp_val_advisor(subjects, possible_answers, available_work, i-1, memory)
        if bottom_branch != top_branch:
            path.append(possible_answers[i])
            available_work -= subjects[possible_answers[i]][WORK]

    return {key: subjects[key] for key in path}

#
# Problem 5: Performance Comparison
#


def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.


if __name__ == '__main__':
    # s = {'6.00': (16, 8),  '1.00': (7, 7), '6.01': (5, 3), '15.01': (9, 6)}
    s = loadSubjects(SUBJECT_FILENAME)
    print(greedyAdvisor(s, 9, cmpValue))
    # print(greedyAdvisor(s, 15, cmpWork))
    # print(greedyAdvisor(s, 15, cmpRatio))
    print(bruteForceAdvisor(s, 9))
    print(dpAdvisor(s, 9))

