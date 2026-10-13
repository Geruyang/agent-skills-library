---
name: reference-import-docx-to-native-docs
description: Import a local DOCX as a native Google Docs document.
---

# Import DOCX To Native Google Docs

When to read: after Default Routing selects DOCX-first creation without a constraining Google Doc template/reference, or after creating or locating a local `.docx` file that the user explicitly wants converted to a native Google Docs document.

This is the polished or complex creation path. Do not use it for blank Google Docs or basic native docs that can be created directly through `reference-native-create-direct.md`.
Do not use it when a supplied Google Doc template, reference, or example is expected to shape the output. Those tasks remain native so tabs, styles, table formatting, chips, controls, and other Google Docs semantics can be copied and adapted.
For DOCX-first Google Docs creation, create the local document with an available DOCX creation tool first, selecting a Google Docs compatible design preset (called `google_docs_default` in the original Documents plugin) unless the user asked for a special, branded, or highly polished visual treatment, then follow this import path.

## Native Conversion

Use native Google Docs conversion by default. For `.docx` inputs, the blessed path is the Google Drive plugin document import action, a discovered Drive native-document import operation, with `upload_mode: "native_google_docs"`. The original connector wrapper uses `upload_mode`; other integrations must use their own verified schema. The equivalent Google Drive API v3 route is `files.create` upload-conversion path by creating the file with the target Google Workspace MIME type `application/vnd.google-apps.document`. Do not preserve the source file type unless the user explicitly asks to keep a Word file in Drive without converting it.

Before import, confirm the Google Drive plugin exposes a discovered Drive native-document import operation. Use the current host’s authenticated Drive integration and verified native-conversion schema. A connector import action or the documented Drive API upload-conversion route may be used only when it preserves the required native result. If neither is available, report the missing integration before importing; do not assume the original plugin identifier can be installed in this host.

Steps:

1. Confirm no supplied Google Doc template/reference constrains the result. If one does, stop and return to the native copy/adaptation route.
2. Confirm the local source path is an absolute path to a `.docx` file.
3. Confirm the local staging path is a per-task scratch directory, not the user-facing workspace root.
4. Confirm no persistent DOCX builder or helper source file was created with tracked file-edit tools such as `apply_patch`, and no helper source file lives in a path surfaced by Changes Made. If generation logic is needed, use the Documents plugin's built-in tooling or a one-shot runtime command that keeps the code ephemeral and writes only the `.docx` and required QA outputs into scratch space. If a tracked helper file was already created, regenerate through untracked scratch before upload unless the user explicitly asked to keep that file.
5. Import the file with the Google Drive connector document import action:

```json
{
  "source_file": "/absolute/path/to/document.docx",
  "title": "Desired Google Doc title",
  "upload_mode": "native_google_docs"
}
```

6. Use the connector function exposed in the current runtime: the discovered native-document import operation.
7. Verify the import response reports native conversion with `mime_type: "application/vnd.google-apps.document"` and a Google Docs URL or document id.
8. If the desired Google Doc title needs adjustment after import, rename the native Google Doc with the discovered Drive metadata-update operation (`files.update`) or the equivalent Drive metadata update tool after upload.
9. Read the imported document with the Google Docs connector and verify that core headings, body text, tables, and other connector-visible content survived conversion.
10. Run the repair-only post-import normalization and mandatory smart-chip pass below.
11. After successful connector readback and normalization, clean up local staging artifacts: generated render folders, QA PNG/PDF files, temporary assets, and the local `.docx` source. Keep local files only when the user explicitly asked to preserve them. Cleanup is a final backstop and does not replace the requirement to avoid tracked helper files before upload.

## Post-Import Normalization

Use this only for imported net-new Google Docs created from the Documents plugin. The goal is to repair conversion drift, not to create a second styling system.

1. Re-read the imported document and sample the title, the first real section heading, one body paragraph, and the first list if present.
2. Verify the imported document still matches the `google_docs_default` intent:
   - title/headings/body text use Arial or the closest connector-visible Arial family
   - text color is black for title, headings, body, and lists
   - section hierarchy is preserved with real Docs heading styles
   - bullets and numbered items are real Docs lists, not typed markers
   - no obvious Word-style residue survived import: blue heading colors, decorative running headers/footers, colored callout fills, dense table borders, or table-first packaging of normal prose
3. If any of those checks drifted during import, use the normal Google Docs connector write path to repair only the affected ranges. Prefer `updateParagraphStyle`, `updateTextStyle`, `createParagraphBullets`, `deleteParagraphBullets`, `updateTableCellStyle`, and other narrow native requests instead of broad rewrites.
4. Identify every concrete semantic date, known-email person, Google Calendar event URL, and Google Docs/Sheets/Slides URL that the import flattened to text or an ordinary hyperlink. Replace it with `insertDate`, `insertPerson`, or `insertRichLink` according to `reference-smart-chips-and-building-blocks.md`; this native repair is required, not a styling flourish.
5. Re-read the repaired ranges and verify each required `dateElement`, `person`, and `richLink`. When available, export `text/html` only as a structure/style proxy; HTML cannot prove smart-chip semantics.
6. Do not add unrelated metadata pills, decorative mastheads, or new styling flourishes in this pass.

## Preservation Mode

Only use a non-native upload when the user explicitly asks to preserve the Word file, keep the source `.docx`, or avoid conversion.

For that explicit preservation request, use `_import_document` with
`upload_mode: "keep_source_file_type"` and make clear that the result is a
Drive-hosted Word file, not a native Google Doc.

## Final Answer

Return the native Google Doc title and link or id when available.
Do not cite the local `.docx` path in the final answer after a successful native import.
