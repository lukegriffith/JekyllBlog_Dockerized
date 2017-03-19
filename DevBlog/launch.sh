#!/bin/sh
echo $1


BlogPath="/Users/luke/GitHub/JekyllBlog_Dockerized/Blog"

docker run -v "$BlogPath:/var/www" $1 
