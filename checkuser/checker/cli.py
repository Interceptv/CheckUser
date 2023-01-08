import json

from checkuser.utils import base_cli
from checkuser.checker import check_user, kill_user
from checkuser.checker import CheckerUserManager

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
        json_string = json.dumps(check_user)
        print(json_string)

    if args.kill:
        kill_user(args.kill)
