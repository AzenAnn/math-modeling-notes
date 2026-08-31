from __future__ import annotations

SCHEMA_VERSION = "1.0.0"
AUTO_BEGIN = "<!-- MM:BEGIN AUTO -->"
AUTO_END = "<!-- MM:END AUTO -->"
MANUAL_HEADING = "## 我的补充"
REGISTRY_DIR = ".modeling-mastery"
REGISTRY_FILE = "registry.json"
INDEX_JSON_FILE = "index.json"
INDEX_DB_FILE = "modeling_index.sqlite3"

PROVENANCE_VALUES = {
    "PAPER_EXPLICIT",
    "PAPER_DERIVED",
    "AI_INFERRED",
    "EXTERNAL_REFERENCE",
    "HEURISTIC",
}

VAULT_FOLDERS = {
    "home": "00_Home",
    "models": "10_Models",
    "algorithms": "20_Algorithms",
    "code": "30_Code-Recipes",
    "cases": "40_Competition-Cases",
    "papers": "50_Papers",
    "data": "60_Data-Processing",
    "visualization": "70_Visualization",
    "writing": "80_Writing",
    "inbox": "90_Inbox",
    "assets": "_assets",
}
