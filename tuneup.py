#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import timeit
# import collections


def profile(func):
    """A function that can be used as a decorator to meausre performance"""
    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        prof.runcall(func, *args, **kwargs)
        prof.disable()
        sort_condition = 'cumulative'
        ps = pstats.Stats(prof).sort_stats(sort_condition)
        return ps.print_stats()

    return wrapper


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


# @profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    my_dictionary = {}
    for movie in movies:
        if movie in my_dictionary:
            my_dictionary[movie] += 1
        else:
            my_dictionary[movie] = 1
        if my_dictionary[movie] > 1 and movie not in duplicates:
            duplicates.append(movie)
    return duplicates
    # hmmm
    # ---------------Method below delivers ~0.05------------------
    # return [movie for n, movie in enumerate(movies) if movie in movies[:n]]
    #
    # -----Method below using collections delivered-------
    # return [movie for movie, count in collections.Counter(movies).items()
    #         if count > 1]
    # ---------orignal code delivers slowest 3.2 seconds-----------
    # while movies:
    #     movie = movies.pop()
    #     if is_duplicate(movie, movies):
    #         duplicates.append(movie)
    # return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES
#     t = timeit.timeit('find_duplicate_movies("movies.txt")',
#                       setup="from __main__ import find_duplicate_movies",
#                       number=10)
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup="from __main__ import find_duplicate_movies")

    process_repitions = 7
    sample_size = 3
    result = t.repeat(repeat=process_repitions, number=sample_size)
    return min(result)/sample_size


@profile
def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    print(timeit_helper())
    print(":)")


if __name__ == '__main__':
    main()
