import torch
import torch.cuda
from torch.autograd import Variable
import unittest
import sys
import pytorch_colors as colors

class TestColorConversion(unittest.TestCase):
    def test_yuv(self):
        a = torch.randn(1, 3, 512, 512).clamp(0, 1)
        a_yuv = colors.rgb_to_yuv(a)
        a_ = colors.yuv_to_rgb(a_yuv)
        mean_err = (a-a_).abs().mean().item()
        self.assertAlmostEqual(mean_err, 0, 6)

    def test_ycbcr(self):
        a = torch.randn(1, 3, 512, 512).clamp(0, 1)
        a_ycbcr = colors.rgb_to_ycbcr(a)
        a_ = colors.ycbcr_to_rgb(a_ycbcr)
        mean_err = (a-a_).abs().mean().item()
        self.assertAlmostEqual(mean_err, 0, 6)

    def test_cielab(self):
        a = torch.randn(1, 3, 512, 512).clamp(0, 1)
        a_lab = colors.rgb_to_lab(a)
        a_ = colors.lab_to_rgb(a_lab)
        mean_err = (a-a_).abs().mean().item()
        self.assertAlmostEqual(mean_err, 0, 6)

    def test_hsv(self):
        a = torch.randn(1, 3, 512, 512).clamp(0, 1)
        a_lab = colors.rgb_to_hsv(a)
        a_ = colors.hsv_to_rgb(a_lab)
        mean_err = (a-a_).abs().mean().item()
        self.assertAlmostEqual(mean_err, 0, 6)

    def test_hed(self):
        a = torch.randn(1, 3, 512, 512).clamp(0, 1)
        a_lab = colors.rgb_to_hed(a)
        a_ = colors.hed_to_rgb(a_lab)
        mean_err = (a-a_).abs().mean().item()
        self.assertAlmostEqual(mean_err, 0, 6)

    def test_xyz(self):
        a = torch.randn(1, 3, 512, 512).clamp(0, 1)
        a_lab = colors.rgb_to_xyz(a)
        a_ = colors.xyz_to_rgb(a_lab)
        mean_err = (a-a_).abs().mean().item()
        self.assertAlmostEqual(mean_err, 0, 6)


class TestCudaConversion(unittest.TestCase):
    def test_keep_cuda(self):
        a = torch.randn(3, 512, 512).clamp(0, 1).cuda()
        a_yuv = colors.rgb_to_yuv(a)
        self.assertTrue(a_yuv.is_cuda)
        a_ = colors.yuv_to_rgb(a_yuv)
        self.assertTrue(a_.is_cuda)

    def test_no_cuda(self):
        a = torch.randn(3, 512, 512).clamp(0, 1)
        a_yuv = colors.rgb_to_yuv(a)
        self.assertFalse(a_yuv.is_cuda)
        a_ = colors.yuv_to_rgb(a_yuv)
        self.assertFalse(a_.is_cuda)


class Test3dTo4dConversion(unittest.TestCase):
    def test_3d(self):
        a = torch.randn(3, 512, 512).clamp(0, 1)
        a_yuv = colors.rgb_to_yuv(a)
        self.assertEqual(a_yuv.dim(), 3, 1)
        a_ = colors.yuv_to_rgb(a_yuv)
        self.assertEqual(a_.dim(), 3, 1)

    def test_4d(self):
        a = torch.randn(1, 3, 512, 512).clamp(0, 1)
        a_yuv = colors.rgb_to_yuv(a)
        self.assertEqual(a_yuv.dim(), 4, 1)
        a_ = colors.yuv_to_rgb(a_yuv)
        self.assertEqual(a_.dim(), 4, 1)


if __name__ == '__main__':
    unittest.main()
