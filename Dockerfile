FROM mambaorg/micromamba:0.25.1
COPY --chown=$MAMBA_USER:$MAMBA_USER wasm-env.yaml  /tmp/wasm-env.yaml
COPY --chown=$MAMBA_USER:$MAMBA_USER build-env.yaml /tmp/build-env.yaml
RUN micromamba install -n base \
        --yes --file  /tmp/build-env.yaml \
    && \
    micromamba create \
        --platform=emscripten-32 \
        --yes --file  /tmp/wasm-env.yaml  \
        -c https://repo.mamba.pm/emscripten-forge \
        -c https://repo.mamba.pm/conda-forge \
    && \
    micromamba clean --all --yes  

ARG ENV_NAME=base
ARG MAMBA_DOCKERFILE_ACTIVATE=1

COPY extra_config.yaml .
RUN curl https://raw.githubusercontent.com/emscripten-forge/recipes/main/empack_config.yaml --output empack_config.yaml
RUN cat empack_config.yaml
RUN empack pack env \
    --env-prefix $MAMBA_ROOT_PREFIX/envs/pyjs-wasm-env \
    --outname sample_webpack_example \
    --config empack_config.yaml \
    --config extra_config.yaml  \
    --outdir output \
    --export-name globalThis.pyjs \
    --split

RUN mkdir wasm

