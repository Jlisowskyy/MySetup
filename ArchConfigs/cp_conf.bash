#!/bin/bash

if [[ $1 == "-h" ]] || [[ $1 == "--help" ]] ||[[ -z $1 ]]; then
    echo "Expected usage:"
    echo "          cp_conf.bash [ output_dir_name ]"
    echo "Copies desired files to ${PWD}/output_dir_name/*"
    echo "And makes backup to folder ${PWD}/.bckp/output_dir_name/*"
else
    FILE_LIST=`./${1}_list`
    DEST_DIR="${PWD}/${1}"
    BACKUP_DIR="${PWD}/.bckp"

    mkdir $DEST_DIR 2>/dev/null
    pacman -Q > "${DEST_DIR}/package_list"

    rm -Rf ${BACKUP_DIR} 2>/dev/null
    cp -R ${DEST_DIR} ${BACKUP_DIR} 2>/dev/null

    cp -R ${FILE_LIST} ${DEST_DIR}
fi
