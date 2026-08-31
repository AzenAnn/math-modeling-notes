from __future__ import annotations

import shutil

from _bootstrap import PROJECT_ROOT

root = PROJECT_ROOT
package_assets = root / "modeling_mastery" / "assets"

for name in ["schemas", "templates", "references"]:
    destination = package_assets / name
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(root / name, destination)

skills_destination = package_assets / "skills"
if skills_destination.exists():
    shutil.rmtree(skills_destination)
skills_destination.mkdir(parents=True)

orchestrator = skills_destination / "modeling-mastery"
orchestrator.mkdir(parents=True)
shutil.copy2(root / "SKILL.md", orchestrator / "SKILL.md")
orchestrator_references = orchestrator / "references"
orchestrator_references.mkdir(parents=True)
shutil.copy2(
    root / "references" / "paper-workspace.md",
    orchestrator_references / "paper-workspace.md",
)
for child in sorted((root / "skills").iterdir()):
    if child.is_dir() and (child / "SKILL.md").exists():
        shutil.copytree(child, skills_destination / child.name)

print(package_assets)
