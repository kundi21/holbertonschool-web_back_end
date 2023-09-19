#!/usr/bin/env python3
"""
task 9
"""

def insert_school(mongo_collection, **kwargs):
    """Insert doc in collection"""

    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id