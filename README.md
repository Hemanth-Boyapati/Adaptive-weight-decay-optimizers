# Adaptive-weight-decay-optimizers

This repository contains optimizer files of applying second order weight decoupling and adaptive weight decay intervals on AdamW, RAdam and AdaBelief optimizers. These optimizers are used for training ViT.
### Use this command for training ViT:
```
python main.py
```
### For training on TinyImagenet dataset first run this script before exectuing the main script:
1. Download the TinyImagenet dataset and extract the files in the downloaded zip file with this code:
```
import urllib.request
import zipfile
import os
url = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"
save_path = "dataset/tiny-imagenet-200.zip"

urllib.request.urlretrieve(url, save_path)
zip_file_path = "dataset/tiny-imagenet-200.zip"
extract_path = "dataset"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
```
2. Next execute these two commands:
```
rm -r dataset/tiny-imagenet-200/test
python3 val_format.py
```
### For using different optimizers for training:
Import the required optimizer from the optimizer folder into the main file and change the lines where optimizer is used and pass the necessary arguments.
#### Import statements:
AdamW with second order decoupling:
```
from optimizers.adamw_second_order_decoupling import AdamW
```
AdamW with adaptive weight decay intervals:
```
from optimizers.adamw_weight_decay_intervals import AdamW
```
RAdam with second order decoupling:
```
from optimizers.radam_second_order_decoupling import RAdam
```
RAdam with adaptive weight decay intervals:
```
from optimizers.radam_weight_decay_intervals import RAdam
```
AdaBelief with second order decoupling:
```
from optimizers.adabelief_second_order_decoupling import AdaBelief
```
AdaBelief with adaptive weight decay intervals:
```
from optimizers.adabelief_weight_decay_intervals import AdaBelief
```

#### Optimizer statements:
Change lines 256 and 258 in main with these respective lines:
1. AdamW
```
optimizer1 = AdamW(parameters1, weight_decay=5e-2)
optimizer2 = AdamW(parameters2, weight_decay=5e-2)
```
2. RAdam
```
optimizer1 = RAdam(parameters1, weight_decay=5e-2,decoupled_weight_decay=True)
optimizer2 = RAdam(parameters2, weight_decay=5e-2,decoupled_weight_decay=True)
```

3. AdaBelief
```
optimizer1 = AdaBelief(parameters1, weight_decay=5e-2,weight_decouple=True)
optimizer2 = AdaBelief(parameters2, weight_decay=5e-2,weight_decouple=True)
```


 


