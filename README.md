# clustering

<div align="center">

[![Build status](https://github.com/clustering/clustering/workflows/build/badge.svg?branch=master&event=push)](https://github.com/clustering/clustering/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/clustering.svg)](https://pypi.org/project/clustering/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/clustering/clustering/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/clustering/clustering/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/clustering/clustering/releases)
[![License](https://img.shields.io/github/license/clustering/clustering)](https://github.com/clustering/clustering/blob/master/LICENSE)

CLI to apply UMAP/Leiden clustering to an array of values

</div>

Honestly, just a dumb front end to cluster a matrix of data using UMAP for nearest neighbors and Leiden for
community detection.  Written because passing data from {reticulate} easily hits up against a `C stack limit` and I'm tired to trying to figure out how to get around it.


## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/clustering/clustering/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

For Pull Request this labels are configured, by default:

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/clustering/clustering/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/clustering/clustering)](https://github.com/clustering/clustering/blob/master/LICENSE)

This project is licensed under the terms of the `BSD-3` license. See [LICENSE](https://github.com/clustering/clustering/blob/master/LICENSE) for more details.

## 📃 Citation

```
@misc{clustering,
  author = {clustering},
  title = {CLI to apply Leiden clustering to an array of values},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/clustering/clustering}}
}
```

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
