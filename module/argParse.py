# -*- coding: utf-8 -*-
# @Author : KrystianLi
# @Github : https://github.com/KrystianLi

import time
from argparse import ArgumentParser

def parseArgs():
    date = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    parser = ArgumentParser()
    parser.add_argument("-t", "--target", required=False, type=str, help=f"Website Titile/company name")
    parser.add_argument("-f", "--file", dest="file", required=False, type=str, default="", help=f"Website Titile file")
    parser.add_argument("-s", "--delay", dest="delay", required=False, type=int, default=120, help=f"Request 5 delays (default 120s)")
    parser.add_argument("-o", "--output", dest="output", required=False, type=str, default=f"{date}", help="output file (default ./output/gDomain_{fileName}_{date}.csv)")
    return parser


