def checkio(matrix):
    lists = [x for x in matrix]
    lists.extend([list(x) for x in zip(*matrix)])
    lists.extend([[matrix[y-x][x] for x in range(len(matrix)) if 0 <= y - x < len(matrix)] for y in range(2 * len(matrix) - 1)])
    lists.extend([[matrix[::-1][y-x][x] for x in range(len(matrix)) if 0 <= y - x < len(matrix)] for y in range(2 * len(matrix) - 1)])
    return check(lists)

def check(list):
    x = [i for i in list if len(i) >= 4]
    for i in x:
        while len(i) >= 4:
            if i[0] == i[1] == i[2] == i[3]:
                return True
                break
            else:
                i.pop(0)
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
