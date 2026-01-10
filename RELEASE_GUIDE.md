# Release Guide - Personal Finance Tracker

## Automated Release Workflow

This project uses GitHub Actions to automate the release process. You can create a release in a single click!

### How to Create a Release

1. Go to your repository on GitHub
2. Navigate to **Actions** tab
3. Select **Release** workflow from the left sidebar
4. Click **Run workflow** button
5. Fill in the required inputs:
   - **Package version**: The version to release (e.g., `1.0.1`, `1.1.0`)
   - **Release name**: A human-readable name for the release (optional)
   - **Update dependencies**: Check this box if you want to update dependency versions
   - **Individual dependency versions**: Fill these in if updating dependencies

### Workflow Features

✅ **Automatic Version Bumping**
- Updates version in `setup.py`
- Updates all dependencies in `requirements.txt` and `requirements-dev.txt`
- Commits changes automatically

✅ **Git Integration**
- Creates a git tag (e.g., `v1.0.1`)
- Pushes changes and tags to main branch
- Creates a GitHub Release with notes

✅ **Dependency Management**
The workflow can update these dependencies:
- **Testing**: pytest, pytest-cov, pytest-mock
- **Code Quality**: black, flake8, isort, mypy
- **Pre-commit**: pre-commit
- **Documentation**: sphinx, sphinx-rtd-theme
- **Security**: bandit, safety

### Workflow Inputs

#### Required
- **package_version**: Semantic version (e.g., `1.0.1`)

#### Optional
- **release_name**: Release description (default: "Release")
- **update_dependencies**: Boolean to update deps (default: false)

#### Dependency Versions (if updating)
- `pytest_version` (default: `6.0.0`)
- `black_version` (default: `21.0.0`)
- `flake8_version` (default: `3.8.0`)
- `mypy_version` (default: `0.800`)
- `isort_version` (default: `5.9.0`)
- `pytest_cov_version` (default: `2.12.0`)
- `pytest_mock_version` (default: `3.6.0`)
- `pre_commit_version` (default: `2.15.0`)
- `sphinx_version` (default: `4.0.0`)
- `sphinx_rtd_theme_version` (default: `0.5.0`)
- `bandit_version` (default: `1.7.0`)
- `safety_version` (default: `1.10.0`)

### What Happens During Release

1. 🔍 **Checkout** - Fetches the latest code
2. 🐍 **Python Setup** - Sets up Python 3.10 environment
3. 📝 **Version Update** - Updates package version in setup.py
4. 📦 **Dependency Update** - Updates dependency versions (if enabled)
5. ✅ **Verification** - Prints all changes made
6. 💾 **Commit** - Commits changes to main branch
7. 🏷️ **Tag** - Creates and pushes git tag
8. 📚 **Release** - Creates GitHub Release with notes
9. 📊 **Summary** - Prints release summary

### Example Release Scenarios

#### Scenario 1: Simple Patch Release
- Package version: `1.0.1`
- Update dependencies: ❌ (unchecked)
- Result: Version bumped, no dependency changes

#### Scenario 2: Feature Release with Dependency Updates
- Package version: `1.1.0`
- Update dependencies: ✅ (checked)
- Update all dependency versions to latest
- Result: Version and dependencies updated

#### Scenario 3: Major Release
- Package version: `2.0.0`
- Release name: `Major Update`
- Update dependencies: ✅ (checked)
- Result: Major version bump with latest dependencies

### Verification

After the workflow completes:

1. Check the **Actions** tab for workflow status (green checkmark = success)
2. Visit **Releases** tab to see the new release
3. Verify git tag was created: `git tag` or GitHub Tags page
4. Confirm files were updated:
   - `setup.py` - version changed
   - `requirements.txt` - if dependencies were updated
   - `requirements-dev.txt` - if dependencies were updated

### Troubleshooting

**Workflow failed to push:**
- Ensure you have GitHub Actions permissions for pushing
- Check branch protection rules (release workflow needs write access)

**Version not updated:**
- Verify the version format matches semantic versioning
- Check that setup.py has the `version="X.X.X"` pattern

**Dependencies not updated:**
- Ensure the `update_dependencies` checkbox is checked
- Verify dependency versions are in correct format (e.g., `>=6.0.0`)

### Versioning Convention

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.0.0)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

Example progression:
- `1.0.0` → `1.0.1` (patch)
- `1.0.1` → `1.1.0` (minor)
- `1.1.0` → `2.0.0` (major)
