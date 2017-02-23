from jsonschema import validate
import jsonschema
import json
import yaml
import os

schema_relpath = 'scripts/jsonschema/schemas/popolo/organization.json'
schema_abspath = 'file://' + os.path.abspath(schema_relpath)

org_schema = json.load(open(schema_relpath, 'r'))

organizations = yaml.load(open('data/committees.yml', 'r'))

class patchedResolver(jsonschema.RefResolver):
    def __init__(self):
        jsonschema.RefResolver.__init__(self,
                base_uri = schema_abspath,
                referrer = None)
        self.store[schema_abspath] = org_schema

newResolver = patchedResolver()

for org in organizations:
    validate(org, org_schema, resolver=newResolver)
