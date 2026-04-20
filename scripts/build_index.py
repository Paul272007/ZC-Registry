import json
import glob

index = {"packages": {}}

for filepath in glob.glob("packages/**/*.json", recursive=True):
    with open(filepath, "r") as f:
        pkg = json.load(f)
        name = pkg["name"]
        version = pkg["version"]

        if name not in index["packages"]:
            index["packages"][name] = {"latest": version, "versions": {}}

        index["packages"][name]["versions"][version] = pkg

with open("index.json", "w") as f:
    json.dump(index, f, indent=2)

print("index.json successfully generated")
