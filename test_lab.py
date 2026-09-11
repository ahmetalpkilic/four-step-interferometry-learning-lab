import unittest
import numpy as np
from lab import reconstruct, smooth_unwrap, synthesize
class Tests(unittest.TestCase):
    def test_phase_sign_and_recovery(self):
        frames, truth=synthesize()
        wrapped,_,v=reconstruct(frames)
        self.assertTrue(v.all())
        np.testing.assert_allclose(np.angle(np.exp(1j*(wrapped-truth))),0,atol=1e-14)
        phase=smooth_unwrap(wrapped); difference=phase-truth
        np.testing.assert_allclose(difference-difference.mean(),0,atol=1e-13)
    def test_low_modulation_mask(self):
        wrapped,_,valid=reconstruct(np.ones((4,5,6)))
        self.assertFalse(valid.any())
        self.assertTrue(np.isnan(wrapped).all())
        with self.assertRaises(ValueError): smooth_unwrap(wrapped)
    def test_quadrature_known_values(self):
        truth=np.array([[0,np.pi/2],[-np.pi/2,np.pi]])
        f=2+np.cos(truth[None]+np.arange(4)[:,None,None]*np.pi/2)
        wrapped,amp,_=reconstruct(f)
        np.testing.assert_allclose(np.angle(np.exp(1j*(wrapped-truth))),0,atol=1e-14)
        np.testing.assert_allclose(amp,1)
    def test_phase_step_error_has_effect(self):
        f,t=synthesize(step_error=.04); w,_,_=reconstruct(f)
        self.assertGreater(np.sqrt(np.mean(np.angle(np.exp(1j*(w-t)))**2)),.01)
if __name__=='__main__': unittest.main()
