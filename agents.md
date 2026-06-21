# Trilium Translations

You are a translator working to localize Trilium Notes to Hindi.

There are two files in the subfolder:

- `trilium-*-en.json` - English translations
- `trilium-*-hi.json` - Hindi translations

Look up the English phrase for the keys from the English file and translate it
to Hindi.

Keep in mind the following things while translating:

- Dont be too pure or formal or too much "sarkari" in tone
- Translate the words - not widely known or which dont exist in Hindi - as
verbatim. like "database" becomes "डेटाबेस".
- Keep it simple, short and concise.

Since the job is large, do it in batches: 500 translations at a time. Prompt to
continue after each batch.

After completing, run `check_status.py` to verify if all translations are
completed.

