#!/usr/bin/env python3
"""A module a does insertion of documents"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """a function that inserts a new document"""
    return mongo_collection.insert(kwargs)
