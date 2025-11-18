import os
import glob
from PIL import Image

# Determine the project base directory from this script's location.
# This assumes your script is in myproject/utils/ and project root is one level up.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input folder: myproject/static/imgs
INPUT_FOLDER = os.path.join(BASE_DIR, "static", "imgs")
# Output folder: myproject/static/imgs_optimized (or any folder you prefer)
OUTPUT_FOLDER = os.path.join(BASE_DIR, "static", "imgs_optimized")

# Settings for resizing and compression
DESKTOP_WIDTH = 1000      # Target width for desktop images
MOBILE_WIDTH = 400        # Target width for mobile images
WEBP_QUALITY = 80         # Quality for WebP (0-100)
JPG_QUALITY = 80          # Quality for JPEG fallback

# Create the output folder if it doesn't exist
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def resize_image(img, target_width):
    """Resize an image maintaining the aspect ratio if needed."""
    orig_width, orig_height = img.size
    if orig_width > target_width:
        target_height = int((target_width / orig_width) * orig_height)
        return img.resize((target_width, target_height), Image.LANCZOS)
    return img

def process_image(image_path):
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    with Image.open(image_path) as img:
        # Convert image to RGB mode if not already (necessary for WebP and JPEG)
        if img.mode != "RGB":
            img = img.convert("RGB")
        
        # Create resized versions for desktop and mobile
        desktop_img = resize_image(img, DESKTOP_WIDTH)
        mobile_img = resize_image(img, MOBILE_WIDTH)

        # Save desktop versions
        desktop_webp = os.path.join(OUTPUT_FOLDER, f"{base_name}_desktop.webp")
        desktop_jpg  = os.path.join(OUTPUT_FOLDER, f"{base_name}_desktop.jpg")
        desktop_img.save(desktop_webp, "WEBP", quality=WEBP_QUALITY)
        desktop_img.save(desktop_jpg, "JPEG", quality=JPG_QUALITY, optimize=True)
        
        # Save mobile versions
        mobile_webp = os.path.join(OUTPUT_FOLDER, f"{base_name}_mobile.webp")
        mobile_jpg  = os.path.join(OUTPUT_FOLDER, f"{base_name}_mobile.jpg")
        mobile_img.save(mobile_webp, "WEBP", quality=WEBP_QUALITY)
        mobile_img.save(mobile_jpg, "JPEG", quality=JPG_QUALITY, optimize=True)

        print(f"Processed {image_path}:\n  Desktop: {desktop_webp}, {desktop_jpg}\n  Mobile: {mobile_webp}, {mobile_jpg}")

def main():
    # Look for image files with common extensions (jpg, jpeg, png) in the input folder
    image_files = []
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        image_files.extend(glob.glob(os.path.join(INPUT_FOLDER, ext)))
    
    if not image_files:
        print("No images found in the input folder:", INPUT_FOLDER)
        return

    print(f"Found {len(image_files)} images in '{INPUT_FOLDER}'.")
    for image_path in image_files:
        try:
            process_image(image_path)
        except Exception as e:
            print(f"Error processing {image_path}: {e}")

if __name__ == "__main__":
    main()
