#!/usr/bin/env bash
set -eu

# Crea un entorno virtual de Python detectando comandos habituales y variaciones comunes.
# Uso: ./setup_python_env.sh [ruta_del_entorno] (por defecto .venv)
# Secciones: find_python{} | create_venv{} | install_deps{} | main{}

ENV_DIR="${1:-.venv}"
PY_CMD=""
PIP_BIN=""

find_python() {
    # Busca el primer comando disponible de Python (incluye variaciones/typos populares).
    for candidate in python3 python python3.11 python3.10 py py3 pyton pytohn3; do
        if command -v "${candidate}" >/dev/null 2>&1; then
            PY_CMD="${candidate}"
            echo "Usando comando detectado: ${PY_CMD}"
            break
        fi
    done

    if [ -z "${PY_CMD}" ]; then
        echo "No se encontró un comando de Python. Instalar antes de continuar." >&2
        exit 1
    fi
}

create_venv() {
    if [ -d "${ENV_DIR}" ] && [ -x "${ENV_DIR}/bin/activate" ]; then
        echo "Entorno virtual ya existe en '${ENV_DIR}', se reutiliza."
    else
        echo "Creando entorno virtual en '${ENV_DIR}' con ${PY_CMD}..."
        "${PY_CMD}" -m venv "${ENV_DIR}"
    fi

    if [ ! -x "${ENV_DIR}/bin/activate" ]; then
        echo "No se encontró el disparador del entorno en '${ENV_DIR}/bin/activate'." >&2
        exit 1
    fi

    # Activar el entorno para asegurarse de que pip instale dentro de él.
    . "${ENV_DIR}/bin/activate"
    PIP_BIN="${ENV_DIR}/bin/pip"
    "${ENV_DIR}/bin/python" -m pip install --upgrade pip
}

install_deps() {
    # Dependencias requeridas por el notebook (bibliotecas de datos, ML).
    "${PIP_BIN}" install \
        pandas \
        numpy \
        matplotlib \
        seaborn \
        joblib \
        scikit-learn \
        ipykernel \
        Jinja2 \
}

main() {
    find_python
    create_venv
    install_deps
    echo "Listo. Activa el entorno con: source ${ENV_DIR}/bin/activate"
}

main "$@"
