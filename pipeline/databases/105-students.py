#!/usr/bin/env python3
"""returns sorted score"""


def top_students(mongo_collection):
    """returns sorted score"""
    return list(mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "scores": 1,
                "averageScore": { "$avg": "$scores.score" }
            }
        },
        {"$sort": {"averageScore": -1}}
    ]))
