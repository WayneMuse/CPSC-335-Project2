from alg1 import find_target_indices
from alg2 import run_length_encode
from alg3 import merge_sorted_arrays


def load_algo1_inputs():
    return [
        ("sanoaklandrialtofullertonmarcolongbreacoronamodestoclovissimithousand", ["brea", "modesto", "clovis", "corona"]),
        ("marcopolmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas", ["fullerton", "chino", "fremont", "fresno"]),
        ("torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange", ["oxnard", "irvine", "orange", "marco"]),
    ]


def load_algo2_inputs():
    return [
        "ddd",
        "heloooooooo there",
        "choosemeeky and tuition-free"
    ]


def load_algo3_inputs():
    return [
        [[2, 5, 9, 21], [-1, 0, 2], [-10, 81, 121], [4, 6, 12, 20, 150]],
        [[10, 17, 18, 21, 29], [-3, 0, 3, 7, 8, 11], [81, 88, 121, 131], [9, 11, 12, 19, 29]],
        [[-4, -2, 0, 2, 7], [4, 6, 12, 14], [10, 15, 25], [5, 6, 10, 20, 24]]
    ]


def main():
    print("======================================")
    print("- Algorithm 1: Target Substrings -\n")
    for i, (text, targets) in enumerate(load_algo1_inputs(), 1):
        indices, words = find_target_indices(text, targets)
        print(f"test {i} String:\n {text}")
        print(f"Test {i} Indices:\n {indices}")
        print(f"Test {i} Words:\n {words}\n")

    print("======================================")
    print("\n- Algorithm 2: Run-Length Encoding -\n")
    for i, s in enumerate(load_algo2_inputs(), 1):
        print(f"Test {i} Input: \n{s}")
        print(f"Test {i} Encoded: \n{run_length_encode(s)}\n")

    print("======================================")
    print("- Algorithm 3: Merging Sorted Arrays -\n")
    for i, arrays in enumerate(load_algo3_inputs(), 1):
        print(f"Test {i} Merged Output: \n{merge_sorted_arrays(arrays)}\n")



main()