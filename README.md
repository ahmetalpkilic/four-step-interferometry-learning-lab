# Four-Step Interferometry Learning Lab

**Lesson 2: reconstruct optical phase from four intensity measurements.**

A 30–45 minute NumPy/Pillow experiment for learning quadrature phase retrieval, phase wrapping, modulation masking and the distinction between optical path difference and reflective surface height. All examples are synthetic; no instrument or model weights are needed.

## Setup and experiments

Python 3.9+:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python lab.py --unwrap
python -m unittest -v
python lab.py --noise 0.01 --unwrap --out output-noisy
python lab.py --step-error-deg 2 --unwrap --out output-step-error
```

The ideal demo should have wrapped phase RMSE below `1e-12 rad` and piston-removed surface-height RMSE below `1e-9 nm` (floating-point numerical recovery, not instrument precision). Compare the noisy and phase-step-error runs to the ideal result.

## Derivation

Assume four measurements `I_k = a + b cos(phi + k*pi/2)` for k=0,1,2,3. Their differences remove the constant background:

- `I0-I2 = 2b cos(phi)`
- `I3-I1 = 2b sin(phi)`

Thus `phi = atan2(I3-I1, I0-I2)`, wrapped to [-pi,pi], and modulation amplitude `b = hypot(I0-I2,I3-I1)/2`. Pixels with b below the threshold are invalid. This b is intensity amplitude, not normalized fringe visibility b/a.

For normal-incidence reflection, phase corresponds to round-trip optical path: `height = wavelength*phase/(4*pi)`. Transmission OPD would use `wavelength*phase/(2*pi)` instead and is not the height geometry used here. Mean height is removed because absolute piston/fringe order is unknown. Tilt and curvature are retained.

Read `synthesize`, `reconstruct`, then `smooth_unwrap` in `lab.py`.

## Outputs and custom data

- `results.json`: validity, phase RMSE against synthetic truth and optional relative-height RMSE.
- `maps.npz`: original frames, wrapped phase in radians, modulation and validity mask; relative height in nm when unwrapping is requested.
- `frame_0.png` through `frame_3.png`: intensity previews clipped to [0,1]. Reconstruction uses the original floating-point data, without preview clipping.
- `wrapped_phase.png`: grayscale from -pi (black) to pi (white). Invalid pixels are also black; use the NPZ validity mask to distinguish them.

```sh
python lab.py --input frames.npy --min-modulation 0.02 --out my-output
```

`frames.npy` must contain a finite numeric array of shape (4,H,W), using the **same** intensity scale for every frame and ordered phase steps 0, pi/2, pi, 3pi/2. Adjust the modulation threshold to that intensity scale. Output files are overwritten in the selected directory.

## Exercises

1. Verify the two intensity-difference identities by hand at phi=0 and phi=pi/2.
2. Sweep noise from 0 to 0.02. Compare phase RMSE and height RMSE at 532 nm and 632.8 nm.
3. Change modulation from 0.35 to 0.05 in `synthesize`. Why does the same intensity noise hurt more?
4. Add a 2-degree phase-step error. Does averaging away intensity noise remove the resulting systematic error?
5. Increase phase slope until neighbouring pixels differ by more than pi. Explain why simple unwrapping can fail.

## Validation and limitations

Four tests cover analytical quadrature values, phase sign and smooth unwrapping, low-modulation masking and sensitivity to nonideal phase steps. These are mathematical/synthetic checks only.

`--unwrap` is deliberately limited: sequential one-dimensional NumPy unwrap along rows then columns, suitable only for smooth, fully valid rectangular fields with adjacent true phase differences below pi. It rejects any invalid pixels. Discontinuities, residues, holes, undersampling and noise can make the result wrong; no general masked 2D phase-unwrapping solver is claimed.

Assumes exact quarter-wave phase steps, stable illumination, stationary scene, linear unsaturated camera and adequate fringe contrast. Real metrology needs phase-step calibration, reference subtraction, wavelength/geometry control and an uncertainty budget. Low modulation is masked, but saturation and motion are not detected.

## Sources and license

- [prysm phase-shifting interferometry documentation](https://prysm.readthedocs.io/en/latest/api/x/psi.html), conceptual/practical inspiration.
- [brandondube/prysm](https://github.com/brandondube/prysm), MIT license inspected; repository activity and exact commit recorded in `sources.json`.

This is original educational code with original synthetic data; no upstream implementation, weights or datasets were copied. App code is MIT; installed NumPy and Pillow retain their own licenses. See [LEARNING_PLAN.md](LEARNING_PLAN.md) for the daily roadmap.
