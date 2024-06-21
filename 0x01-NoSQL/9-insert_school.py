#!/usr/bin/env python3
"""Module that defines a function that runs a mongo query"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new documents in a collection


    # return list(mongo_collection.find({}))
    # query = ""
    # for k, v in kwargs.items():
    # query += '{{\"{}\" : \"{}\"}},'.format(a, b)
    """

    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
