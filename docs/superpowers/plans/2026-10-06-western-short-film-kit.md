# Western Short Film Kit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Publish a usable Thai-first vertical AI filmmaking starter kit.
**Architecture:** Markdown prompts and templates with a fully written original six-shot example. Reuse the MIT Chinese kit checker at its existing `check(root)` interface, with targeted validation and a small stdlib regression check.
**Tech Stack:** Markdown, SVG, Python stdlib, GitHub Actions.
**Spec:** docs/superpowers/specs/2026-10-06-western-short-film-kit-design.md

## Global Constraints
- 9:16, 48-second example, six ordered 8-second shots, one adult speaker.
- Python 3.9+, no additional packages; MIT attribution for reused code.
- Free distributable kit; no credit spending or claims of rendered video.
- Public release in the authenticated GitHub account; no credentials or production assets.

## Review Focus
- Broken relative links or absent required kit files must fail validation.
- Gaps, reordered shots, wrong duration, wrong speaker or changed dialogue must fail.
- Copying one prompt alone must preserve character, outfit and scene continuity.
- Flow UI and model capability changes must not make exact settings or prices guarantees.
- Example-only editing must not imply actual subtitle alignment or audiovisual QC.

### Task 1: Publishable content and validator
**Files:** README.md, WORKFLOW.md, AGENTS.md, LICENSE, THIRD_PARTY_NOTICES.md, assets/hero.svg; prompts/MASTER-PROMPT.md, prompts/REPAIR.md; templates/PRODUCTION.md; examples/one-floor-below-48s.md; docs/GOOGLE-FLOW.md, docs/EDITING.md, docs/TEST-REPORT.md; scripts/check_repo.py and scripts/test_check_repo.py; .github/workflows/check.yml.
**Interfaces:** `check(root: Path) -> tuple[errors, document_count, link_count]`; CLI exit 0 on success and 1 on errors. Regression script executes the real checker against temporary altered copies.
- [x] Write a small regression script; verify the checker is missing before implementation.
- [x] Adapt the existing checker; write the kit and an original complete example.
- [x] Verify: `python3 scripts/check_repo.py` and `python3 scripts/test_check_repo.py` both exit 0; negative mutations fail for the expected reasons.
- [x] Commit all verified content.

### Task 2: Review and public delivery
**Interfaces:** Existing verified content, public GitHub repository URL, standalone ZIP.
- [x] Fresh-context whole-repository review against the spec, plan and Review Focus; repair material findings and rerun checks.
- [x] Create the new public repo with gh, push main, verify visibility and full remote file tree.
- [x] Verify GitHub Actions passes, create a ZIP from the committed tree and verify its files.
- [x] Report the repository and ZIP links with the unrendered-media limitation.
