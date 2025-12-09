#!/usr/bin/env bash
set -eu

# Renombra archivos de una carpeta agregando _<palabra> antes de la extensión.
# Uso: ./rename_with_suffix.sh [carpeta] [palabra]
# Valores por defecto: carpeta=pred, palabra=JA_ASUS_PY_3.12
# Secciones: validate_inputs{} | rename_files{} | main{}

DIR="${1:-pred}"
SUFFIX="${2:-JA_ASUS_PY_3.12}"

validate_inputs() {
    if [ ! -d "${DIR}" ]; then
        echo "La carpeta '${DIR}' no existe" >&2
        exit 1
    fi
}

rename_files() {
    for path in "${DIR}"/*; do
        [ -e "${path}" ] && [ -f "${path}" ] || continue

        filename="$(basename "${path}")"
        base="${filename%.*}"
        ext="${filename##*.}"
        # Si no hay extensión, dejamos ext vacío
        [ "${base}" = "${filename}" ] && ext="" || ext=".${ext}"

        new_path="$(dirname "${path}")/${base}_${SUFFIX}${ext}"
        if [ -e "${new_path}" ]; then
            echo "Omitiendo '${path}': ya existe '${new_path}'" >&2
            continue
        fi

        mv -- "${path}" "${new_path}"
    done
}

main() {
    validate_inputs
    rename_files
    echo "Renombrado completado en '${DIR}' usando sufijo '${SUFFIX}'."
}

main "$@"
