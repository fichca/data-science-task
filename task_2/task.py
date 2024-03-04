def dot(first_vector: [int], second_vector: [int]) -> int:
    result = 0
    for index in range(len(first_vector)):
        result += first_vector[index] * second_vector[index]

    return result


def norm(vector: [int]) -> int:
    result = 0
    for val in vector:
        result += val ** 2

    return result ** 0.5


def show_cosine_distance(first_vector: [int], second_vector: [int]):
    if len(first_vector) != len(second_vector):
        print("err: vectors of different lengths.")
        return

    dot_val = dot(first_vector, second_vector)
    first_norm = norm(first_vector)
    second_norm = norm(second_vector)

    if first_norm == 0 or second_norm == 0:
        print("err: norm is 0")
        return

    cosine_distance = dot_val / (first_norm * second_norm)
    print("Cosine distance: ", cosine_distance)


a = [23, 34]
b = [0, 1]

show_cosine_distance(a, b)
