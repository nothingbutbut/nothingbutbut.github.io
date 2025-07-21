"""
Compressing a image to certain size.
Usage:
    python compress.py <input_image> <output_image> <target_width> <target_height>
Where:
    input_image: The path to the input image file.
    output_image: The path to save the compressed image file.
    target_width: The target width in pixels for the compressed image.
    target_height: The target height in pixels for the compressed image.
"""
import sys
from PIL import Image

def compress_image(input_image, output_image, target_width, target_height):
    try:
        # Open the input image
        with Image.open(input_image) as img:
            # Resize the image to the target dimensions
            img = img.resize((target_width, target_height), Image.LANCZOS)
            # Save the compressed image to the output path
            img.save(output_image, quality=85, optimize=True)
            print(f"Image compressed and saved to {output_image}")
    except Exception as e:
        print(f"Error compressing image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python compress.py <input_image> <output_image> <target_width> <target_height>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2]
    target_width = int(sys.argv[3])
    target_height = int(sys.argv[4])

    compress_image(input_image, output_image, target_width, target_height)