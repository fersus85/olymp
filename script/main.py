import logging
from pathlib import Path

from script.modules import load_competitors_from_json, load_results_from_txt
from script.modules import calculate_durations, generate_output
from script.modules import display_output, save_results_in_json

from script.logging_config import setup_logging


def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting app")

    try:
        competitors_path = Path("script/competitors_data/competitors2.json")
        results_path = Path("script/competitors_data/results_RUN.txt")

        competitors = load_competitors_from_json(competitors_path)
        results = load_results_from_txt(results_path)

        durations = calculate_durations(results=results)
        output = generate_output(competitors=competitors, durations=durations)

        display_output(data=output)
        save_results_in_json(results=output, path="output.json")
    except Exception as ex:
        logger.exception("Unexpected error in main: %s", ex, exc_info=True)


if __name__ == "__main__":
    main()
