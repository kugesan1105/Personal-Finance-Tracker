# Release Workflow Setup - Summary

## ✅ What's Been Set Up

Your Personal Finance Tracker now has a **fully automated one-click release system**!

### Files Created/Modified

1. **[.github/workflows/release.yml](.github/workflows/release.yml)** ⭐ Main workflow
   - Handles version bumping
   - Updates dependencies
   - Creates git tags and GitHub releases
   - Automatic commits and pushes

2. **[RELEASE_GUIDE.md](RELEASE_GUIDE.md)** 📖 Complete documentation
   - How to create releases
   - Workflow features and inputs
   - Troubleshooting guide
   - Versioning conventions

3. **[release.sh](release.sh)** 🚀 Helper script
   - Quick reference commands
   - CLI examples using GitHub CLI

### Key Features

✨ **Single-Click Release Process**
- No manual file editing needed
- All steps automated
- Version bumping in setup.py
- Dependency version updates (optional)
- Automatic git tags and GitHub releases

🎯 **Easy to Use Interface**
- Web UI in GitHub Actions
- Fill in version number
- Check "Update dependencies" checkbox
- Click "Run workflow"

🔄 **Flexible Configuration**
- Update package version only
- Or update dependencies simultaneously
- Individual control over each dependency version
- Customizable release names

📦 **Manages These Dependencies**
```
pytest, black, flake8, mypy, isort, pytest-cov, pytest-mock,
pre-commit, sphinx, sphinx-rtd-theme, bandit, safety
```

### Quick Start

1. **Go to GitHub → Actions Tab**
2. **Select "Release" Workflow**
3. **Click "Run workflow"**
4. **Fill in:**
   - Version: `1.0.1` (or desired version)
   - Update dependencies: Yes/No
   - Individual dependency versions (if updating)
5. **Click "Run workflow"**
6. **Done!** 🎉

The workflow will:
- Update version in setup.py
- Update dependencies in requirements files
- Commit changes
- Create git tag (v1.0.1)
- Create GitHub Release
- Display completion summary

### Workflow Inputs Available

#### Required
- **package_version**: Semantic version (e.g., 1.0.1)

#### Optional
- **release_name**: Custom release description
- **update_dependencies**: Boolean checkbox
- **Individual dependency versions**: 12 dependencies configurable

### Versioning Guide

```
1.0.0 → 1.0.1 (patch)   - Bug fixes
1.0.1 → 1.1.0 (minor)   - New features
1.1.0 → 2.0.0 (major)   - Breaking changes
```

### What Gets Automated

1. ✅ Version number in setup.py
2. ✅ All dependency versions in requirements.txt
3. ✅ All dependency versions in requirements-dev.txt
4. ✅ Git commit with version message
5. ✅ Git tag creation (v1.0.1)
6. ✅ GitHub Release creation
7. ✅ Release notes generation
8. ✅ Completion summary

### No More Manual Steps!

❌ Don't need to:
- Manually edit setup.py
- Manually edit requirements files
- Manually commit and push
- Manually create git tags
- Manually create GitHub releases

✅ Just trigger the workflow and you're done!

---

**For detailed instructions, see [RELEASE_GUIDE.md](RELEASE_GUIDE.md)**
