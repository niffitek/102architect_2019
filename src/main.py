#! /usr/bin/env python3

import math
import argparse
import sys


def translation(point, arg1, arg2):
    try:
        new_point = [0] * 2
        new_point[0] = point[0] + arg1
        new_point[1] = point[1] + arg2
        return (new_point)
    except exit(84):
        exit(84)


def scaling(point, arg1, arg2):
    try:
        new_point = [0] * 2
        new_point[0] = point[0] * arg1
        new_point[1] = point[1] * arg2
        return (new_point)
    except exit(84):
        exit(84)


def rotation(point, arg1):
    try:
        new_point = [0] * 2
        new_point[0] = point[0] * math.cos(math.radians(arg1)) - point[1] * math.sin(math.radians(arg1))
        new_point[1] = point[0] * math.sin(math.radians(arg1)) + point[1] * math.cos(math.radians(arg1))
        return (new_point)
    except exit(84):
        exit(84)


def mat_rot(arg):
    try:
        mat = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        mat[0] = math.cos(math.radians(arg))
        mat[1] = -math.sin(math.radians(arg))
        mat[3] = math.sin(math.radians(arg))
        mat[4] = math.cos(math.radians(arg))
        return (mat)
    except exit(84):
        exit(84)


def reflection(point, arg):
    try:
        new_point = [0] * 2
        new_point[0] = point[0] * math.cos(math.radians(2 * arg)) + point[1] * math.sin(math.radians(2 * arg))
        new_point[1] = point[0] * math.sin(math.radians(2 * arg)) - point[1] * math.cos(math.radians(2 * arg))
        return (new_point)
    except exit(84):
        exit(84)


def mat_ref(arg):
    try:
        mat = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        mat[0] = math.cos(math.radians(2 * arg))
        mat[1] = math.sin(math.radians(2 * arg))
        mat[3] = math.sin(math.radians(2 * arg))
        mat[4] = -math.cos(math.radians(2 * arg))
        return (mat)
    except exit(84):
        exit(84)


def mult(mat_og, mat2):
    try:
        matrix = mat_og
        matrix[0] = mat_og[0] * mat2[0] + mat_og[1] * mat2[3] + mat_og[2] * mat2[6]
        matrix[1] = mat_og[0] * mat2[1] + mat_og[1] * mat2[4] + mat_og[2] * mat2[7]
        matrix[2] = mat_og[0] * mat2[2] + mat_og[1] * mat2[5] + mat_og[2] * mat2[8]
        matrix[3] = mat_og[3] * mat2[0] + mat_og[4] * mat2[3] + mat_og[5] * mat2[6]
        matrix[4] = mat_og[3] * mat2[1] + mat_og[4] * mat2[4] + mat_og[5] * mat2[7]
        matrix[5] = mat_og[3] * mat2[2] + mat_og[4] * mat2[5] + mat_og[5] * mat2[8]
        return (matrix)
    except exit(84):
        exit(84)


def input():
    try:
        matrix = [1, 0, 0, 0, 1, 0, 0, 0, 1]
        parser = argparse.ArgumentParser(description='102architect')
        parser.add_argument('point', type=int, nargs=2,
                            help='original point (x, y)')
        parser.add_argument('-t', dest='t', action='store', type=int, nargs=2,
                            help='translation along vector (i, j)')
        parser.add_argument('-z', dest='z', action='store', type=int, nargs=2,
                            help='scaling by factors m (x-axis) and n (y-axis)')
        parser.add_argument('-r', dest='r', action='store', type=int, nargs=1,
                            help='rotation centered in O by a d degree angle')
        parser.add_argument('-s', dest='s', action='store', type=int, nargs=1,
                            help='reflection over the axis passing through O with an inclination angle of d degrees')
        try:
            args = parser.parse_args()
        except exit(84):
            sys.exit(84)
        if len(sys.argv) == 3:
            exit(84)
        point = [0] * 2
        point[0] = int(sys.argv[1])
        point[1] = int(sys.argv[2])
        og_point = point
        for i in range(3, len(sys.argv)):
            if sys.argv[i] == '-t':
                matrix[2] += int(sys.argv[i + 1])
                matrix[5] += int(sys.argv[i + 2])
                print("Translation along vector (%s, %s)" % (sys.argv[i + 1], sys.argv[i + 2]))
                point = translation(point, int(sys.argv[i + 1]), int(sys.argv[i + 2]))
            elif sys.argv[i] == '-z':
                for j in range(0, 3):
                    matrix[j] *= int(sys.argv[i + 1])
                for j in range(3, 6):
                    matrix[j] *= int(sys.argv[i + 2])
                print("Scaling by factors %s and %s" % (sys.argv[i + 1], sys.argv[i + 2]))
                point = scaling(point, int(sys.argv[i + 1]), int(sys.argv[i + 2]))
            elif sys.argv[i] == '-r':
                print("Rotation by a %s degree angle" % sys.argv[i + 1])
                point = rotation(point, int(sys.argv[i + 1]))
                tmp_mat = mat_rot(float(sys.argv[i + 1]))
                print("%.2f\t%.2f\t%.2f" % (tmp_mat[0], tmp_mat[1], tmp_mat[2]))
                print("%.2f\t%.2f\t%.2f" % (tmp_mat[3], tmp_mat[4], tmp_mat[5]))
                matrix = mult(tmp_mat, matrix)
                print("%.2f\t%.2f\t%.2f" % (matrix[0], matrix[1], matrix[2]))
                print("%.2f\t%.2f\t%.2f" % (matrix[3], matrix[4], matrix[5]))
            elif sys.argv[i] == '-s':
                print("Reflection over an axis with an inclination angle of %s degrees" % sys.argv[i + 1])
                point = reflection(point, int(sys.argv[i + 1]))
                tmp_mat = mat_ref(float(sys.argv[i + 1]))
                matrix = mult(tmp_mat, matrix)
        for i in range(0, 6):
            if 0 > matrix[i] > -0.005:
                matrix[i] *= -1
        print("%.2f\t%.2f\t%.2f" % (matrix[0], matrix[1], matrix[2]))
        print("%.2f\t%.2f\t%.2f" % (matrix[3], matrix[4], matrix[5]))
        print("0.00\t0.00\t1.00")
        print("(%.2f, %.2f) => (%.2f, %.2f)" % (og_point[0], og_point[1], point[0], point[1]))
        exit(0)
    except ValueError:
        exit(84)


input()