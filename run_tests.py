from argparse import ArgumentParser
import pytest


def main():
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument(
        '-r', '--repeat',
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
    args = parser.parse_args()
    pytest_args: list[str] = ['-q']
    if args.environment:
        pytest_args.append(f'--environment={args.environment}')

    # this is not best prac

    for _ in range(args.repeat):
        pytest.main(pytest_args)


if __name__ == '__main__':
    main()
