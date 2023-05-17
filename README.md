# Image Forgery Detection using Python and Django
This repository contains an image forgery detection system implemented using Python and Django. The system utilizes various image processing techniques to detect forged areas within an image.

# Methodology
The image forgery detection process follows the following steps:

* Input Image: The system takes an input image for forgery detection.

* Division of Blocks: The input image is divided into blocks or patches to analyze smaller regions of the image. Each block represents a localized area that can potentially contain forged content.

* Feature Extraction using DCT: For each block, the Discrete Cosine Transform (DCT) is applied to extract frequency domain features. The DCT represents the block in terms of its frequency components.

* Dimensionality Reduction via Quantization: The extracted DCT coefficients are quantized to reduce the dimensionality of the feature space. Quantization groups similar frequency components into bins, reducing the complexity of subsequent processing steps.

* Lexicographic Sort: The quantized DCT coefficients are sorted in a lexicographic manner. Sorting helps in creating a unique representation for each block, facilitating comparison and identification of forged areas.

* Output Image: The system generates an output image where forged areas are highlighted or marked for visualization purposes. The identified forged regions can be used for further analysis or forensic examination.

# Requirements
Python 
Django
Other dependencies, as specified in the requirements.txt file

# Installation
1. Clone the repository: git clone [https://github.com/your-username/image-forgery-detection.git](https://github.com/DivyaKohli/imageForgeryDetection)
2. Change into the project directory: cd image_forgery
3. Run the Django server: python manage.py runserver

# Usage
1. Open a web browser and go to http://localhost:8000 to access the image forgery detection system.
2. Upload an image for forgery detection.
3. The system will process the image using the specified methodology and display the output image with highlighted forged areas.

# Credit
This repository is maintained by Divya Kohli, Simran Mujral, Aditi, Lavish Gupta, Balibhadra Singh, Anmol
