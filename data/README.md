# Datasets del projecte

## Estructura

- `raw/`: datasets originals o descarregats.
- `processed/`: datasets derivats, nets o transformats.

## Criteri

- Posa a `data/raw/` els fitxers que facis servir per practicar amb scripts.
- Posa a `tests/data/` només fitxers petits pensats per a proves automatitzades.

## Exemple

L'script `src/python-proves/exemple_lectura_dataset.py` llegeix el fitxer
`data/raw/punts_exemple.csv` fent servir `pathlib` i una ruta relativa al
directori arrel del projecte.
