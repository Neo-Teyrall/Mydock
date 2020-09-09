# export l'environnement dans un ficheir yaml pour qu'il puisse etre recontruit.
conda env export -n <env_name> --no-builds | grep -v "^prefix:"  > <name>.yml

