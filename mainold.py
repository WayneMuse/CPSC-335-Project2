from alg1 import find_target_indices
from alg2 import run_length_encode
from alg3 import merge_sorted_arrays


def load_algo1_inputs():
    with open("in2a.txt", "r") as f:
        lines = f.read().splitlines()
    inputs = []
    for i in range(0, len(lines), 2):
        text = lines[i].strip().strip('[]"')
        targets_line = lines[i + 1].strip().strip('[]')
        targets = [t.strip().strip("'") for t in targets_line.split(',') if t.strip()]
        inputs.append((text, targets))
    return inputs


def load_algo2_inputs():
    with open("in2b.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]


def load_algo3_inputs():
    with open("in2c.txt", "r") as f:
        content = f.read()
    arrays = []
    current_array = []
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("Array_"):
            if current_array:
                arrays.append(current_array)
                current_array = []
        elif line.startswith("[") and line.endswith("]"):
            line_clean = line.strip("[]").replace("]", "").replace("[", "")
            if line_clean:
                try:
                    current_array.append([int(x.strip()) for x in line_clean.split(",") if x.strip()])
                except ValueError:
                    print(f"Warning: Skipped malformed line: {line}")
    if current_array:
        arrays.append(current_array)
    return arrays



def main():
    print("--- Algorithm 1: Target Substrings ---")
    for i, (text, targets) in enumerate(load_algo1_inputs(), 1):
        indices, words = find_target_indices(text, targets)
        print(f"Test {i} Input:\n {text}")
        print(f"Test {i} Indices:\n {indices}")
        print(f"Test {i} Words:\n {words}\n")

    print("\n--- Algorithm 2: Run-Length Encoding ---")
    for i, s in enumerate(load_algo2_inputs(), 1):
        print(f"Test {i} Input: \n{s}")
        print(f"Test {i} Encoded: \n{run_length_encode(s)}\n")

    print("--- Algorithm 3: Merging Sorted Arrays ---")
    for i, arrays in enumerate(load_algo3_inputs(), 1):
        print(f"Test {i} Merged Output: \n{merge_sorted_arrays(arrays)}\n")


if __name__ == "__main__":
    main()