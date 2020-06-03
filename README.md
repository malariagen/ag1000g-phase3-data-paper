# Ag1000G phase 3 data resource paper

[![HTML Manuscript](https://img.shields.io/badge/manuscript-HTML-blue.svg)](https://malariagen.github.io/ag1000g-phase3-data-paper/)
[![PDF Manuscript](https://img.shields.io/badge/manuscript-PDF-blue.svg)](https://malariagen.github.io/ag1000g-phase3-data-paper/manuscript.pdf)
[![GitHub Actions Status](https://github.com/malariagen/ag1000g-phase3-data-paper/workflows/Manubot/badge.svg)](https://github.com/malariagen/ag1000g-phase3-data-paper/actions)

This repository is for building a manuscript describing the Ag1000G
phase 3 data resource.

**This is a work in progress. Any data made available via this
repository are subject to the [Ag1000G terms of
use](https://www.malariagen.net/data/terms-use/ag1000g-terms-use).**

## Contributor setup

Fork this repository to your own github user account, then clone
locally, e.g.:

```
git clone --recursive git@github.com:{myusername}/ag1000g-phase3-data-paper.git
```

Run the conda environment installation script:

```
cd /path/to/local/clone/of/ag1000g-phase3-data-paper
./binder/install-conda.sh
```

Once conda is installed, activate the conda environment:

```
source binder/env.sh
```

Run a jupyter notebook server, e.g.:

```
jupyter notebook
```

...or:

```
jupyter lab
```

## Approach

- This is a public repo, meaning no personal information, _e.g._, no email addresses, no reviewer comments or comments from consortium 
- This repo uses CI (continuous integration) to build the paper, the build must pass before PR can be merged, to ensure no-one breaks the paper

## Structure of repo

- `notebooks` contains Jupyter notebooks, perhaps organised in subdirectories if analysis encompasses several steps.
- `content` contains included image files (PNGs) and data files (CSVs), etc. 
- Files named _descriptively_ not by likely figure position.

## Style

### Images

- Prefer PNG or PDF (vector). 
- Preferred format may depend on whether using latex or pandoc (manubot) - PDF figures are good with latex but maybe not with pandoc
- Prefer 120-300 DPI
- Style rules
  - Max 8 inches wide
  - Min 6 pt font size
  - Max 10 pt font size

### Code

- All code should be reproducible by all contributors on DataLab _i.e._ read data directly from GCS
- Python module or setup notebook to hold common code and variables (avoid copying boilerplate) TBA
- Avoid too much indirection - max one level (import Python module or %run setup notebook)

## Writing code and review process

1. Work in your own fork preferred (but not essential).
  - if branch is in main repo, prefix with your username
  - branches should include the number of the quire issue they are addressing
  - branch title marked as WIP
2. Submit PRs.
  - Check CI passes
  - remove WIP label
  - link to PR from relevant quire issue(s)
  - request review
  - No further pushes to branch (to avoid conflicts)
  - upon merge, quire issue can be closed.
3. Review.
  - Reviews should check notebooks by rerunning on datalab
  - Minor changes can be requested using "request changes"
  - More substantive changes can be made by making a PR to the branch in question. Avoid pushing directly to avoid conflicts.

## Manubot

<!-- usage note: do not edit this section -->

Manubot is a system for writing scholarly manuscripts via GitHub.
Manubot automates citations and references, versions manuscripts using git, and enables collaborative writing via GitHub.
An [overview manuscript](https://greenelab.github.io/meta-review/ "Open collaborative writing with Manubot") presents the benefits of collaborative writing with Manubot and its unique features.
The [rootstock repository](https://git.io/fhQH1) is a general purpose template for creating new Manubot instances, as detailed in [`SETUP.md`](SETUP.md).
See [`USAGE.md`](USAGE.md) for documentation how to write a manuscript.

Please open [an issue](https://git.io/fhQHM) for questions related to Manubot usage, bug reports, or general inquiries.

### Repository directories & files

The directories are as follows:

+ [`content`](content) contains the manuscript source, which includes markdown files as well as inputs for citations and references.
  See [`USAGE.md`](USAGE.md) for more information.
+ [`output`](output) contains the outputs (generated files) from Manubot including the resulting manuscripts.
  You should not edit these files manually, because they will get overwritten.
+ [`webpage`](webpage) is a directory meant to be rendered as a static webpage for viewing the HTML manuscript.
+ [`build`](build) contains commands and tools for building the manuscript.
+ [`ci`](ci) contains files necessary for deployment via continuous integration.

### Local execution

The easiest way to run Manubot is to use [continuous integration](#continuous-integration) to rebuild the manuscript when the content changes.
If you want to build a Manubot manuscript locally, install the [conda](https://conda.io) environment as described in [`build`](build).
Then, you can build the manuscript on POSIX systems by running the following commands from this root directory.

```sh
# Activate the manubot conda environment (assumes conda version >= 4.4)
conda activate manubot

# Build the manuscript, saving outputs to the output directory
bash build/build.sh

# At this point, the HTML & PDF outputs will have been created. The remaining
# commands are for serving the webpage to view the HTML manuscript locally.
# This is required to view local images in the HTML output.

# Configure the webpage directory
manubot webpage

# You can now open the manuscript webpage/index.html in a web browser.
# Alternatively, open a local webserver at http://localhost:8000/ with the
# following commands.
cd webpage
python -m http.server
```

Sometimes it's helpful to monitor the content directory and automatically rebuild the manuscript when a change is detected.
The following command, while running, will trigger both the `build.sh` script and `manubot webpage` command upon content changes:

```sh
bash build/autobuild.sh
```

### Continuous Integration

Whenever a pull request is opened, CI (continuous integration) will test whether the changes break the build process to generate a formatted manuscript.
The build process aims to detect common errors, such as invalid citations.
If your pull request build fails, see the CI logs for the cause of failure and revise your pull request accordingly.

When a commit to the `master` branch occurs (for example, when a pull request is merged), CI builds the manuscript and writes the results to the [`gh-pages`](https://github.com/malariagen/ag1000g-phase3-data-paper/tree/gh-pages) and [`output`](https://github.com/malariagen/ag1000g-phase3-data-paper/tree/output) branches.
The `gh-pages` branch uses [GitHub Pages](https://pages.github.com/) to host the following URLs:

+ **HTML manuscript** at https://malariagen.github.io/ag1000g-phase3-data-paper/
+ **PDF manuscript** at https://malariagen.github.io/ag1000g-phase3-data-paper/manuscript.pdf

For continuous integration configuration details, see [`.github/workflows/manubot.yaml`](.github/workflows/manubot.yaml) if using GitHub Actions or [`.travis.yml`](.travis.yml) if using Travis CI.

## License

[![License: CC BY 4.0](https://img.shields.io/badge/License%20All-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)

Except when noted otherwise, the entirety of this repository is licensed under a CC BY 4.0 License ([`LICENSE.md`](LICENSE.md)), which allows reuse with attribution.
Please attribute by linking to https://github.com/malariagen/ag1000g-phase3-data-paper.

All files are licensed under CC BY 4.0.

Please open [an issue](https://github.com/malariagen/ag1000g-phase3-data-paper/issues) for any question related to licensing.
