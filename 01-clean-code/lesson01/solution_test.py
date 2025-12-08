import types
from challenge import destroy_walls
# from solution import destroy_walls #test solution

def run_tests(task: types.FunctionType, test_inputs: list)-> list:
    if not isinstance(task, types.FunctionType):
        raise TypeError("param:task must be a function!")
    
    if not isinstance(test_inputs, list):
        raise TypeError("param:test_inputs must be a list!")
    if test_inputs is None:
        return []
    
    return task(test_inputs)

def present_results(results):
    cli_ui = f"{40*'='}\n{15*' '}TESTING ARENA{15*' '}\n{40*'='}"
    count = 1
    passed_num = 0
    failed_num = 0

    for input_data, expected_data, test_data, test_result in results:
        if test_result is True:
            passed_num += 1
        else:
            failed_num += 1
        message = "--------- Test Count ---------"
        message = f"\ninput:\t{input_data}\n"
        message += f"expected: {expected_data}\n"
        message += f"actual:\t{test_data}\n"
        message += f"status: {'Passed!' if test_result else 'Failed!'}"
        if count < len(results):
            message += "\n---------------------------------"
            count += 1
        cli_ui += message
    cli_ui += f"\n============= {'PASS' if not failed_num else 'FAIL'} ==============\nPassed: {passed_num}\nFailed: {failed_num}\n"

    print(cli_ui)

def main():
    # testing arena
    test_data = [
        [0, 20, 30],
        [10, 0, 40, 0],
        [0, 4, 2, 3, 0, 1],
        []
    ]
    test_data_expected = [
        [20, 30],
        [10, 40],
        [4,2,3,1],
        []
    ]
    test_data_actuals = [run_tests(task=destroy_walls, test_inputs=row) for row in test_data]
    test_results = [ test_data_actuals[index] == test_data_expected[index]  for index in range(len(test_data))]
    results = [(test_data[index], test_data_expected[index], test_data_actuals[index], test_results[index]) for index in range(len(test_data))]
    print(results)
    present_results(results)




if __name__ == "__main__":
    main()