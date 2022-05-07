# Store original full-res images in assets/photography/originals/
# TODO: one could add some more info to the gallery.yaml, for example title and caption. We should add functionality to
#  this script so as we load the previous gallery and add new images, in a non-destructive way. See original code


import yaml
import shutil
import cv2 as cv
from pathlib import Path

# configuration
BASE_DIR = Path("assets/photography")
OUTPUT_FILE = BASE_DIR / "photography.yml"
INPUT_FILE = OUTPUT_FILE
SUBDIR = "originals"
IMAGE_DIR = BASE_DIR / SUBDIR
EXTENSIONS = ['jpg', 'png']


def get_files_recursively(base_dir, extensions):
    all_files = []
    for ext in extensions:
        all_files.extend(Path(base_dir).rglob(f"*.{ext}"))
    return sorted(all_files)


# Extract image files
print('Collecting files...')
images_paths = get_files_recursively(IMAGE_DIR, EXTENSIONS)

images_data = []
for img_path in images_paths:
    img_name = img_path.stem
    img_ext = img_path.suffix

    # Create down-sampled versions of the image and save them to disk
    img = cv.imread(str(img_path))
    image_paths = []
    output_path = BASE_DIR / f"{img_name}.jpg"
    image_paths.append(output_path)
    if not output_path.exists():
        cv.imwrite(str(output_path), img)
    resized_image = img
    for scale_factor in range(1, 5):
        output_path = BASE_DIR / f"{img_name}_factor-{2 ** scale_factor:02d}.jpg"
        image_paths.append(output_path)
        resized_image = cv.resize(resized_image, (0, 0), None, 0.5, 0.5)
        if not output_path.exists():
            cv.imwrite(str(output_path), resized_image)

    # Add to data structure
    images_data.append(
        {
            "filename": img_name,
            "original": str(image_paths[0].name),
            "sizes": [str(path.name) for path in image_paths],
            "thumbnail": str(image_paths[-1].name)
        }
    )

# Save and override gallery
gallery = {
    "picture_path": SUBDIR,
    "preview": images_data
}
with open(OUTPUT_FILE, 'w') as f:
    f.write(yaml.dump(gallery, default_flow_style=False))
