#!/bin/sh
echo $1

pushd $(pwd)

cd ..

cd Blog

BlogPath=$(pwd)

popd

docker run -v "$BlogPath:/srv/jekyll" -p 4000:4000 $1 
