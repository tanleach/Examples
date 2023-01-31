#!/usr/bin/python

import argparse
import logging
import os
from datetime import datetime

# Helper function for making sure that the file name passed
# in through the commandline actually exists
def file_exists(file_name):
    if not os.path.isfile(file_name):
        raise argparse.ArgumentTypeError("{} does not exist".format(file_name))
    return file_name


def doWork(inFile, outFile):
    #Let's assume we are working with CSV Files and we want to load it into pandas

    # Read a CSV file into a Pandas DataFrame
    # df = pd.read_csv(inFile)
    df = pd.read_excel(inFile)

    #Do things to the dataframe

    # Save the DataFrame to an Excel file
    # df.to_csv(outFile, index=False)
    df.to_excel(outFile, index=False)

    return

if __name__ == '__main__':
    print("here")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=file_exists, help='Input File Name')
    parser.add_argument('-o', '--output', help='Name of output file. (If not provided, output file will be "--file/-f" + "epoch time in milliseconds"')
    args = parser.parse_args()

# Configure the logger
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Use the logger
    logging.debug('This is a debug message.')
    logging.info('This is an info message.')
    logging.warning('This is a warning message.')
    logging.error('This is an error message.')
    logging.critical('This is a critical message.')

    if args.output is None:
        epoch_seconds = int(datetime.now().timestamp())
        args.output = f'{args.input}_{epoch_seconds}'

    logging.info(args.input)
    logging.info(args.output)

    doWork(args.input, args.output)