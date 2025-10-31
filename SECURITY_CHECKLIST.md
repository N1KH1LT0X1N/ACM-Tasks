# 🔒 Security Checklist - Before Every Commit

## ✅ Pre-Commit Security Verification

Run these checks BEFORE every `git commit` and `git push`:

### 1. Check Git Status
```powershell
git status
```
**Look for:**
- ❌ No `.env` files should appear
- ❌ No PDF files with sensitive data
- ❌ No files in `task2/` that shouldn't be there

### 2. Verify .env is Ignored
```powershell
git check-ignore task2/.env .env
```
**Expected output:** Both paths should be listed (means they're ignored)

### 3. Review Changes
```powershell
git diff
```
**Check for:**
- ❌ No API keys (gsk_...)
- ❌ No passwords or secrets
- ❌ No hardcoded credentials

### 4. Check Staged Changes
```powershell
git diff --cached
```
**Verify:**
- ✅ Only intended files are staged
- ✅ No sensitive data in staged files

### 5. Search for Secrets in Staged Files
```powershell
git diff --cached | Select-String -Pattern "gsk_|api.*key.*=|secret.*=|password.*="
```
**Expected output:** No matches (or only in .env.example with placeholder values)

### 6. Verify .gitignore
```powershell
Get-Content .gitignore | Select-String -Pattern ".env|.pdf"
```
**Expected output:** Should show .env and PDF patterns are ignored

---

## 🚨 Current Security Status

### ✅ Protected Files (Ignored by Git)
- `task2/.env` - Contains your actual API key
- `task2/ACM_Tasks.pdf` - May contain sensitive data
- `task2/Banking_BMC.pdf` - May contain sensitive data
- All `__pycache__/` directories
- All `.pyc` files
- `venv/` directory

### ✅ Safe to Commit (Example Files)
- `task2/.env.example` - Template with placeholder
- All `.py` files - No hardcoded secrets
- All `.md` files - Documentation only
- `.gitignore` - Ignore rules

### ⚠️ Files That Were Checked
- ✅ No `.env` in git history
- ✅ No real API keys in code
- ✅ No secrets in documentation

---

## 📋 Quick Pre-Commit Checklist

Copy this and check each item before committing:

```
[ ] Ran `git status` - No unexpected files
[ ] Ran `git check-ignore .env` - .env is ignored
[ ] Ran `git diff` - No secrets visible
[ ] Reviewed all staged files
[ ] No API keys in changes (gsk_...)
[ ] No passwords or tokens
[ ] Only intended files are staged
[ ] Commit message is clear and descriptive
```

---

## 🛡️ Security Commands Quick Reference

```powershell
# Check what will be committed
git status

# Check if .env is properly ignored
git check-ignore task2/.env

# See all changes before staging
git diff

# See staged changes before committing
git diff --cached

# Search for potential secrets in changes
git diff --cached | Select-String "gsk_|password|secret|api.*key"

# Check git history for .env files
git log --all --full-history -- **/.env

# List all files tracked by git in task2/
git ls-files task2/
```

---

## 🔄 Safe Commit Workflow

1. **Make changes to code**
   ```powershell
   # Edit files normally
   ```

2. **Review changes**
   ```powershell
   git status
   git diff
   ```

3. **Stage only intended files**
   ```powershell
   git add task1/task1.py
   git add README.md
   # etc. - Stage files individually
   ```

4. **Review staged changes**
   ```powershell
   git diff --cached
   ```

5. **Run security check**
   ```powershell
   git diff --cached | Select-String "gsk_|password|secret"
   ```

6. **Commit if safe**
   ```powershell
   git commit -m "Your commit message"
   ```

7. **Push to GitHub**
   ```powershell
   git push origin main
   ```

---

## 🚨 What If You Find a Secret?

If you discover a secret in your changes:

1. **DON'T commit or push!**
2. **Unstage the file:**
   ```powershell
   git reset HEAD <file>
   ```
3. **Remove the secret from the file**
4. **Add the file to .gitignore if needed**
5. **Re-stage the cleaned file**

---

## 📞 Emergency Contacts

If you accidentally commit/push secrets:

1. **Revoke API Key Immediately**
   - Groq Console: https://console.groq.com/keys

2. **Contact Platform**
   - GitHub Support for sensitive data removal

3. **Clean Git History** (see .env.security file)

---

## ✅ Your Current Status: SECURE

- API Key Location: `task2/.env` (ignored ✅)
- API Key Status: **NOT in git history** ✅
- .gitignore Status: **Working correctly** ✅
- Security Risk: **LOW** ✅

**Keep following this checklist before every commit!** 🔒
