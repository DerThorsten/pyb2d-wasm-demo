#!/bin/bash
set -e



micromamba create \
    --platform=emscripten-32 \
    --yes --file  wasm-env.yaml  \
    -c https://repo.mamba.pm/emscripten-forge \
    -c https://repo.mamba.pm/conda-forge 


curl https://raw.githubusercontent.com/emscripten-forge/recipes/main/empack_config.yaml --output empack_config.yaml
empack pack env \
    --env-prefix $MAMBA_ROOT_PREFIX/envs/pyjs-wasm-env \
    --outname sample_webpack_example \
    --config empack_config.yaml \
    --config extra_config.yaml  \
    --outdir src \
    --export-name globalThis.pyjs \
    --split

cp -a $MAMBA_ROOT_PREFIX/envs/pyjs-wasm-env/lib_js/pyjs/. src

node add_export_to_js.js