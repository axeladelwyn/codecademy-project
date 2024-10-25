result = 1
call_stack = []
def sum_to_one(n):
    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        print(f"Push: n = {n}")
        print(f"Stack: {[ctx["n_value"] for ctx in call_stack]}")
        n -= 1
    print("\nBase CASE REACHED: n = 1")

    # Inwinding the call stack (simulating recursive returns)

    print("\nUnwinding call stack:")
    running_sum = result
    while len(call_stack) > 0:
        return_value = call_stack.pop()
        running_sum += return_value["n_value"]
        print(f"Pop: n = {return_value["n_value"]}")
        print(f"Running sum = {running_sum}")

    return running_sum

def test_sum_to_one():
    test_case = [4, 5, 1, 2]

    for n in test_case:
        print(f"\n{'='*40}")
        print(f"Testing sum_to_one({n})")
        result = sum_to_one(n)
        print(f"Final result: {result}")

        expected = sum(range(1, n + 1))
        print(f"Verification: sum(1..{n}) = {expected}")
        assert result == expected, f"Test failed for n={n}"



        
# Run the tests
if __name__ == "__main__":
    test_sum_to_one()