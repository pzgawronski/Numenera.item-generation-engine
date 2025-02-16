from collector import Collector
from item_classes import Artifact, Cypher, Oddity

raw_artifacts = "./RAW_ITEMS_ARTIFACTS.csv"
raw_cyphers = "./RAW_ITEMS_CYPHERS.csv"
raw_oddities = "./RAW_ITEMS_ODDITIES.csv"

_ARTIFACTS = Collector(raw_artifacts, Artifact)
_CYPHERS = Collector(raw_cyphers, Cypher)
_ODDITIES = Collector(raw_oddities, Oddity)

ARTIFACTS = _ARTIFACTS.collection
CYPHERS = _CYPHERS.collection
ODDITIES = _ODDITIES.collection

if __name__ == "__main__":
    assert len(_ARTIFACTS.collection) == 300, "Artifact collection failed"
    assert len(_CYPHERS.collection) == 500, "Cypher collection failed"
    assert len(_ODDITIES.collection) == 400, "Oddity collection failed"
