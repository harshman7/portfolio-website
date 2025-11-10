#!/bin/bash
# Script to push portfolio website to GitHub

echo "🚀 Pushing Portfolio Website to GitHub"
echo ""

# Check if remote exists
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ Remote 'origin' already exists"
    echo "Remote URL: $(git remote get-url origin)"
    echo ""
    echo "Pushing to GitHub..."
    git push -u origin main
else
    echo "❌ No remote repository configured"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Create a repository on GitHub: https://github.com/new"
    echo "2. Name it: portfolio-website (or your preferred name)"
    echo "3. DO NOT initialize with README, .gitignore, or license"
    echo "4. Copy the repository URL"
    echo ""
    echo "5. Then run:"
    echo "   git remote add origin https://github.com/YOUR_USERNAME/portfolio-website.git"
    echo "   git push -u origin main"
    echo ""
    echo "Or run this script again after adding the remote!"
fi

