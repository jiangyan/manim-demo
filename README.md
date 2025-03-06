# Manim Pythagorean Theorem Demonstration

This repository contains a demonstration of the Pythagorean Theorem using Manim, a mathematical animation engine.

## Overview

This project showcases the power of Manim for creating mathematical animations. It includes several scenes that demonstrate the Pythagorean Theorem in different ways:

1. **PythagoreanTheorem**: A basic demonstration of the theorem with visual and algebraic proofs
2. **PythagoreanVisualProof**: A visual proof showing how the areas relate
3. **InteractiveExploration**: Exploration of different right triangles and verification of the theorem

## Installation

### Prerequisites

- Python 3.6+
- FFmpeg
- LaTeX distribution (MiKTeX or TeX Live)

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. To install Manim using uv:

```bash
# Install uv if you don't have it
pip install uv

# Create a virtual environment
uv venv

# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Install Manim
uv pip install manim

# Install additional dependencies if needed
uv pip install numpy scipy
```

### Alternative Installation Methods

You can also install Manim using pip directly:

```bash
pip install manim
```

Or using Conda:

```bash
conda create -n manim-env python=3.9
conda activate manim-env
conda install -c conda-forge manim
```

## Usage

To render a scene, use the following command:

```bash
# Using uv
uv run manim -pql pythagorean_theorem.py PythagoreanTheorem

# Or if you've activated the virtual environment
manim -pql pythagorean_theorem.py PythagoreanTheorem
```

Command-line options:
- `-p`: Preview the animation once it's done rendering
- `-l`: Use low quality (faster rendering)
- `-m`: Use medium quality
- `-h`: Use high quality (slower rendering)
- `-q`: Quiet mode (less output)

## Available Scenes

### PythagoreanTheorem

The main scene demonstrating the Pythagorean Theorem with a 3-4-5 right triangle. It shows:
- The basic theorem statement (a² + b² = c²)
- Visual representation with squares on each side
- Area calculations
- Algebraic proof

### PythagoreanVisualProof

A visual proof of the theorem using two identical squares with different arrangements of triangles.

### InteractiveExploration

Explores different right triangles (3-4-5, 5-12-13, and 1-1-√2) to show that the theorem holds for all right triangles.

## Project Structure

- `pythagorean_theorem.py`: Main code containing all the scenes
- `hello.py`: Simple hello world script

## Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Manim GitHub Repository](https://github.com/ManimCommunity/manim)
- [Manim Discord Server](https://discord.gg/mMRrZQW)

## License

This project is open source and available under the MIT License.
