find . | grep yaml | xargs cat | awk '{print $2}' |sort| uniq |wc
