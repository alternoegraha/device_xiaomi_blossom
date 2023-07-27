Unified device tree for Xiaomi Redmi 9A family devices (blossom)
================================================================

```
#
# Copyright (C) 2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#
```

## Included devices

### `dandelion`

+ Redmi 9A
+ Redmi 9I
+ Redmi 9I Sport
+ Redmi 10A

### `angelica`

+ Redmi 9C

### `angelican`

+ Redmi 9C NFC

### `cattail`
+ Redmi 9 Active
+ Redmi 9 India
+ Redmi 9A sport
+ Redmi 9AT

### `angelicain`

+ Poco C3
+ Poco C31

## Note

Although I have access to the original blossom device tree (which is closed-source by its authors for now), I write this tree completely from scratch by reversing and comparing blobs. No code is copied from the original device tree, and I don't read any code in the original tree to create this open-source tree.

So don't expect this device tree will be complete (and ofc it does not have the complete commit history), and it may include some dirty changes extracted from the dump. Also it's just for fun and learning purposes, bcs I am a complete noob. Bugs are expected.

Using [@Sushrut1101](https://github.com/Sushrut1101) (the original blossom device tree developer)'s kernel headers and vendor tree from [xiaomi-mt6765-dev](https://github.com/xiaomi-mt6765-dev) and [Xiaomi-MT6765](https://gitlab.com/Xiaomi-MT6765), since they are already open-source.



## How to Build using this fork??
On `Ubuntu 22.04 LTS`
Install dependencies:
```
sudo apt install bc bison build-essential ccache curl flex g++-multilib gcc-multilib git git-lfs gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev libelf-dev liblz4-tool libncurses5 libncurses5-dev libsdl1.2-dev libssl-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev
```
Create some directories:
```
mkdir -p ~/bin
mkdir -p ~/lineage
```
Install repo & Configure git:
```
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
export PATH="$HOME/bin:$PATH"

git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```
Initialize your local repository:
```
cd ~/lineage && pwd
repo init -u https://github.com/LineageOS/android.git -b lineage-20.0 --git-lfs
git clone https://github.com/snnbyyds/local_manifests-blossom.git .repo/local_manifests
```
Sync the code:
```
repo sync
```
Build it:
```
export USE_CCACHE=1
ccache -M 50G

source build/envsetup.sh
breakfast blossom
brunch blossom
```
