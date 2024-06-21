#!/usr/bin/env python3
"""Module that defines a function that runs a mongo query"""

def list_all(mongo_collection):
	"""
	Function that lists all documents in a collection
	"""

	return list(mongo_collection.find({}))	
