#!/usr/bin/env python3
"""returns the list"""


def schools_by_topic(mongo_collection, topic):
    """returns the list"""
    return list(mongo_collection.find({"topics": topic}))
