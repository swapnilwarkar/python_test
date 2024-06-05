https://pylint.readthedocs.io/en/stable/

sudo apt install pylint
pylint --generate-rcfile > ${HOME}/.pylintrc
sudo cp .pylintrc /mnt/c/swap_wsl/swapnil_repo/python_test/2_projects/my_python_template/

How to run the .pylint analysis: 
1. pylint my_python_template

We can do the analysis for single file as well: 
1. pylint my_python_template/main.py
2. pylint my_python_template/data.py

