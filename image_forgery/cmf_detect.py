import argparse
from . import quant_matrix
from. import helper_utils

def cmf_Detect(imagePath):
    block_size = 8
    qf = 0.75
    shift_thresh = 10
    stride = 1
    # 8x8 quantization matrix based on QF
    Q_8x8 = quant_matrix.QuantizationMatrix().get_qm(qf)

    # read img
    img, original_image, overlay, width, height = helper_utils.read_img(imagePath)

    # DCT
    quant_row_matrices = helper_utils.create_quantize_dct(img, width, height, block_size, stride, Q_8x8)

    # lexographic sort
    shift_vec_count, matched_blocks = helper_utils.lexographic_sort(quant_row_matrices)

    # shift vector threhsolding
    matched_pixels_start = helper_utils.shift_vector_thresh(shift_vec_count, matched_blocks, shift_thresh)

    # displaying output
    result_image_path = helper_utils.display_results(overlay, original_image, matched_pixels_start, block_size)
    return result_image_path

if __name__ == "__main__":

    # Create the parser
    parser = argparse.ArgumentParser()
    
    # Add an argument
    parser.add_argument('--img', required=True, help="Path of the image on which operation needs to be performed")
    parser.add_argument('--block_size', type=int, default=8, help="Block Size")
    parser.add_argument('--qf', type=float, default=0.75, help="Quality Factor")
    parser.add_argument('--shift_thresh', type=int, default=10, help="Threshold for shift vector count")
    parser.add_argument('--stride', type=int, default=1, help="Sliding window stride count / overlap")
    
    # Parse the argument
    args = parser.parse_args()
    
    img_path = args.img
    block_size = args.block_size
    qf = args.qf
    shift_thresh = args.shift_thresh
    stride = args.stride

    # 8x8 quantization matrix based on QF
    Q_8x8 = quant_matrix.QuantizationMatrix().get_qm(qf)

    # read img
    img, original_image, overlay, width, height = helper_utils.read_img(img_path)

    # DCT
    quant_row_matrices = helper_utils.create_quantize_dct(img, width, height, block_size, stride, Q_8x8)

    # lexographic sort
    shift_vec_count, matched_blocks = helper_utils.lexographic_sort(quant_row_matrices)

    # shift vector threhsolding
    matched_pixels_start = helper_utils.shift_vector_thresh(shift_vec_count, matched_blocks, shift_thresh)

    # displaying output
    helper_utils.display_results(overlay, original_image, matched_pixels_start, block_size)
