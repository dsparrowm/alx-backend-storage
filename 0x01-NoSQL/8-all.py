#!/usr/bin/env python3
"""Python function that lists all documents in a collection:"""
import pymongo


def list_all(mongo_collection):
    """return all docs in collection"""
    if mongo_collection is None:
        return []
    result = mongo_collection.find()
    return [doc for doc in result]
