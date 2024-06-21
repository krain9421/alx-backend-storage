#!/usr/bin/env python3
"""Module that defines a function that runs a mongo query"""

def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics
    of a school document based on the name:
    """

    mongo_collection.update({"name": name}, {"$set": {"topics": topics}})	
