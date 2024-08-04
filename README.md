# Structure

Data is _modelled_.

Autobot provides a framework for the execution of the data
modelling process that is strongly typed.

1. Retrieve data using a self-contained process.
2. Clean the data using reproducible DuckDB.
3. Persist the model using DuckDB.


# The "process"

Autobot organizes data modelling capabilities into _pipelines_.

Each pipeline represents a completely independent data-transformation process.
A pipeline has the following:

1. Tasks (DAG). each task has (up to) **one** input table and **one** output table.

The set of input tables used by initial tasks forms the dependencies of a pipeline, and the set of output tables exposed form the output of the pipeline.
These may be persisted into the **autobot** model.

Refreshing a model runs all pipelines with output tables to that model.

We need a thin wrapper around DuckDB so that it can be replaced by another SQL engine.

Pipelines should run in-process.
