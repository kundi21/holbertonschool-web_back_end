#!/usr/bin/env python3
""" Task 10 """
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a
    school document based on the name
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count