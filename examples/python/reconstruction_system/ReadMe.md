# Running the reconstruction system on Polycam data

- Download one of the datasets from this google drive: https://drive.google.com/drive/folders/1Z-eoOKOB8VMgZIivhAd4v-cTMnxghCWC?usp=sharing, for example `guest-bedroom`, then unzip the folder and copy the folder to ./datasets directory

- `pip3 install open3D numpy`

- `python3 run_system.py ./config/guest-bedroom.json --make --register --refine --integrate`

- This should run the whole reconstruction pipeline end to end, and you can view the output in `./dataset/guest-bedroom/scene/integrated.ply`

NOTE: this runs pretty much the same algorithm that is in the public open3D repo https://github.com/intel-isl/Open3D, where the main difference is that in the `./make_fragments.py` file I read the odometry from ARKit rather than estimating the odometry from scratch. This is (i) much faster and (ii) gives better results. I suspect that we can do better with a bit more work though.
