find . | grep yaml | xargs cat | awk '{print $2}' | sort | uniq | wc -l

find . | grep yaml | xargs cat | awk '{print $2}' | sort | uniq >.a
cat redis.cmds | awk '{print $1":"}' | grep -v -E '^$|//' | sort | uniq >.b

comm -13 .a .b

rm -f .a .b
