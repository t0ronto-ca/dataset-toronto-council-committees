# Council Committees

| Automated Test Suite | Status |
|----------------------|--------|
| Data Validation      | [![Build Status](https://travis-ci.org/t0ronto-ca/dataset-toronto-council-committees.svg?branch=master)](https://travis-ci.org/t0ronto-ca/dataset-toronto-council-committees) |

A dataset containing current committee data for Toronto City Hall

## Data

[**`data/committees.yml`**](data/committees.yml). Defines all City of
Toronto committees, validated against [Open Civic Data spec for
organizations](https://opencivicdata.readthedocs.io/en/latest/data/organization.html).

## Scripts

Run `make` in project root to see available scripts to run.

```
$ make
Usage: make <command>

where <command> is one of the following:

validate             Validate data
json                 Generate JSON from YAML
dummy                Perform a dummy action with outputs
```

## License

See [LICENSE.md](LICENSE.md).
