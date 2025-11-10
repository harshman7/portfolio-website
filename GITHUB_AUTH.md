# 🔐 GitHub Authentication Guide

Your code is ready to push, but you need to authenticate with GitHub first.

## Option 1: Use Personal Access Token (Recommended)

### Step 1: Create Personal Access Token

1. **Go to GitHub Settings**
   - Visit: https://github.com/settings/tokens
   - Or: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

2. **Generate New Token**
   - Click "Generate new token" → "Generate new token (classic)"
   - **Note**: Give it a name like "Portfolio Website"
   - **Expiration**: Choose your preferred duration (90 days, 1 year, etc.)
   - **Scopes**: Check `repo` (full control of private repositories)
   - Click "Generate token"

3. **Copy the Token**
   - ⚠️ **Important**: Copy the token immediately (you won't see it again!)
   - It will look like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 2: Push Using Token

```bash
# When prompted for password, use your Personal Access Token instead
git push -u origin main
```

**Username**: `harshman7`  
**Password**: `(paste your Personal Access Token)`

---

## Option 2: Use GitHub CLI (Easier)

### Install GitHub CLI

```bash
# macOS
brew install gh

# Or download from: https://cli.github.com
```

### Authenticate

```bash
gh auth login
```

Follow the prompts to authenticate, then push:

```bash
git push -u origin main
```

---

## Option 3: Update Git Credentials

### Clear Old Credentials

```bash
# macOS Keychain
git credential-osxkeychain erase
host=github.com
protocol=https
```

### Push (will prompt for new credentials)

```bash
git push -u origin main
```

When prompted:
- **Username**: `harshman7`
- **Password**: Use Personal Access Token (not your GitHub password)

---

## Quick Push Command

After setting up authentication, run:

```bash
cd "/Users/harshmanpreetsingh/Desktop/Portfolio website"
git push -u origin main
```

---

## Verify Push

After pushing, check your repository:
https://github.com/harshman7/portfolio-website

You should see all your files!

---

## Troubleshooting

### "Permission denied" error
- Make sure you're using the correct GitHub username
- Use Personal Access Token, not password
- Check token has `repo` scope

### "Repository not found" error
- Verify repository exists: https://github.com/harshman7/portfolio-website
- Check you have write access to the repository

### Authentication issues
- Clear old credentials
- Generate new Personal Access Token
- Use GitHub CLI for easier authentication

---

**Recommended**: Use **Option 1 (Personal Access Token)** - it's the most reliable method!

