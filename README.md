[![image](https://img.shields.io/badge/license-%20AGPL--v3.0-blue.svg)](LICENSE)

# TMS location

Code to visualize and locate points for trans-cranial magnetic stimulation
(TMS).


## Requirements

- You need mesh data generated by https://github.com/bast/MRI-extract-surfaces.
- You need an installation of [Apptainer](https://apptainer.org/) (e.g. following
  the [quick
  installation](https://apptainer.org/docs/user/latest/quick_start.html#quick-installation)).
  Alternatively, [SingularityCE](https://sylabs.io/singularity/) should also
  work.


## How to use it

First download the container image (ending with *.sif) from here:
https://github.com/bast/tms-location/releases

Make the image executable and then point the container image to the directory
where you have the mesh data:
```bash
$ ./tms-location.sif /path/to/ernie_data
```

Then open the browser at the URL shown in the terminal (typically <http://127.0.0.1:8050>).


## The code uses the [potpourri3d library](https://github.com/nmwsharp/potpourri3d) to compute geodesic paths

- https://github.com/nmwsharp/potpourri3d
- https://nmwsharp.com/research/flip-geodesics/

If you use this code, please cite their paper:
```bibtex
@article{sharp2020flipout,
  author = {Sharp, Nicholas and Crane, Keenan},
  title = {You Can Find Geodesic Paths in Triangle Meshes by Just Flipping Edges},
  journal = {ACM Trans. Graph.},
  volume = {39},
  number = {6},
  year = {2020},
  publisher = {ACM},
  address = {New York, NY, USA},
}
```


## Other resources

- https://kathleenhupfeld.com/mni-template-coordinate-systems/
- https://clinicalresearcher.org/F3/calculate.php
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2882797/


## About the container image

To build the image, I have used [this wonderful
guide](https://github.com/singularityhub/singularity-deploy) as starting point
and inspiration.

I find it important that everybody can verify how the container image was
built. And you can! You can inspect the definition file and all scripts which
are all part of this repository.
