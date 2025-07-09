# How to deploy it?

cd ReachbotPredictor
conda env create -f environment.yml

then, kindly build mmcv on souce code.

git clone https://github.com/open-mmlab/mmcv.git
cd mmcv
pip install -r requirements/optional.txt
pip install -e . -v
python ./dev_scripts/check_installation.py # validate the installation

then, kindly validate the installation by: 
cd mmsegementation
python tools/train_repeat.py --num_repeat 2 --config paper_configs/vit/vessels/dice.py -- --amp 2>&1 | tee log.txt # see if it works

This is how to deploy it on your GCP compute in the fastest way. Kindly leavea message if you meet any difficulty.:) The End.

