import sys
sys.setrecursionlimit(1_000_000)
def solution():
    num_case = int(input())
    for i in range(num_case):
        num_book, num_people = map(int, sys.stdin.readline().split())
        people = []
        for i in range(num_people):
            people.append(tuple(map(int, sys.stdin.readline().split())))

        book = [-1] * (num_book+1)

        def dfs(person_idx):
            (a, b) = people[person_idx]

            for book_num in range(a, b+1):

                if check[book_num] is True:
                    continue
                check[book_num] = True

                if book[book_num] == -1 or dfs(book[book_num]):
                    book[book_num] = person_idx
                    return True
            return False

        for i in range(num_people):
            check = [0] * (num_book + 1)
            dfs(i)

        print(sum(1 if i != -1 else 0 for i in book))


if __name__ == '__main__':
    solution()