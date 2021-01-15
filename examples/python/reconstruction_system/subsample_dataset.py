import os 
import argparse
import shutil

DATASET_DIR = "dataset"
OG_PATH = "dataset/tutorial"
SUBSAMPLE = 2


image_dir = os.path.join(OG_PATH, 'image')
depth_dir = os.path.join(OG_PATH, 'depth')
subsample_dir = os.path.join(DATASET_DIR, "sub_sample_{}".format(SUBSAMPLE))
new_image_dir = os.path.join(subsample_dir, 'image')
new_depth_dir = os.path.join(subsample_dir, 'depth')

images = sorted(os.listdir(image_dir))
depths = sorted(os.listdir(depth_dir))

os.makedirs(new_image_dir, exist_ok=True)
os.makedirs(new_depth_dir, exist_ok=True)


for i, image in enumerate(images):
    if i % SUBSAMPLE == 0:
        src = os.path.join(image_dir, image)
        dst = os.path.join(new_image_dir, image)
        shutil.copyfile(src, dst)


for i, image in enumerate(depths):
    if i % SUBSAMPLE == 0:
        src = os.path.join(depth_dir, image)
        dst = os.path.join(new_depth_dir, image)
        shutil.copyfile(src, dst)

