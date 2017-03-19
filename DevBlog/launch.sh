#!/bin/sh

pushd $(pwd)

cd ..

cd Blog

BlogPath=$(pwd)

popd

docker run -v "$BlogPath:/srv/jekyll" -p 4000:4000 lukegriffith/blog_dev
