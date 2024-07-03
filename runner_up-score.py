if __name__ == '__main__':
    n = int(input())  # Read the number of elements (not used further)
    arr = list(map(int, input().split()))  # Read the scores into a list of integers

    # Remove duplicates and sort in descending order
    unique_num = sorted(set(arr), reverse=True)

    # Check if there are at least two unique scores
    if len(unique_num) < 2:
        print("There is no runner up")
    else:
        # Retrieve the second maximum score
        second_max = unique_num[1]
        print(second_max)
