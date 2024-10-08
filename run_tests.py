# pyright: reportAny=false
from argparse import ArgumentParser

import pytest


def main():
    parser: ArgumentParser = ArgumentParser()

    _ = parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help=' Number of times to repeat the test(default = 1)'
    )

    _ = parser.add_argument(
        '-e', '--environment',
        choices=['staging', 'production', 'uat'],
        default='staging',
        help=' Choose environemnt (default = staging)'
    )

    _ = parser.add_argument(
        '--tb',
        choices=['auto', 'long', 'short', 'line', 'native', 'no'],
        default='short',
        help=' Choose traceback length (default = short)'
    )

    _ = parser.add_argument(
        '-f', '--file',
        help=' Specific test to run (default = None)'
    )

    _ = parser.add_argument(
        '--window',
        nargs='?',
        const='',
        help=' Choose to show driver opts (default = headless)'
    )

    _ = parser.add_argument(
        '-v',
        action='store_true',
        help=' Verbosity level 1 (default = none)',
    )
    _ = parser.add_argument(
        '-vv',
        help=' Verbosity level 2 (default = none)',
        action='store_true',
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

    if args.v:
        pytest_args.append('-v')
    elif args.vv:
        pytest_args.append('-vv')

    # this is not best prac
    for _ in range(args.count):
        _ = pytest.main(pytest_args)


if __name__ == '__main__':
    main()
