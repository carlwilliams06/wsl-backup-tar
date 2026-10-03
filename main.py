"""WSL Backup TAR — Export a WSL distro to a .tar file via the Windows wsl --export command."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='wsl_backup_tar',
        description='Export a WSL distro to a .tar file via the Windows wsl --export command.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('WSL Backup TAR')
    print('A distro snapshot on disk.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
