import json

from scannycheck.utils import base_cli
from scannycheck.checker import check_user, kill_user
from scannycheck.checker import CheckerUserManager

base_cli.add_argument(
    '--check',
    '-c',
    type=str,
    help='Check user',
)

base_cli.add_argument(
    '--kill',
    '-k',
    type=str,
    help='Kill user',
)


def args_handler(args):
    if args.check:
        print(json.dumps(check_user(args.check), indent=4))

    if args.kill:
        kill_user(args.kill)
