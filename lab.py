"""Four-step phase-shifting interferometry learning lab (MIT)."""
import argparse
import json
from pathlib import Path
import numpy as np
from PIL import Image


def reconstruct(frames, min_modulation=0.02):
    frames = np.asarray(frames, dtype=float)
    if frames.ndim != 3 or frames.shape[0] != 4 or min(frames.shape[1:]) < 2 or not np.isfinite(frames).all():
        raise ValueError('Need four finite H x W frames in order 0, pi/2, pi, 3pi/2.')
    if not np.isfinite(min_modulation) or min_modulation <= 0:
        raise ValueError('min_modulation must be positive and finite.')
    cosine, sine = frames[0]-frames[2], frames[3]-frames[1]
    modulation = np.hypot(cosine, sine)/2
    valid = modulation >= min_modulation
    phase = np.arctan2(sine, cosine)
    phase[~valid] = np.nan
    return phase, modulation, valid


def smooth_unwrap(wrapped):
    if not np.isfinite(wrapped).all():
        raise ValueError('Demo unwrapping requires a full rectangular valid field; masked data are unsupported.')
    return np.unwrap(np.unwrap(wrapped, axis=1), axis=0)


def synthesize(noise=0, step_error=0):
    y, x = np.mgrid[-1:1:128j, -1:1:192j]
    phase = 7*x + 2*y + 1.2*np.exp(-8*(x*x+y*y))
    steps = np.arange(4)*(np.pi/2+step_error)
    frames = 0.5 + 0.35*np.cos(phase[None]+steps[:,None,None])
    frames += np.random.default_rng(17).normal(0, noise, frames.shape)
    return frames, phase


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, help='NPY array with shape (4,H,W), common intensity scale')
    p.add_argument('--noise', type=float, default=0)
    p.add_argument('--step-error-deg', type=float, default=0)
    p.add_argument('--wavelength-nm', type=float, default=632.8)
    p.add_argument('--min-modulation', type=float, default=.02)
    p.add_argument('--unwrap', action='store_true', help='Smooth, fully valid synthetic-style fields only')
    p.add_argument('--out', type=Path, default=Path('output'))
    args = p.parse_args()
    if not all(np.isfinite(v) for v in [args.noise,args.step_error_deg,args.wavelength_nm]) or args.noise<0 or args.wavelength_nm<=0:
        p.error('Noise must be nonnegative; wavelength positive; all parameters finite.')
    try:
        truth = None
        if args.input:
            frames = np.load(args.input, allow_pickle=False)
        else:
            frames, truth = synthesize(args.noise, np.deg2rad(args.step_error_deg))
        wrapped, modulation, valid = reconstruct(frames, args.min_modulation)
        summary = {'valid_fraction':float(valid.mean()),'wavelength_nm':args.wavelength_nm,'unwrapped':args.unwrap,
                   'geometry':'normal-incidence reflection; relative surface height only'}
        arrays = dict(frames=frames, wrapped_phase_rad=wrapped, modulation=modulation, valid=valid)
        if truth is not None and valid.any():
            error = np.angle(np.exp(1j*(wrapped[valid]-truth[valid])))
            summary['wrapped_phase_rmse_rad'] = float(np.sqrt(np.mean(error**2)))
        if args.unwrap:
            phase = smooth_unwrap(wrapped)
            height = phase*args.wavelength_nm/(4*np.pi)
            height -= height.mean()  # Remove arbitrary piston, not tilt or curvature.
            arrays['relative_height_nm'] = height
            if truth is not None:
                expected = truth*args.wavelength_nm/(4*np.pi); expected -= expected.mean()
                summary['relative_height_rmse_nm'] = float(np.sqrt(np.mean((height-expected)**2)))
        args.out.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(args.out/'maps.npz', **arrays)
        (args.out/'results.json').write_text(json.dumps(summary, indent=2)+'\n')
        for i, frame in enumerate(frames):
            Image.fromarray(np.uint8(np.clip(frame,0,1)*255)).save(args.out/('frame_%d.png'%i))
        gray = np.where(valid, (np.nan_to_num(wrapped)+np.pi)/(2*np.pi), 0)
        Image.fromarray(np.uint8(np.clip(gray,0,1)*255)).save(args.out/'wrapped_phase.png')
        print(json.dumps(summary, indent=2))
    except (ValueError, OSError) as e:
        p.error(str(e))

if __name__ == '__main__': main()
