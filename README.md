# Improved-GWCNN

[![](https://img.shields.io/badge/python-2.7-brightgreen)](https://www.python.org/download/releases/2.7/) [![](https://img.shields.io/badge/python-3.7-green)](https://www.python.org/downloads/release/python-370/) [![](https://img.shields.io/badge/pytorch-1.5.1-blue)](https://pytorch.org/) [![](https://img.shields.io/badge/arxiv-2011.04418-red)](https://arxiv.org/abs/2011.04418) 

This reposity contains all the codes to reproduce the results for our paper:  [Improved deep learning techniques in gravitational-wave data analysis](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.024040) by H Xia et al. (2020) [[arxiv:2011.04418](https://arxiv.org/abs/2011.04418)].

## Dataset Generation

Our codes to generate gravitational-wave data are based on the open source tool [ggwd](https://github.com/timothygebhard/ggwd) for paper [*Convolutional neural networks: a magic bullet for gravitational-wave detection?*](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.100.063015) [[arXiv:1904.08693](https://arxiv.org/abs/1904.08693)]. For details of using this tool, please check `README.md` in `./ggwd`.

## Requirements

Environment needed to run our model including:

- PyTorch == 1.5.1
- numpy == 1.19.1
- scikit-learn == 0.23.2
- torchsummary == 1.5.1
- matplotlib == 3.3.1
- pandas == 1.1.3
- tqdm == 4.49.0

To settle the environment quickly, run:

```
pip install -r requirements.txt
```

## Usage

Models that are used in our paper can be found in `./model`. After generating your own datasets and preprocessing the data in `./ggwd`, you can run `run.ipynb` to see the results of your own.

