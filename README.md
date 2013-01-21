COMP400
=======

Representation of graph databases optimized for k-th neighbour search on large graphs stored on hard disk

This is the official repository for my McGill COMP-400 project course on database systems. We are trying to optimize a very specific type of queries that often appears in social networks with large social graphs called k-th neighbour search queries. In Facebook, for example, this type of query would correspond to a query such as :

- Who are my friends (1st neighbour search)?
- Who are the friends of my friends and their friends (3rd neighbour search)?

The approach would be to profile such queries done using SQL and try to build to build a custom system that can answer these queries faster.

Jules
