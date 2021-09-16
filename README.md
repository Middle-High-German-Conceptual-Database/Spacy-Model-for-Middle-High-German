# GMH-Tagger for Spacy v3

This tagger model for [spacy v3](https://spacy.io/) is based on data of the [Reference corpus of Middle High German Version 1.0](https://www.linguistics.rub.de/rem/). The needed data in cora xml format can be downloaded from [Laudatio](https://www.laudatio-repository.org/browse/corpus/xCS3CnMB7CArCQ9C3LRB/corpora). Pos tags are based on  [HITS (HISTORICAL TAGSET)](https://www.linguistics.ruhr-uni-bochum.de/comphist/resources/hits/index.html).

## Reference corpus of Middle High German

> Wich-Reif, Claudia.´Reference Corpus of Middle High German (1050–1350) (1.0)´ Rheinische Friedrich-Wilhelms-Universität Bonn, Ruhr-Universität Bochum, 2016. Homepage: <https://www.linguistics.rub.de/rem/index.html>. DOI: <https://doi.org/10.34644/laudatio-dev-xCS3CnMB7CArCQ9C3LRB>

## Model usage

The model is provided in *models/model-best*. A usage example is provided in *modelTest.py*.

* setup virtual python3 enviroment and load requirements
* execute script

```console
(venv)$ python modelTest.py
```

---

## Training statistics

```console
ℹ Pipeline: ['tok2vec', 'tagger']
ℹ Initial learn rate: 0.001
E    #       LOSS TOK2VEC  LOSS TAGGER  TAG_ACC  SCORE 
---  ------  ------------  -----------  -------  ------
  0       0          0.00        65.10    14.87    0.15
  0     200        262.83     10621.43    75.84    0.76
  0     400        530.47      7645.48    82.05    0.82
  0     600        712.44      7978.32    85.30    0.85
  0     800        902.26      8498.41    86.32    0.86
  0    1000       1102.51      9474.23    87.41    0.87
  0    1200       1362.57     10814.16    88.30    0.88
  0    1400       1688.07     12756.19    89.11    0.89
  0    1600       2089.57     14811.60    89.95    0.90
  0    1800       2541.39     17153.68    90.41    0.90
  0    2000       3053.57     19759.17    90.77    0.91
  0    2200       3812.58     23610.73    91.29    0.91
  0    2400       4496.85     26479.80    91.67    0.92
  0    2600       4655.26     26294.00    91.85    0.92
  0    2800       4702.10     25661.97    92.08    0.92
  0    3000       4718.87     24966.15    92.29    0.92
  1    3200       4806.15     24569.51    92.35    0.92
  1    3400       4717.55     22731.52    92.55    0.93
  1    3600       4857.03     22482.97    92.65    0.93
  1    3800       5015.36     22440.42    92.80    0.93
  1    4000       5016.72     22034.78    92.80    0.93
  1    4200       5113.89     22057.36    92.92    0.93
  1    4400       5104.36     21763.53    92.98    0.93
  1    4600       5163.33     21509.02    93.10    0.93
  1    4800       5292.48     21661.49    93.17    0.93
  2    5000       5233.37     20952.29    93.14    0.93  
  2    5200       5219.53     19612.54    93.22    0.93
  2    5400       5404.91     19654.91    93.15    0.93
  2    5600       5419.01     19369.70    93.33    0.93
  2    5800       5675.79     19880.49    93.38    0.93
  2    6000       5825.59     20196.77    93.37    0.93
  2    6200       5705.57     19554.28    93.45    0.93
  2    6400       5969.08     20093.95    93.49    0.93
  2    6600       5941.85     19875.87    93.54    0.94
  3    6800       5799.12     19066.11    93.59    0.94
  3    7000       5823.24     18071.56    93.50    0.94
  3    7200       6197.17     18905.18    93.56    0.94
  3    7400       6002.32     18068.97    93.63    0.94
  3    7600       6191.74     18360.41    93.63    0.94
  3    7800       6191.64     18110.58    93.70    0.94
  3    8000       6344.78     18168.08    93.68    0.94
  3    8200       6512.15     18454.55    93.75    0.94
  3    8400       6596.44     18575.79    93.76    0.94
  4    8600       6241.27     17284.66    93.72    0.94
  4    8800       6489.69     16945.88    93.78    0.94
  4    9000       6546.82     16934.75    93.80    0.94
  4    9200       6793.86     17272.44    93.83    0.94
  4    9400       6912.54     17419.32    93.82    0.94
  4    9600       7027.06     17553.34    93.86    0.94
  4    9800       7205.23     17735.52    93.88    0.94
  4   10000       7212.00     17620.83    93.83    0.94
  4   10200       7279.06     17754.80    93.83    0.94
  5   10400       6829.92     16338.48    93.88    0.94
  5   10600       7039.58     16068.71    93.89    0.94
  5   10800       7212.91     16200.82    93.89    0.94
  5   11000       7416.97     16387.91    93.95    0.94
  5   11200       7644.46     16842.92    93.98    0.94
  5   11400       7531.70     16514.61    93.97    0.94
  5   11600       7880.57     17285.24    93.94    0.94
  5   11800       7822.56     17015.28    93.99    0.94
  5   12000       7927.11     17079.88    94.06    0.94
  6   12200       7467.90     15694.47    93.99    0.94
  6   12400       7559.72     15169.55    94.04    0.94
  6   12600       7767.79     15344.22    94.02    0.94
  6   12800       8220.52     16248.93    94.01    0.94
  6   13000       8398.07     16340.65    94.09    0.94
  6   13200       8343.02     16164.52    94.08    0.94
  6   13400       8351.15     16151.07    94.05    0.94
  6   13600       8588.68     16580.61    94.11    0.94
  6   13800       8343.99     16150.88    94.11    0.94
  7   14000       7837.48     14640.21    94.10    0.94
  7   14200       8304.96     14972.37    94.10    0.94
  7   14400       8577.43     15343.77    94.14    0.94
  7   14600       8621.37     15280.43    94.13    0.94
  7   14800       8666.39     15233.18    94.15    0.94
  7   15000       8860.83     15676.02    94.13    0.94
  7   15200       9103.35     15889.79    94.18    0.94
  7   15400       9093.77     15763.97    94.24    0.94
  8   15600       9134.42     15768.34    94.21    0.94
  8   15800       8577.19     14333.81    94.20    0.94
  8   16000       8956.50     14652.68    94.18    0.94
  8   16200       9209.77     14892.38    94.17    0.94
  8   16400       9324.56     14937.85    94.17    0.94
  8   16600       9529.17     15222.72    94.20    0.94
  8   16800       9439.55     15022.82    94.21    0.94
  8   17000       9650.75     15229.33    94.23    0.94
```

---

## Training instructions

Only follow these steps, if you want to train the pos tagger. Otherwise use the provided model data. [See documentation for more](https://spacy.io/usage/training).

### Preparation

* Download REM Corpus in Cora Format and add to */data/REM*
* setup virtual python3 enviroment and load requirements
* Convert to spacy format using Python script *cora2spacy.py*

```console
(venv)$ python cora2spacy.py
```

* Build config from *base_config.cfg*

```console
(venv)$ python -m spacy init fill-config base_config.cfg config.cfg
```

### Training

Start training with

```console
(venv)$ python -m spacy train config.cfg --output ./models --paths.train ./corpus/train.spacy --paths.dev ./corpus/dev.spacy
```
