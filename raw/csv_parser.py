import csv
from collector import Artifact, collect

raw_artifacts = "./RAW_ITEMS_ARTIFACTS.csv"
raw_cyphers = "./RAW_ITEMS_CYPHERS.csv"
raw_oddities = "./RAW_ITEMS_ODDITIES.csv"

ARTIFACTS = {}
CYPHERS = {}
ODDITIES = {}

collect(raw_artifacts, ARTIFACTS, Artifact)

print(ARTIFACTS)
