#!/bin/sh
rsync -av --exclude .git --exclude env --exclude .env --exclude .vscode ./ rogerbage@rogerbage.vps-kinghost.net:/home/rogerbage/metaLeg
