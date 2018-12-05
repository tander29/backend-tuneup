#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import timeit


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
    print('Reading file with improved code: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def read_movies_original(src):
    """Read a list of movie titles"""
    print('Reading file with original code: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


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


def find_duplicate_movies_orig(src):
    movies = read_movies_original(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


@profile
def timeit_helper_original():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES
    t = timeit.Timer(stmt='find_duplicate_movies_orig("movies.txt")',
                     setup="from __main__ import find_duplicate_movies_orig")
    process_repitions = 7
    sample_size = 3
    result = t.repeat(repeat=process_repitions, number=sample_size)
    answer = 'Original time across {} repeats of {} runs/repeat= {}'.format(
        process_repitions, sample_size, min(result)/sample_size)
    print
    return answer


@profile
def timeit_helper_improved():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup="from __main__ import find_duplicate_movies")
    process_repitions = 7
    sample_size = 3
    result = t.repeat(repeat=process_repitions, number=sample_size)
    answer = 'Improved time of {} repeats of {} runs/repeat= {}'.format(
        process_repitions, sample_size, min(result)/sample_size)
    print
    return answer


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    print(timeit_helper_original())
    print(timeit_helper_improved())
    print(":)")


if __name__ == '__main__':
    main()

