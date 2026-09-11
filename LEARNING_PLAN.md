# Daily Computer Vision and Optical Metrology Learning Plan

Owner: ahmetalpkilic. Goal: learn by running, modifying and validating one focused project per day. Each repository should take roughly 30–60 minutes to explore, require no proprietary data, and include a plain-language derivation, one-command demo, expected results, meaningful tests, 3–5 exercises and honest limitations.

## Starter projects published together

1. [Planar homography](https://github.com/ahmetalpkilic/planar-homography-learning-lab): perspective geometry and planar distances.
2. [Four-step interferometry](https://github.com/ahmetalpkilic/four-step-interferometry-learning-lab): quadrature phase and relative reflective height.

These are the first two lessons, created together to establish both tracks. The daily automation continues with the next unfinished lesson; it should not recreate them.

## Integrated camera–optics–vision–mathematics curriculum

User priority: focus on the intersection of all four disciplines. Each project must connect a physical image-formation model, explicit camera parameters/units, a vision inference or measurement task, and a mathematical derivation with an error experiment. Alternating isolated optics and vision exercises is no longer the main organizing principle.

Additional completed starter: [Lens distortion and measurement](https://github.com/ahmetalpkilic/lens-distortion-measurement-learning-lab). Simulate a radial lens model, map through focal length and pixel pitch, invert distortion and quantify planar length bias. This replaces the previously planned generic radial-distortion lesson.

## Next daily projects, in order

| Order | Specific project | Connection and deliverable |
|---|---|---|
| 1 | Diffraction versus camera sampling | Wavelength + f-number -> optical MTF; pixel pitch + pixel aperture -> sampled contrast. Compare Nyquist, aliasing and resolvable chart detail using Fourier analysis. |
| 2 | Defocus and subpixel edge precision | Lens defocus + pixel integration + noise -> edge profiles -> subpixel localization bias and repeatability. Distinguish precision from resolution. |
| 3 | Calibration target geometry and uncertainty | Camera projection + radial distortion -> noisy checkerboard coordinates -> parameter fitting and held-out reprojection/length errors. |
| 4 | Wavefront aberration to camera image | Explicit Zernike convention + complex pupil -> FFT PSF -> sampled image -> feature-localization error. |
| 5 | Stereo depth under optical blur | Focal length, baseline and pixel pitch -> blurred/noisy stereo pair -> disparity -> depth uncertainty and Monte Carlo check. |
| 6 | Structured-light phase to surface height | Camera/projector geometry + fringes -> phase recovery -> triangulation; expose phase ambiguity and calibration sensitivity. |
| 7 | Photon noise to centroid precision | Photon counts, PSF width and read noise -> simulated star/spot images -> centroid estimation -> bias, repeatability and a stated statistical bound. |
| 8 | Rolling shutter and motion metrology | Exposure/readout timing + image motion -> row-dependent geometry -> estimate speed and demonstrate correction limits. |
| 9 | Chromatic aberration and color registration | Wavelength-dependent blur/magnification -> RGB camera images -> channel alignment -> residual dimensional bias. |
| 10 | Physics-based image restoration | Known optical PSF + sensor noise -> blurred image -> regularized inversion; compare sharpness, noise amplification and measurement accuracy. |
| 11 | Telecentric versus perspective measurement | Compare projection models under object-depth changes -> dimensional measurement -> derive depth-sensitivity and calibration limits. |
| 12 | Differentiable optical parameter fitting | Simulated PSF/images -> fit a small set of defocus/aberration parameters -> gradients, identifiability and held-out recovery. |

These are proposed future projects, not existing repositories. Keep daily implementations small and runnable; split a difficult topic into focused successive lessons when needed. Explain idealized assumptions and do not imply synthetic performance establishes hardware accuracy.

Retain the earlier RANSAC, fringe-noise, Zernike, uncertainty and deep-learning ideas as prerequisites or extensions within this integrated sequence. Next project is diffraction versus camera sampling, unless memory records it complete. Check local repositories and memory before building; a new lesson may revisit an existing concept only with a materially new cross-disciplinary experiment.

For every project, include a **four-way connection** table, a forward model, an inverse/measurement task, an error budget or controlled sensitivity experiment, and 3–5 exercises. Use metres/mm/micrometres/nm and pixels explicitly; state wavelength, aperture, coordinate, sampling and noise conventions as applicable. Validate against an analytic special case or independent known answer. Review active public implementations and reuse licenses before selecting dependencies.

## Learning workflow for each day

1. Read the question and predict the ideal result.
2. Run the deterministic demo and inspect outputs.
3. Read the short mathematical explanation alongside the core function.
4. Change one parameter and explain the error or failure.
5. Run tests and complete one extension exercise.

## Publishing standard

Publish one new public repository per daily run under ahmetalpkilic. Use descriptive names and original code or appropriately attributed permissive dependencies. Verify the remote commit and uploaded files before reporting success. Include provenance and test results. Never present simulation accuracy as validated instrument performance. Prefer existing authenticated local Git for pushes; the GitHub connector may create repositories but previously rejected contents writes.
