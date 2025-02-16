from collector import Artifact, Cypher, Oddity, Collector

raw_artifacts = "./RAW_ITEMS_ARTIFACTS.csv"
raw_cyphers = "./RAW_ITEMS_CYPHERS.csv"
raw_oddities = "./RAW_ITEMS_ODDITIES.csv"

ARTIFACTS = Collector(raw_artifacts, Artifact)
CYPHERS = Collector(raw_cyphers, Cypher)
ODDITIES = Collector(raw_oddities, Oddity)

if __name__ == "__main__":
    assert len(ARTIFACTS.collection) == 300, "Artifact collection failed"
    assert len(CYPHERS.collection) == 500, "Cypher collection failed"
    assert len(ODDITIES.collection) == 400, "Oddity collection failed"
