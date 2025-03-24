# Module 4 - SBOM

**Goal**: Generate an SBOM

## Steps

1. Install cyclonedx-cli

```bash
pip install cyclonedx-bom
```

2. Run the tool to generate the SBOM. Remember to store `sbom.json` as an artifact

```bash
cyclonedx-py requirements -o bom.json
```
