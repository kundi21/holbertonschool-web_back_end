#!/usr/bin/env python3
"""
task 11
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    returns list
    """
    return mongo_collection.find({"topics": topic})