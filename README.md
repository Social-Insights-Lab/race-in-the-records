# Race in the Record

Code, data, and model outputs for **Race in the Record: Measuring Racial Signal and Model Inference in Police Arrest Narratives** (Dutta\*, Forsyth\*, Robertson, KhudaBukhsh; EMNLP 2026).

We built RPD-UoF, a corpus of 3,091 use-of-force narratives that the Rochester Police Department released under New York FOIL request RR20-02509. We use it to ask three questions:

- **RQ1.** Do officer-written narratives still separate by subject race after we redact race terms, names, and places?
- **RQ2.** Does conditioning an LLM on subject race change what it writes, or whether it writes at all?
- **RQ3.** Does racial signal survive text redaction and reappear in images generated from the narratives?

## What is in this repository

```
datasets/
  rpd_uof_metadata.json         3,091-record corpus, structured fields only (no narrative text)
  04_redacted/
    data_redacted.json          1,000 redacted narratives (500 Black, 500 White); RQ2 seed pool
    balanced_results_1000.json  987 redacted narratives with GPT-5.2 character sketches and image status (RQ3)
generations/
  narratives/generation_analysis_full.json   8,002 narratives from the controlled generation experiment (§4.2.1)
  character_sketches/balanced_1000/          807 GPT-5 images (RQ3)
outputs/
  pipelines/generation_v2.jsonl              14,037 counterfactual generations from 8 models (§4.2.2)
  analysis/log_odds_fixed.csv                log-odds z-scores per word (§4.1.1)
  classification/                            classifier results, LLM-output audit, FairFace CLIP baseline
notebooks/
  pipelines/                    P00 OCR extraction, P01 counterfactual generation
  analysis/                     00 to 06: corpus construction, log-odds, generation analysis, images, erasure, validation
  classification/               C00 race classifiers, C02 image pipeline, C03 classifier audit, C04 FairFace baseline
  config.example.py             paths, model IDs, constants
```

## Paper to file map

| Paper | Notebook | Data or output |
|---|---|---|
| §3, Table 8, Figs 1, 4, 5 | `P00_ocr_extraction_v2`, `00_data_pipeline_v2`, `06_validation_v2` | `datasets/rpd_uof_metadata.json` (full text withheld, see below) |
| §4.1.1, Fig 6 | `01_log_odds_fasttext_v2` | `outputs/analysis/log_odds_fixed.csv` |
| §4.1.2, Table 2 | `C00_narrative_race_classification_v2` | `outputs/classification/classification_results_*.json` |
| Fig 2 (erasure) | `05_race_inference_v2` | |
| §4.2.1, Table 3 | none (see Known gaps) | `generations/narratives/generation_analysis_full.json` |
| §4.2.2, Tables 4, 5 | `P01_narrative_generation_v2` | `outputs/pipelines/generation_v2.jsonl` |
| Table 9 | `C03_classifier_bias_audit` | `outputs/classification/classifier_bias_audit_*` |
| §4.3, Tables 6, 7, Figs 3, 7 | `C02_image_generation_pipeline_v2`, `04_character_image_audit_v2` | `datasets/04_redacted/balanced_results_1000.json`, `generations/character_sketches/balanced_1000/` |
| Figs 8, 9 | `C04_fairface_clip_baseline_v2` | `outputs/classification/fairface_clip_baseline*.json` |
| Appendix A.4 prompts | P2 and P2B in `P01`, P3 in `C02` | P1 and P4 appear only in the paper |

## Data availability

The FOIL release contains officer names, badge numbers, and addresses. We promised in the paper to remove these, so this repository ships only redacted text:

- `rpd_uof_metadata.json` keeps the structured fields for all 3,091 records (CR number, date, year, race, gender, force type, resistance, subject description, narrative length, train/test splits). It has no narrative text.
- The two redacted sets drop the original narrative and keep only the redacted version.
- In every text field we ship, including model outputs and notebook outputs, we replaced tokens that match a lexicon of 1,200 officer and person surnames with `[NAME]`. We built the lexicon from the unredacted corpus. It holds capitalized words that follow an officer title and that rarely appear in lowercase. We also dropped 227 name rows from `log_odds_fixed.csv` and the person names from `ROCHESTER_STOPWORDS`. Numeric fields such as word counts were computed before this pass and are unchanged.

The scanned PDFs, OCR output, and full-text corpus (`bw_dataset_with_splits.json`, `data_clean.json`, `data_deduplicated.json`, `police_narratives_complete.json`, `2022_narratives.json`) are available to researchers on request. Contact the corresponding author, Ashiqur R. KhudaBukhsh (axkvse@rit.edu). Notebooks that read these files (P00, 00, 01, 05, 06, C00, and parts of 03) will not run without them.

## Setup

```bash
cp notebooks/config.example.py notebooks/config.py
export OPENAI_API_KEY=... ANTHROPIC_API_KEY=... GEMINI_API_KEY=... \
       DEEPSEEK_API_KEY=... MISTRAL_API_KEY=... HF_TOKEN=...
```

Run each notebook from its own folder. The notebooks find `config.py` and the data through paths relative to the repository root, and `config.py` creates the output folders on import. Open-weight generators (Gemma, Llama, Mistral) are served through Ollama on the ports in `OLLAMA_PORTS`. C03 needs the fine-tuned BERT and DeBERTa checkpoints from C00, which we do not ship.

## Known gaps

- The code for Table 3 (differential adjectives) and the §4.2.1 generator is not in these notebooks. The generated narratives are in `generation_analysis_full.json`.
- The statistics in Tables 4 and 5 (per-model refusal rates, the McNemar test on discordant pairs, the paired t-tests) are not in the notebooks. We flagged a completion as a refusal when its `generated_text` contained a refusal phrase such as "I can't", "I cannot", or "I'm unable". The refusal-asymmetry figure, Figure 7 (ITA), and the BERT/DeBERTa re-run on `[REDACTED]` text (§4.1.2) are not in the notebooks either.
- `C02` writes new images to `generations/images/images_v2/`. The 875 images analyzed in the paper come from an earlier run of the same prompt (P3). Those are the images in `generations/character_sketches/balanced_1000/`, and `04` analyzes them.
- The last section of `C04` reads `outputs/image_character_v2.jsonl`, which comes from a later image run. That run is not part of the paper and is not included.
- `log_odds_fixed.csv` comes from an earlier run with 4,234 words. The paper reports 3,990 words after filtering a 695-token name vocabulary, which is not included.
- The 875 successful GPT-5 records in `balanced_results_1000.json` point to 807 image files. Multi-subject incidents share a CR number, so later images overwrote earlier ones.

## Ethics

The images and character sketches show what generative models do with race-redacted text. They make no claim that appearance says anything about a person. Section 7 of the paper discusses intent, annotation, and privacy.

## Citation

```bibtex
@inproceedings{dutta-forsyth-2026-race,
  title     = {Race in the Record: Measuring Racial Signal and Model Inference in Police Arrest Narratives},
  author    = {Dutta, Arka and Forsyth, Ted and Robertson, O. Nicholas and KhudaBukhsh, Ashiqur R.},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing},
  year      = {2026}
}
```
