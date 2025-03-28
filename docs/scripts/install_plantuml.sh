#!/bin/bash
###########################
# Install a newer version of plantuml than the default readthedocs
# version. That older version was raising exceptions that did not
# exist on my local plantuml.
#
#
# Script from user Hudson on stack overflow
# https://stackoverflow.com/questions/77869766/how-do-i-specify-the-plantuml-version-with-readthedocs
###########################

# Stop and exit on error
set -euox pipefail

# Check for required tools
java -version
dot -V

# This folder is on PATH and does not require sudo
# Download latest plantuml.jar from github
curl -o ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml.jar -L https://github.com/plantuml/plantuml/releases/download/v1.2024.3/plantuml-1.2024.3.jar
# Create an executable script for plantuml
printf '#!/bin/bash\nexec java -Djava.awt.headless=true -jar ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml.jar "$@"' > ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml
chmod +x ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml

# Check plantuml version
plantuml -version