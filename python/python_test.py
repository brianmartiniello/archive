#!/usr/bin/python3

"""Test Module"""

# import glob
import os
# import re
import shutil
import sys
# import getopt
# import importlib

# Set path to file
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
SCRIPT_NAME = os.path.basename(SCRIPT_PATH)

# Set path to file
CURRENT_DIR = os.path.abspath(os.getcwd())


def rm_dir(output_dir):
    """ Function to remove directory """
    if os.path.exists(output_dir):
        print("\nRemoving output directory")
        shutil.rmtree(output_dir)


def usage():
    """ Function to print usage """
    bold = "\033[1m"
    reset = "\033[0;0m"
    # Note: Use the formatter.push_font() to set the NAME and SYNOPSIS to bold
    print("\n")
    print(bold + "NAME" + reset)
    print("\t " + SCRIPT_NAME +
          " - Script that generates graphml and pfs graphs\n")
    print(bold + "SYNOPSIS" + reset)
    print("\t hello_world_graphs.py -a -b <# beams> -o <output directory> " +
          "--noDiagram --noGraphml --noPfs --showLevels\n")
    print(bold + "DESCRIPTION" + reset)
    print("\t This script generates a graph.")
    print("   ")
    print("\t Note: --options for the individual graph options are " +
          "not provided to distinguish them from the")
    print("\t graph formatting options ")
    print(bold + "OPTIONS" + reset)
    print(bold + "\t -a" + reset)
    print("\t\t Specifies to disable graph partition")
    print(bold + "\t -b <# beams>" + reset)
    print("\t\t Specifies the number of beams to support")
    print(bold + "\t -o <output directory>" + reset)
    print("\t\t Specifies the path to output directory")
    print(bold + "\t --noDiagram" + reset)
    print("\t\t Specifies the output graphviz (gv) file to not be generated.")
    print(bold + "\t --noGraphml" + reset)
    print("\t\t Specifies the output graphml file to not be generated.")
    print(bold + "\t --noPFS" + reset)
    print("\t\t Specifies the output paraflow script file (.pfs) " +
          "to not be generated.")
    print(bold + "\t --showLevels" + reset)
    print("\t\t Inserts the level information into the diagram.")


#
# main
#
def main(argv):
    """ Function main """
    # num_beams = 0
    # output_dir = '.'
    # graph_partition = True

    # # Note: (--) versions of these arguments cannot be provided.
    # # They need to be distinguished from the graph formation options
    # # expected from generate_graph.
    # try:
    #     # Add the GDL options here so that including them on the
    #     # command line does not cause this to throw an exception
    #     # for unrecognized arguments.
    #     opts, args = getopt.getopt(argv, "ab:o:",
    #                 ["noDiagram", "noGraphml", "noPFS", "showLevels"])
    # except:
    #     why = sys.exc_info()[0]
    #     where = sys.exc_info()[1]
    #     print("Exception while getting options: " +
    #           str(why) + " " + str(where))
    #     usage()
    #     sys.exit(1)

    # for opt, arg in opts:
    #     if opt in ("-a"): # allocate by partition nodes
    #         graph_partition = False
    #     elif opt in ("-b"):
    #         num_beams = int(arg)
    #     elif opt in ("-o"):
    #         output_dir = arg

    # # Remove all arguments from sys.argv not used by generate graph.
    # # This is needed since the generateGraph call inspects the arguments
    # # to this application and any items outside its set of expected values
    # # results in an error.
    # for opt in argv :
    #     if not opt.startswith('--'):
    #         sys.argv.remove(opt)

    # # Convert output directory to absolute path
    # output_dir = os.path.abspath(output_dir)

    # Report
    print("Hello World! - Args (" + str(argv) + ")")


if __name__ == '__main__':
    main(sys.argv[1:])
