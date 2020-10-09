# Time Complexity: order of n^2
def find_addition_pair(arr, result):
    for i in range(0, len(arr)-1):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == result:
                print(f"numbers are {arr[i]} and {arr[j]}")


# Time Complexity: Linear Time (n)
def find_addition_pair2(arr, result):
    pair = {}
    for index, value in enumerate(arr):
        if result-value in pair:
            print(f"number are {arr[pair.get(result-value)]} and {arr[index]}")
            return
        pair[value] = index
    print("Not Found")


if __name__ == "__main__":
    find_addition_pair2([10, 20, 30, 40], 50)
    print("Hello")
