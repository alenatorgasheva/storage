import argparse
import os
import tempfile
import json


# Functions:
def reading(storage_path):
    """Reading data"""
    with open(storage_path, 'r') as f:
        data = json.load(f)
    return data


def writing(storage_path, data):
    """Writing data"""
    with open(storage_path, 'w') as f:
        json.dump(data, f)


def create_arguments():
    """Creating arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help='Key word', required=True)
    parser.add_argument("--val", help='Value of key word', required=False)
    args = parser.parse_args()
    return args


def key(args, data):
    """Printing data by key word (--key)"""
    if args.key in data:
        print(', '.join(data[args.key]))
    else:
        print(None)


def val(args, data):
    """Adding data (--val)"""
    if args.key in data:
        if not isinstance(data[args.key], list):
           data[args.key] = [data[args.key]]
        data[args.key].append(args.val)
    else:
        data[args.key] = list(args.val)


# Main:
def main():

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    data = reading(storage_path)
    args = create_arguments()

    # Doing actions:
    if not args.val:
        key(args, data)
    elif args.val:
        val(args, data)

    writing(storage_path, data)


main()
