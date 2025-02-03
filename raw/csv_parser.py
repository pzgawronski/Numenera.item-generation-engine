from collector import Artifact, Cypher, Oddity, collect

raw_artifacts = "./RAW_ITEMS_ARTIFACTS.csv"
raw_cyphers = "./RAW_ITEMS_CYPHERS.csv"
raw_oddities = "./RAW_ITEMS_ODDITIES.csv"

ARTIFACTS = collect(raw_artifacts, Artifact)
CYPHERS = collect(raw_cyphers, Cypher)
ODDITIES = collect(raw_oddities, Oddity)

if __name__ == "__main__":
    assert len(ARTIFACTS) == 300, "Artifact collection failed"
    assert len(CYPHERS) == 500, "Cypher collection failed"
    assert len(ODDITIES) == 400, "Oddity collection failed"
