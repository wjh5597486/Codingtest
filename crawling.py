from bs4 import BeautifulSoup
import requests

def get_input_output(problem):
    response = requests.get("https://www.acmicpc.net/problem/"+problem)
    soup = BeautifulSoup(response.text, 'html.parser')

    input_ = []
    output_ = []

    for i in range(1, 10):
        input_data = soup.select(f'#sample-input-{i}')
        input_data = [line.get_text() for line in input_data]

        output_data = soup.select(f'#sample-output-{i}')
        output_data = [line.get_text() for line in output_data]

        if input_data:
            input_.append(input_data[0])
            output_.append(output_data[0])
        else:
            break

    return input_, output_