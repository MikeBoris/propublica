propublica
==========
Minimal python wrapper for [Propublica's Congress API](https://www.propublica.org/datastore/api/propublica-congress-api)

Requires: your own API key from Propublica.
In a separate file in cwd, save your key as
```
key = "SJ82ja8HH733D82jfndjsHKD" #not a real key
```
and import/reference this from your program.

Output
======
Currently setup to return 20 [bills recently introduced in the house](https://propublica.github.io/congress-api-docs/?shell#bills) with select traits (eg title, id, recent actions) but planning to expand for additional data features.
```
python congress_api.py

H.R.1810
March 30, 2017
To amend the Internal Revenue Code of 1986 to allow deductions and credits relating to expenditures
in connection with marijuana sales conducted in compliance with State law.
Referred to the House Committee on Ways and Means.
March 30, 2017

H.R.1830
March 30, 2017
To amend the Internal Revenue Code of 1986 to provide that a deduction equal to fair market value sh
all be allowed for charitable contributions of literary, musical, artistic, or scholarly composition
s created by the donor.
Referred to the House Committee on Ways and Means.
March 30, 2017
```
