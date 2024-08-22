import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Enter a temperature to convert. First argument = temp. Second argument = starting units. Third argument = ending units.'
    )

    parser.add_argument("--temp_input", required=True, type=int)
    parser.add_argument("--scale_from", required=True, type=str)
    parser.add_argument("--scale_to", required=True, type=str)

    args = parser.parse_args()

    temp_input = args.temp_input
    scale_from = args.scale_from
    scale_to = args.scale_to

    print(convert_temperature(temp_input, scale_from, scale_to))