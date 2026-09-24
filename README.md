# DM Vault

A Wikipedia-style reader for your Markdown campaign notes, made for game masters: stat blocks, initiative,
dice, weather, pinned notes and a screen for the players. It runs entirely in the browser: your notes stay
on your computer.

- **Use it online:** open DM Vault on its website, then *Open my campaign folder* or *Try the example campaign*.
- **Download everything:** the latest [release](../../releases/latest) contains `dm-vault.html` and a ready-to-use
  campaign folder (an example chapter and the 2024 SRD bestiary). Unzip, open `dm-vault.html`, pick the `Campaign` folder.

## What is in this repository

| Path | What it is |
|---|---|
| `dm-vault.html` | The whole tool, in one file |
| `demo/` | The example campaign opened by *Try the example campaign* (`demo/index.md` is its main page) |
| `tools/make-manifest.py` | Writes `demo/manifest.json`, the list of the files of the example |
| `.github/workflows/pages.yml` | Publishes the repository on GitHub Pages (and runs the script above) |

## Credits

The monsters and conditions in `demo/Monsters` and `demo/Rules` include material from the System Reference
Document 5.2 ("SRD 5.2") by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd, licensed under
the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/legalcode).
They were converted from the 5e-database project (https://github.com/5e-bits/5e-database, MIT License).
See `demo/About the SRD.md`.
