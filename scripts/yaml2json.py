# convert yaml to json
# pip3 install pyyaml
# http://pyyaml.org/wiki/PyYAMLDocumentation
# py3 yaml2json.py < ~/code/manpow/homeland/heartland/puphpet/config.yaml
# gist https://gist.github.com/noahcoad/51934724e0896184a2340217b383af73

import json
import sys
import yaml


# See: http://stackoverflow.com/a/25895504
def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

yml = yaml.load(sys.stdin)

sys.stdout.write(json.dumps(yml,
    sort_keys=True,
    indent=2,
    default=date_handler))
