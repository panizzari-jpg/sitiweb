#!/bin/bash
# Pubblica le build sui branch GitHub (Hostinger auto-deploy). Uso: ./pubblica.sh "messaggio"
set -e
MSG=${1:-"Aggiornamento siti"}
R=/home/claude/sitiweb
cd $R && git checkout -q main
cp /home/claude/sites/{core.py,laser.py,studio.py,shot.py,pubblica.sh,LEGGIMI_DEPLOY.md,immagini_da_copiare.txt} /home/claude/sites/sitemap_attuale_*.txt sorgenti/ 2>/dev/null || true
mkdir -p sorgenti/asset_originali && cp -r /home/claude/sites/asset_originali/. sorgenti/asset_originali/
git add -A && git commit -qm "$MSG (sorgenti)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Hs2iGZAZvAv5NP8eeTF48u" || true
for s in progettilaser pangeastudio; do
  git checkout -q $s
  HT=$(cat .htaccess)
  find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
  cp -r /home/claude/sites/build/$s/. . && rm -f htaccess-da-unire.txt
  echo "$HT" > .htaccess
  git add -A && git commit -qm "$MSG ($s)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Hs2iGZAZvAv5NP8eeTF48u" || true
done
git checkout -q main
git -c push.negotiate=true push -q origin main progettilaser pangeastudio 2>&1 | grep -v "negotiat\|acknowledg" || true
git ls-remote origin | cat
