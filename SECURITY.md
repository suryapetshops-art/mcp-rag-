# Security & secret handling

If a secret (API key, password, token) is accidentally exposed in this repository, **act immediately**:

1. Rotate the secret at the provider right away (revoke the old key and create a new one).
2. Remove the secret from repository history and force-push the cleaned repo (see options below).
3. Notify your team and any downstream systems that may have used the exposed secret.

## Quick detection commands
- Find commits that mention a key prefix (example):
  - `git log --all -S 'sk-proj-' --pretty=format:"%h %an %ad %s"`
- Search current files for the string:
  - `git grep -n "sk-proj-" || true`

## Recommended cleaning: git filter-repo (preferred)
1. Clone a mirror of the repo:
   - `git clone --mirror https://github.com/<owner>/<repo>.git`
2. Create `replacements.txt` with lines of the form `OLD==>NEW` (e.g., `sk-proj-REDACTED==>[REDACTED]`).
3. Run:
   - `git filter-repo --replace-text replacements.txt`
4. Expire reflogs and run GC:
   - `git reflog expire --expire=now --all && git gc --prune=now --aggressive`
5. Push the cleaned history (force):
   - `git push --force --all`
   - `git push --force --tags`

Notes: `git filter-repo` is the recommended tool (fast and flexible). Install it from https://github.com/newren/git-filter-repo.

## Alternative: BFG Repo-Cleaner
1. Mirror clone:
   - `git clone --mirror https://github.com/<owner>/<repo>.git`
2. Create a `passwords.txt` file that lists secrets and patterns to replace.
3. Run:
   - `java -jar bfg.jar --replace-text passwords.txt repo.git`
4. `cd repo.git`
   - `git reflog expire --expire=now --all && git gc --prune=now --aggressive`
   - `git push --force` 

## After cleaning
- Ask all collaborators to re-clone the repository (old clones may still contain the secret in the reflog).
- Invalidate any tokens tied to the exposed secret and rotate them in third-party services.
- If the secret was pushed to a public remote, treat it as compromised and rotate immediately.

## Help
If you'd like, I can prepare the exact `replacements.txt` or BFG `passwords.txt` for the secret value you want removed (do not paste the real secret here; tell me whether the secret was pushed and to which remote and I will provide the exact commands to run locally).
