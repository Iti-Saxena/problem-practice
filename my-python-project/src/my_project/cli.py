# CLI for My Project

import argparse

def main():
    parser = argparse.ArgumentParser(description='Command-line interface for My Project.')
    parser.add_argument('--option', type=str, help='An example option for the CLI.')
    
    args = parser.parse_args()
    
    if args.option:
        print(f'Option provided: {args.option}')
    else:
        print('No option provided. Use --option to specify one.')

if __name__ == '__main__':
    main()