#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Sarah Beverton with some help from Joseph's help session"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
            description="Perform transformation on input text.")
    parser.add_argument('-u', '--upper', help='convert text to uppercase',
                        action='store_true')
    parser.add_argument('-l', '--lower', help='convert text to lowercase',
                        action='store_true')
    parser.add_argument('-t', '--title', help='convert text to titlecase',
                        action='store_true')
    parser.add_argument('text', help='text to be manipulated',
                        type=str, nargs='+')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)

    """
    with open('USAGE') as f:
            expected_lst = f.read().splitlines()
            expected = '\n'.join(expected_lst)
    print(expected)
    """

    if not ns:
        parser.print_usage()
        sys.exit(1)

    echo_text = ' '.join(ns.text)

    if ns.upper:
        print(echo_text.upper())
    elif ns.lower:
        print(echo_text.lower())
    elif ns.title:
        print(echo_text.title())
    else:
        print(echo_text)


if __name__ == '__main__':
    main(sys.argv[1:])
