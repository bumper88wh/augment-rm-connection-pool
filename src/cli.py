# Main CLI entry point
import argparse

def build_parser():
    parser = argparse.ArgumentParser(prog='app')
    parser.add_argument('paths', nargs='+')
    parser.add_argument('--write', action='store_true')
    return parser

def main():
    args = build_parser().parse_args()
    print('processing', args.paths)

if __name__ == '__main__':
    main()
