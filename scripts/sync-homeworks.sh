#!/usr/bin/env bash
# Mirror student-facing homework files into otus-mlsd-homeworks.
#
# Usage:
#   ./scripts/sync-homeworks.sh /path/to/otus-mlsd-homeworks
#
# Source of truth is this program repo. The destination is overwritten to match
# the student slice (homeworks + two templates + generated README).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${1:-}"

if [[ -z "${DEST}" ]]; then
  echo "usage: $0 /path/to/otus-mlsd-homeworks" >&2
  exit 2
fi

if [[ ! -d "${DEST}" ]]; then
  echo "destination does not exist: ${DEST}" >&2
  exit 1
fi

DEST="$(cd "${DEST}" && pwd)"
STAGING="$(mktemp -d)"
trap 'rm -rf "${STAGING}"' EXIT

mkdir -p "${STAGING}/homeworks" "${STAGING}/templates"

shopt -s nullglob
for src in "${ROOT}"/homeworks/*.md; do
  python3 "${ROOT}/scripts/strip_teacher_notes.py" \
    "${src}" "${STAGING}/homeworks/$(basename "${src}")"
done
shopt -u nullglob

cp "${ROOT}/templates/design-doc-template.md" "${STAGING}/templates/design-doc-template.md"
cp "${ROOT}/templates/checklist.md" "${STAGING}/templates/checklist.md"

cat > "${STAGING}/.gitignore" <<'EOF'
.DS_Store
.venv
__pycache__/
.idea/
.vscode/
EOF

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync is required" >&2
  exit 1
fi

rsync -a --delete \
  --exclude '.git/' \
  --exclude '.github/' \
  "${STAGING}/" "${DEST}/"

forbidden=(program.md lessons prompts archive .cursor artifacts)
for name in "${forbidden[@]}"; do
  if [[ -e "${DEST}/${name}" ]]; then
    echo "unexpected path in student repo: ${DEST}/${name}" >&2
    exit 1
  fi
done

if grep -R --quiet "Примечание для преподавателя" "${DEST}/homeworks"; then
  echo "teacher notes leaked into ${DEST}/homeworks" >&2
  exit 1
fi

echo "synced student slice -> ${DEST}"
