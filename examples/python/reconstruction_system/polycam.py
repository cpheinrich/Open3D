import json
import os
import open3d as o3d
import numpy as np


def get_camera_file_lists(path_dataset):
    file_list = []
    cam_dir = os.path.join(path_dataset, "cameras")
    if os.path.isdir(cam_dir):
        for f in os.listdir(cam_dir):
            if ".json" in f:
                file_list.append(os.path.join(cam_dir, f))
    return sorted(file_list)


""" Reads the arkit camera json file and returns a 4x4 world -> cam transformation matrix """


def extract_transform(cam_path):
    j = {}
    with open(cam_path, "r") as f:
        j = json.load(f)
    transform = np.zeros((4, 4))
    R = np.zeros((3, 3))

    R[0, 0] = j["t_00"]
    R[0, 1] = j["t_01"]
    R[0, 2] = j["t_02"]
    R[1, 0] = j["t_10"]
    R[1, 1] = j["t_11"]
    R[1, 2] = j["t_12"]
    R[2, 0] = j["t_20"]
    R[2, 1] = j["t_21"]
    R[2, 2] = j["t_22"]
    transform[0, 3] = j["t_03"]
    transform[1, 3] = j["t_13"]
    transform[2, 3] = j["t_23"]
    transform[3, 3] = 1
    transform[0:3, 0:3] = R

    # take inverse to get world to cam
    transform = np.linalg.inv(transform)

    # A rotation by 180 degrees around x axis is necessary
    # to remove an unorthodox convention used by ARKit
    Rx = np.zeros((4, 4))
    Rx[0, 0] = 1.0
    Rx[1, 1] = -1.0
    Rx[2, 2] = -1.0
    Rx[3, 3] = 1.0

    transform = np.matmul(Rx, transform)

    # transform = np.linalg.inv(transform)

    return transform
