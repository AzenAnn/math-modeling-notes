# Third-party integrations

Modeling-Mastery 只提供适配层，不分发下列项目的模型权重或源代码：

- MinerU: https://github.com/opendatalab/MinerU
- Docling: https://github.com/docling-project/docling
- Obsidian: https://obsidian.md/
- Claude Code Agent Skills documentation: https://code.claude.com/docs/en/skills

集成点：

- MinerU CLI: `mineru -p <input_path> -o <output_path>`，可追加 `-b pipeline`。
- Docling Python: `DocumentConverter().convert(source).document.export_to_markdown()` 与 `export_to_dict()`。
- Obsidian: 直接写入 Markdown、YAML frontmatter、Wikilink 和本地索引文件，不依赖私有 API。

请在生产或商业部署前复核每个依赖的当前许可证和模型使用条款。
