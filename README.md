# English to Any Language Translator

A Python translation utility using the [`deep-translator`](https://pypi.org/project/deep-translator/) library with Google Translate backend. No API keys are required.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI translator:

```bash
python translator.py
```

### Features
- **[PR 1] Basic Text Translator**: Enter text in English and target language (e.g. `french`, `hindi`, `spanish`, `punjabi`, etc., or ISO language codes like `fr`, `hi`, `es`, `pa`).
- Supports 100+ languages provided by Google Translate.
- Clean terminal prompt loop with exception handling and UTF-8 safe output logging.