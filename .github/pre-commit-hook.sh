#!/bin/bash
# Pre-commit hook to prevent committing sensitive files
# To enable: Copy this to .git/hooks/pre-commit and make executable

echo "🔍 Running security checks..."

# Check for .env files
if git diff --cached --name-only | grep -E "\.env$|\.env\.local$"; then
    echo "❌ ERROR: Attempting to commit .env file!"
    echo "Your .env file contains sensitive API keys."
    echo "This commit has been blocked."
    exit 1
fi

# Check for API keys in staged changes
if git diff --cached | grep -iE "GROQ_API_KEY.*=.*gsk_[a-zA-Z0-9]{52}"; then
    echo "❌ ERROR: Detected API key in staged changes!"
    echo "Remove the API key before committing."
    exit 1
fi

# Check for common secret patterns
if git diff --cached | grep -iE "(password|secret|api[_-]?key|private[_-]?key).*=.*['\"][^'\"]{10,}"; then
    echo "⚠️  WARNING: Potential secret detected in staged changes!"
    echo "Please review your changes carefully."
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "✅ Security checks passed!"
exit 0
