# AlgeGloves
## _An Interactive Algebra Interface that allows Students to Mold Algebraic Functions_

This is the code used for the simulations during my research internship at Carnegie Mellon University as part of the RISS 2021 program.

The current application works to provide two main interactive simulations for the user. The user can control a Line and a Parabola, interacting with a precalibrated pair of gloves.

We encourage everyone interested in this work to review the paper published at the RISS 2021 JOURNAL prior to check this code.

## Setup

AlgeGloes require python 3.8.
Install the dependencies and packages using the requirements file.

We suggest you to create a [conda](https://docs.anaconda.com/anaconda/install/) environment to have your work more organized.
After you have successfully installed conda, the next step is to create an environment and activate it. In linux, type:

```sh
conda create -n envRiss21 python=3
source activate envRiss21
```
Then, you may install the requirements needed for the project.
```sh
pip install requirements.txt
```

## Running the Code
The first step is to calibrate the colors of the glove using the calibration script provided. Inside the script, move the sliders to match the desired filter colors.
```sh
python3 paperversion/Calibration.py --camera Web-Cam
```
Move the last slider to save the colors 
- 1 for right hand colors.
- 2 for left hand colors.

Colors will be automatically saved when you close the script.

To run the simulations do it as:
```sh
python3 paperversion/Parabola.py --camera Web-Cam
```
That's it, enjoy the interface.
