---
layout: post
title: Install PyTorch and Tensorflow with M1 support
---

Python3.9
Conda virtual environment

## Pre-requisites

`xcode-select --install`

## Miniforge

https://github.com/conda-forge/miniforge

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
chmod +x Miniforge3-MacOSX-arm64.sh
./Miniforge3-MacOSX-arm64.sh
```

### Add to system path

Open .bashrc (or .zshrc) and add: `export PATH="/Users/<USER>/miniforge3/bin:$PATH"`

### Useful conda config

`conda config --set auto_activate_base false`

## Check OSX version

```python
import platform
platform.platform()
```

Should be someting like `macOS-12.4-arm64-arm-64bit`
2 important things to check:
- `12.4` is the version of OSX. Must be `12.3` or above
- `arm64`. Could also be `x86`. In that case you need to create an ARM conda environment for python

# Create virtualenv

```bash
conda config --set auto_activate_base false
CONDA_SUBDIR=osx-arm64 conda create -n .env python=3.9 -c conda-forge
```

# Install pytorch (check the official site just in case this command changes)

```bash
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
```

# Install Tensorflow and Metal plugin

```bash
pip install tensorflow-macos
pip install tensorflow-metal
```

# Troubleshoot

## Pycharm Error. 

Error loading: /Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevd_attach_to_process/attach_x86_64.dylib

The solution for that error is modify the file /Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevd_attach_to_process/linux_and_mac/compile_mac.sh and replace all code for the next one:

g++ -fPIC -D_REENTRANT -std=c++11 -arch arm64 -c -o attach_x86_64.o attach.cpp
g++ -dynamiclib -nostartfiles -arch arm64 -o attach_x86_64.dylib attach_x86_64.o -lc
rm attach_x86_64.o
mv attach_x86_64.dylib ../attach_x86_64.dylib

Source: https://youtrack.jetbrains.com/issue/PY-51483

# Testing

Refer to Sebastian Raschka's tests: https://github.com/rasbt/machine-learning-notes/tree/main/benchmark/pytorch-m1-gpu

# Credits

https://towardsdatascience.com/gpu-acceleration-comes-to-pytorch-on-m1-macs-195c399efcc1

https://caffeinedev.medium.com/how-to-install-tensorflow-on-m1-mac-8e9b91d93706

https://sebastianraschka.com/blog/2022/pytorch-m1-gpu.html 
