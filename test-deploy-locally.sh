#!/bin/bash

# Test script to simulate the GitHub Actions deploy workflow locally
# Usage: ./test-deploy-locally.sh YOUR_GITHUB_TOKEN

set -e

# Check for required tools
if ! command -v jq &> /dev/null; then
    echo "Error: 'jq' is required but not installed."
    echo ""
    echo "Install jq:"
    echo "  - macOS: brew install jq"
    echo "  - Ubuntu/Debian: sudo apt-get install jq"
    echo "  - RHEL/CentOS: sudo yum install jq"
    exit 1
fi

if [ -z "$1" ]; then
    echo "Usage: $0 <github-token>"
    echo ""
    echo "Get a token from: https://github.com/settings/tokens"
    echo "Token needs 'repo' scope with full access"
    exit 1
fi

GITHUB_TOKEN="$1"
TARGET_REPO="davegoopot/beemanager-deploy"

echo "=== Testing Deploy Workflow Locally ==="
echo ""

# Test 1: Check API access
echo "[1/5] Testing API access to target repository..."
response=$(curl -s -H "Authorization: token ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/${TARGET_REPO})

if echo "$response" | jq -e '.name' > /dev/null 2>&1; then
    echo "✓ API access successful"
    echo "  Repo: $(echo "$response" | jq -r '.full_name')"
    echo "  Permissions: $(echo "$response" | jq -r '.permissions')"
else
    echo "✗ API access failed"
    echo "$response" | jq '.' 2>/dev/null || echo "$response"
    exit 1
fi
echo ""

# Test 2: Note about temp_clone_token
echo "[2/5] Note about temp_clone_token..."
temp_clone_token=$(echo "$response" | jq -r '.temp_clone_token // empty')
if [ -n "$temp_clone_token" ]; then
    echo "  Found temp_clone_token: ${temp_clone_token:0:10}..."
    echo "  Note: temp_clone_token is READ-ONLY and cannot be used for push"
fi
echo "  Using GITHUB_TOKEN for git operations (push requires write access)"
GIT_TOKEN="$GITHUB_TOKEN"
echo ""

# Test 3: Check if repository is empty
echo "[3/5] Checking if repository is empty..."
refs_response=$(curl -s -H "Authorization: token ${GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/${TARGET_REPO}/git/refs)

if echo "$refs_response" | grep -q "Git Repository is empty"; then
    echo "  Repository is empty (would need initialization)"
else
    echo "✓ Repository has commits"
fi
echo ""

# Test 4: Test git ls-remote with credential store
echo "[4/5] Testing git ls-remote with credential store..."
# Set up temporary git config
export GIT_CONFIG_GLOBAL="/tmp/test-git-config-$$"
export HOME_BACKUP="$HOME"
export HOME="/tmp/test-home-$$"
mkdir -p "$HOME"

git config --global user.name "Test User"
git config --global user.email "test@example.com"
git config --global credential.helper store

# Create credentials file
install -m 600 /dev/null ~/.git-credentials
echo "https://git:${GIT_TOKEN}@github.com" > ~/.git-credentials

echo "  Credentials file created at: ~/.git-credentials"
echo "  Testing git ls-remote..."

if git ls-remote https://github.com/${TARGET_REPO}.git 2>&1; then
    echo "✓ git ls-remote successful!"
else
    echo "✗ git ls-remote failed"
    echo ""
    echo "Trying with token directly in URL..."
    if git ls-remote https://${GIT_TOKEN}@github.com/${TARGET_REPO}.git 2>&1; then
        echo "✓ Direct token in URL works!"
        echo ""
        echo "This suggests the credential store isn't being used properly."
    else
        echo "✗ Even direct token in URL fails"
        echo ""
        echo "This suggests the token doesn't have git protocol access."
    fi
fi
echo ""

# Test 5: Summary and cleanup
echo "[5/5] Test Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Token being used for git operations: ${GIT_TOKEN:0:15}..."
echo ""
echo "To debug further, try these commands:"
echo ""
echo "1. Test API access:"
echo "   curl -H \"Authorization: token YOUR_TOKEN\" \\"
echo "        https://api.github.com/repos/${TARGET_REPO}"
echo ""
echo "2. Test git ls-remote directly:"
echo "   git ls-remote https://YOUR_TOKEN@github.com/${TARGET_REPO}.git"
echo ""
echo "3. Check token scopes at:"
echo "   https://github.com/settings/tokens"
echo ""

# Cleanup
rm -rf "/tmp/test-home-$$" "$GIT_CONFIG_GLOBAL"
export HOME="$HOME_BACKUP"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
