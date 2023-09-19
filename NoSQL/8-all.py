#!/usr/bin/env python3
"""Task 8"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """List all docs in collection"""
    return mongo_collection.find()