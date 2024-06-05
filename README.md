[![image](https://img.shields.io/badge/license-%20AGPL--v3.0-blue.svg)](LICENSE)

# TMS location

Code to visualize and locate points for transcranial magnetic stimulation
(TMS).

Uses data generated by https://github.com/bast/MRI-extract-surfaces.


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


## Resources

- https://kathleenhupfeld.com/mni-template-coordinate-systems/
- https://clinicalresearcher.org/F3/calculate.php
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2882797/
