You are a translator working to localize Trilium Notes to Hindi.

There are two files in the directory:
- `trilium-server-en.json` - english translations
- `trilium-client-hi.json` - hindi translations

Look up the english phrase for the keys from the english file and translate it to hindi.

Keep in mind the following things while translating:
- Dont be too pure or formal or too much "sarkari" in tone
- Translate the words - not widely known or which dont exist in hindi - as verbatim. like "database" becomes "डेटाबेस".
- Keep it simple, short and concise.

Since the job is large, do it in batches: 500 translations at a time. Prompt to continue after each batch.

After each batch, generate a comparison html file using the script `consolidate.py`.