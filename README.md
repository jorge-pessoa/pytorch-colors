PyTorch Colors
===========
PyTorch Colors is a simple utility to **convert Tensors and Variables between color spaces**. Currently all the operations are non-differentiable.
PyTorch Colors is in early alpha, and supports the following color spaces:
1. RGB
2. HSV
3. CIE\*Lab
4. YUV
5. YCbCr
6. XYZ
7. HED

Please request additional color spaces in the issues or provide a pull request with the implementation. Differentiable versions for each color space conversion will also be added in time.

## Installation and requirements

To install PyTorch Colors use the command `python setup.py install` inside the repository directory. 
PyTorch Colors requires the default PyTorch (version > 0.3) installation and scikit-image (version > 0.1) to work.

## Usage

 All PyTorch-Colors methods from color space C1 to color space C2 are named `c1_to_c2(img)`. Either c1 or c2 must be RGB, so all color spaces can be converted between each other by going through the RGB color space.
 
 All the methods expect a FloatTensor and output a FloatTensor. 

 ```python
 import pytorch_colors as colors
 
 img = torch.randn(1, 3, 256, 256) # example image in RGB
 img_hsv = colors.rgb_to_hsv(img)
 
 # hsv -> ycbcr
 img = colors.hsv_to_rgb(img_hsv)
 img_ycbcr = colors.rgb_to_ycbcr(img)
  
 ```

The supported inputs are either 3 dimensional `(channel, width, height)` or 4 dimensional `(batch_size, channel, width, height)` images. So the following is also valid:

 ```python
 img = torch.randn(3, 256, 256) # example image in RGB
 img_hsv = colors.rgb_to_hsv(img) # output is also 3 dimensional
 ```

The supported inputs are Tensors and Variables, with or without cuda activated and the output should be consistent with the input.

 ```python
 img = torch.randn(1, 3, 256, 256) # example image in RGB
 v_img = Variable(torch.randn(1, 3, 256, 256)) # example Variable image in RGB
 c_v_img = v_img.cuda() # with CUDA activated

 img_hsv = colors.rgb_to_hsv(img) # output is Tensor
 v_img_hsv = colors.rgb_to_hsv(img) # output is Variable
 c_v_img_hsv = colors.rgb_to_hsv(img) # output is CUDA Variable
 ```

A method with string input is also provided, and can be used for example with script arguments. The string input to convert from c1 to c2 should be `c1toc2`. I.e: `rgb2hsv` to convert from RGB to HSV.

 ```python
 import pytorch_colors as colors

 parser = argparse.ArgumentParser()
 parser.add_argument('-c', '--color', help='...') 
 (...)
 cfg = parser.parse_args()
 input_ = colors.convert(input_, cfg.color)
 ```
 You can find more examples in the tests/ folder.

