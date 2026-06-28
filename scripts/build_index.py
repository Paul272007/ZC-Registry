import json
import glob

def parse_version(v):
    parts = []
    for part in v.split('-')[0].split('.'):
        try:
            parts.append(int(part))
        except ValueError:
            parts.append(0)
    return tuple(parts)

index = {"packages": {}}

for filepath in glob.glob("packages/**/*.json", recursive=True):
    with open(filepath, "r") as f:
        pkg = json.load(f)
        name = pkg["name"]
        version = pkg["version"]

        if name not in index["packages"]:
            index["packages"][name] = {"latest": version, "versions": {}}
        else:
            current_latest = index["packages"][name]["latest"]
            if parse_version(version) > parse_version(current_latest):
                index["packages"][name]["latest"] = version

        pkg.pop("name", None)
        pkg.pop("version", None)

        index["packages"][name]["versions"][version] = pkg

with open("index.json", "w") as f:
    json.dump(index, f)
