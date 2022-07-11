import sys
sys.setrecursionlimit(1_000_000)

def solution():
    num_cows, num_cage = map(int, sys.stdin.readline().split())

    cow = []

    for i in range(num_cows):
        cow.append(list(map(int, sys.stdin.readline().split()))[1:])

    cage = [-1] * (num_cage+1)

    def dfs(person_idx):
        for book_num in cow[person_idx]:

            if check[book_num] is True:
                continue
            check[book_num] = True

            if cage[book_num] == -1 or dfs(cage[book_num]):
                cage[book_num] = person_idx
                return True
        return False

    for i in range(num_cows):
        check = [0] * (num_cage + 1)
        dfs(i)

    print(sum(1 if i != -1 else 0 for i in cage))


if __name__ == '__main__':
    solution()