import json
import os

from datetime import datetime


def read_metadata(filename):
    with open(filename, encoding='utf-8') as handle:
        headers = [next(handle) for x in range(13)]
    return json.loads(''.join(headers))

translators = os.listdir("translators")
translators = [t for t in translators if t.endswith('js') and t != 'RefWorks Tagged.js']
translators = sorted(translators)

translator_metadata = {}
for t in translators:
    metadata = read_metadata("translators/" + t)
    translator_metadata[t] = {
        'label': metadata['label'],
        'lastUpdated': metadata['lastUpdated']
    }

with open("data/translators.json", 'w', encoding='utf-8') as handle:
    print(translator_metadata)
    json.dump(translator_metadata, handle, ensure_ascii=False)