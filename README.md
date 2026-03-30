# OpenCV Projects

A collection of OpenCV-based Python experiments and tutorial exercises built around computer vision concepts such as face detection, eye detection, and Harris corner detection.

## Project Overview

This repository contains sample scripts created while learning OpenCV with Python. The code demonstrates practical usage of OpenCV operations, including:

- Real-time face and eye detection using Haar cascades
- Harris corner detection with non-maximal suppression and normalization
- Image processing utilities for visualization and experimentation

## Requirements

- Python 3.14 or newer
- `opencv-contrib-python`
- `matplotlib`

The project dependencies are defined in `pyproject.toml`.

## Setup

1. Create and activate a virtual environment in the project folder:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you do not have a `requirements.txt`, install directly from `pyproject.toml` dependencies:

   ```bash
   pip install opencv-contrib-python matplotlib
   ```

## How to Run

- `python main.py`
  - A simple entry point that prints a startup message.

- `python harris_corner_cv2.py`
  - Runs a Harris corner detection demo using `assets/checkersboard.png` and displays the processing results.

- `python t9.py`
  - Runs a live webcam demo for face and eye detection with OpenCV Haar cascades.

Other scripts (`t1.py` through `t8.py`, `t8_1.py`, `t6_1.py`, `test.py`) are likely additional tutorial examples and experiments.

## Repository Structure

- `main.py` – project entry point
- `harris_corner_cv2.py` – Harris corner detection example
- `t9.py` – face and eye detection example
- `t1.py` … `t8.py`, `t8_1.py`, `t6_1.py` – tutorial/exploration scripts
- `assets/` – sample images used for demonstrations
- `pyproject.toml` – project metadata and dependency configuration

## Notes

- The `assets` folder contains sample images used by the scripts, including `checkersboard.png` for corner detection.
- Press `q` to exit the live webcam demo in `t9.py`.

## References

- OpenCV tutorials: https://opencv2-python-tutorials.readthedocs.io/en/latest/index.html
- OpenCV Haar cascade documentation and examples
