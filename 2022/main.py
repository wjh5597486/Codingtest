# Libraries
import json
import time
import sys

# Imported models
from model import Model, Model_2
from api_request import Communicator


def save_json(file_name, json_data):
    with open(file_name, "w") as file:
        json.dump(json_data, file)
        return 0


def open_json(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


def write_log(file_name, log):
    with open(file_name, "a") as file:
        file.write(log)
        return 0


def solution(config, problem: int, init: bool):
    """
    PARAMETERS AND MODEL SETTING
    """
    # Communicator - build model and method
    comm = Communicator(config["base_url"], config["token"], problem)
    get = comm.get_method
    put = comm.put_method
    post = comm.post_method

    # Model - call parameters
    parameters_saved = open_json("parameters.json")
    parameters = parameters_saved["problem" + str(problem)]
    # Model - build model
    model = Model(parameters, init) if problem==1 else Model_2(parameters, init)


    """
    IMPLEMENT
    """
    epoch = 10
    for i in range(epoch):
        res = get("/waiting_line")

        res = get("/game_result")

        print(f'\r round {i:03}/{epoch} ', end="")
    print(f'\r', end="")  # remove print

    """ 
    LOG and SAVE
    """

    # log and score
    log = model.get_log()
    score = get("/score")
    print(score)
    write_log("log.txt", f'[{problem}] {log} _ {str(score)}\r')



    # Save Mode
    # all parameters will be saved in 'parameters.json'
    # check the value 'save' below
    save = False
    if save:
        print("Do you want to save the parameters?[y/n]: ", end="")
        while True:
            ans = input()
            if ans == "y":
                new_parameters = model.get_parameters()
                parameters_saved["problem" + str(problem)] = new_parameters  # save at the problem
                save_json("parameters.json", parameters_saved)
                break
            elif ans == "n":
                break
            else:
                continue

    return


if __name__ == '__main__':

    start_time = time.time()
    config = {
        "token": "abe6714ee14403ec61610873c55d17dd",
        "base_url": "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
    }

    """
    implement solution.
    : set "init" True, if you want to use the init parameters in the model.
    """
    solution(config, problem=1, init=True)
    # solution(config, problem=2, init=True)


    # running-time checker
    running_time = int(time.time() - start_time)
    print(f'{running_time // 60} min {running_time % 60} sec')
