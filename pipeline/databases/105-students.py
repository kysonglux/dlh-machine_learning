#!/usr/bin/env python3
"""returns sorted score"""


def top_students(mongo_collection):
    """returns sorted score"""
    return list(mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]))
