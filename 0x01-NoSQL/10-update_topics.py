#!/usr/bin/env python3
"""A module that changes topic of a school documwnt"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """a fumction that updates a document"""
    return mongo_collection.update({"name": name},
                                   {$set: {"topics": topics}})
