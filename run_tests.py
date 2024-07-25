from argparse import ArgumentParser

import pytest


def main():
    parser: ArgumentParser = ArgumentParser()

    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of times to repeat the test(default = 1)'
    )

    parser.add_argument(
        '-e', '--environment',
        choices=['staging', 'production'],
        default='staging',
        help='Choose environemnt (default = staging)'
    )

    parser.add_argument(
        '--tb',
        choices=['auto', 'long', 'short', 'line', 'native', 'no'],
        default='short',
        help='Choose traceback length (default = short)'
    )

    parser.add_argument(
        '-f', '--file',
        help='Specific test to run (default = None)'
    )

    # TODO: decide if I want to add -w for ease of use
    parser.add_argument(
        '--window',
        nargs='?',
        const='',
        help='Choose to show driver opts (default = headless)'
    )

    args = parser.parse_args()
    pytest_args: list[str] = ['-rs']

    if args.environment:
        pytest_args.append(f'--environment={args.environment}')

    if args.tb:
        pytest_args.append(f'--tb={args.tb}')

    if args.file:
        pytest_args.insert(0, args.file)

    if args.window is not None:
        pytest_args.append(f'--window={args.window}')

    # this is not best prac
    for _ in range(args.count):
        pytest.main(pytest_args)


if __name__ == '__main__':
    main()
