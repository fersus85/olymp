from read_input import load_competitors_from_json, load_results_from_txt
from generate_output import calculate_durations, generate_output
from display_and_save import display_output, save_results_in_json


def main():
    competitors = load_competitors_from_json('competitors2.json')
    results = load_results_from_txt('results_RUN.txt')
    durations = calculate_durations(results=results)
    output = generate_output(competitors=competitors, durations=durations)
    display_output(data=output)
    save_results_in_json(results=output, path='output.json')


if __name__ == '__main__':
    main()
