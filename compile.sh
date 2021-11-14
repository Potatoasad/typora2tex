#!/bin/bash

mkdir ../typora2tex-compiled
zip -r ../typora2tex-compiled/typora2tex.zip *
cd ../typora2tex-compiled

echo '#!/usr/bin/env python' | cat - typora2tex.zip > typora2tex
rm ./typora2tex.zip
chmod +x typora2tex
