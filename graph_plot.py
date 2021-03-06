import argparse
import os

import matplotlib.pyplot as plt


def get_output_filename(inp_fname):
    return inp_fname.replace('output', 'graph.png')


def get_x_value(graph_type, x):
    if graph_type == "trials":
        return int(x[11:-1])
    elif graph_type == "initpolicy":
        return int(x[21:-1])
    elif graph_type == "maxiter":
        return int(x[12: -1])
    elif graph_type == "revert":
        return int(x[11:-1])
    elif graph_type == "target":
        return int(x[11:-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("graph_type", help="type of graphs (eg., cweights, trials etc)", type=str)
    parser.add_argument("inp_file", help="input file whose data should be plotted", type=str)
    args = parser.parse_args()

    with open(args.inp_file, mode='r', encoding='utf-8') as input_file:
        file_content = input_file.readlines()

    x_vals = list()
    y_vals = list()
    for line in file_content:
        x, y = line.strip().split(' ')
        x_vals.append(get_x_value(args.graph_type, x))
        # x_vals.append(x)
        y_vals.append(y)

    for a, b in zip(x_vals, y_vals):
        print(a, b)

    plt.plot(x_vals, y_vals, marker='o')
    plt.xlabel('{} setting'.format(args.inp_file))
    plt.ylabel('Colors Differences')
    fig = plt.gcf()
    plt.show()
    # fig.savefig('{}.png'.format(args.inp_file), dpi=100)
    fig.savefig(get_output_filename(args.inp_file))

if __name__ == '__main__':
    main()
