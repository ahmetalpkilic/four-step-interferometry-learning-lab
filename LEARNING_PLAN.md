# Daily Computer Vision and Optical Metrology Learning Plan

Owner: ahmetalpkilic. Goal: learn by running, modifying and validating one focused project per day. Each repository should take roughly 30–60 minutes to explore, require no proprietary data, and include a plain-language derivation, one-command demo, expected results, meaningful tests, 3–5 exercises and honest limitations.

## Starter projects published together

1. [Planar homography](https://github.com/ahmetalpkilic/planar-homography-learning-lab): perspective geometry and planar distances.
2. [Four-step interferometry](https://github.com/ahmetalpkilic/four-step-interferometry-learning-lab): quadrature phase and relative reflective height.

These are the first two lessons, created together to establish both tracks. The daily automation continues with the next unfinished lesson; it should not recreate them.

## Next 12 daily lessons

| Order | Track | Project | What you should learn |
|---|---|---|---|
| 3 | Vision | Robust line fitting with RANSAC | Outliers, residuals, reproducible sampling |
| 4 | Metrology | Fringe visibility and phase-noise budget | Contrast, noise and measurement precision |
| 5 | Vision | Radial lens distortion simulation and correction | Distortion coefficients and reprojection error |
| 6 | Metrology | Zernike wavefront fitting | Piston, tilt, defocus, masks and RMS conventions |
| 7 | Vision | Subpixel edge localization | Sampling, interpolation and edge-position bias |
| 8 | Metrology | Fresnel diffraction sampling lab | Propagation, units and sampling limits |
| 9 | Vision | Lucas–Kanade motion on synthetic patches | Brightness constancy and aperture ambiguity |
| 10 | Metrology | Thin-film reflectance at normal incidence | Complex amplitude, wavelength and refractive index |
| 11 | Vision | Stereo triangulation with uncertainty | Disparity, baseline and depth sensitivity |
| 12 | Metrology | Monte Carlo dimensional uncertainty | Calibration, repeatability and error propagation |
| 13 | Vision | Tiny trainable segmentation model | Train/test separation, masks and generalization |
| 14 | Metrology | Least-squares phase-step calibration | Model assumptions and systematic phase error |

This is a proposed curriculum, not a claim that future projects exist. Before each run, check existing repositories and memory to avoid duplicates; substitute a related unbuilt lesson when necessary. Review current public implementations and reuse licenses before selecting dependencies. Keep the topic progression coherent, and update the memory with completion and the next lesson.

## Learning workflow for each day

1. Read the question and predict the ideal result.
2. Run the deterministic demo and inspect outputs.
3. Read the short mathematical explanation alongside the core function.
4. Change one parameter and explain the error or failure.
5. Run tests and complete one extension exercise.

## Publishing standard

Publish one new public repository per daily run under ahmetalpkilic. Use descriptive names and original code or appropriately attributed permissive dependencies. Verify the remote commit and uploaded files before reporting success. Include provenance and test results. Never present simulation accuracy as validated instrument performance. Prefer existing authenticated local Git for pushes; the GitHub connector may create repositories but previously rejected contents writes.
