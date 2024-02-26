
from PIL import Image

def apply_sepia(image):
    width, height = image.size
    sepia_matrix = (
        (0.7, 0.769, 0.189),
        (0.1, 0.686, 0.168),
        (0.1, 0.534, 0.131)
    )



    sepia_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            new_r = int((r * sepia_matrix[0][0]) + (g * sepia_matrix[0][1]) + (b * sepia_matrix[0][2]))
            new_g = int((r * sepia_matrix[1][0]) + (g * sepia_matrix[1][1]) + (b * sepia_matrix[1][2]))
            new_b = int((r * sepia_matrix[2][0]) + (g * sepia_matrix[2][1]) + (b * sepia_matrix[2][2]))

            # Make sure the values are within 0-255 range
            new_r = min(255, new_r)
            new_g = min(255, new_g)
            new_b = min(255, new_b)

            sepia_image.putpixel((x, y), (new_r, new_g, new_b))

    return sepia_image

if __name__ == "__main__":
    # Load image
    input_image_path = "787-9_front.JPG"
    output_image_path = "sepia_image.jpg"
    original_image = Image.open(input_image_path)

    # Apply sepia filter
    sepia_image = apply_sepia(original_image)

    # Save sepia image
    sepia_image.save(output_image_path)
