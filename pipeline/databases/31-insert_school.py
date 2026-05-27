#!/usr/bin/env python3
"""insert documents"""


def insert_school(mongo_collection, **kwargs):
    """insert documents"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
