propublica
==========
Minimal python wrapper for [Propublica's Congress API](https://www.propublica.org/datastore/api/propublica-congress-api)

Currently setup to return 20 [bills recently introduced in the house](https://propublica.github.io/congress-api-docs/?shell#bills) with select traits (eg title, id, recent actions) but planning to expand for additional data features.

Requires: your own API key from Propublica.
In a separate file in cwd, save your key as
```
key = "SJ82ja8HH733D82jfndjsHKD" #not a real key
```
and import/reference this from your program.
