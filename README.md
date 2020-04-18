# marbleextractor

A Python 3 script to extract the contents of the `marble.bza` archive from Marble Blast Ultra on Xbox Live Arcade

## Usage

1. Obtain a copy of the Xbox Live Arcade title Marble Blast Ultra for Xbox 360. Its title ID is `FAFF44B4C6642F88B541801FD506FEEEF72D8E8258`.
1. Use [wxPirs 1.1](https://digiex.net/threads/wxpirs-extract-content-from-xbox-360-demos-video-dlc-and-arcade-game-containers.9464/) to extract the Xbox Live Arcade title.
1. In the resulting extracted directory, you'll find assets like `default.xex`, `Tim_Trance.wma`, and `marble.bza`.
1. Copy `marble.bza` into this directory.
1. Run `./extract.py` to extract the contents.

## Notes

* `*.jng` files can be converted to PNG with the `convert` command line tool that ships with ImageMagick, e.g. `convert grow.jng grow2.png`.
