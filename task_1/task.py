def find_unique_and_sort(numbers: list[int]) -> list[int]:
    return sorted(set(numbers))


test_list = [12123, 123, 123, 123, 123, 127]
print(type(find_unique_and_sort(test_list)))
