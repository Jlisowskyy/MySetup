PATH="${PATH}:${HOME}/.local/bin"

# Possible alternative to less
#export PAGER="most -s" 

#------------------------------------
# Stolen from net - man colors

# Get color support for 'less'
export LESS="--RAW-CONTROL-CHARS"

# Use colors for less, man, etc.
[[ -f ~/.LESS_TERMCAP ]] && . ~/.LESS_TERMCAP
#------------------------------------
# found on arch wiki - syntax colors

export LESSOPEN="| /usr/bin/source-highlight-esc.sh %s"
export LESS="${LESS} -R "

#------------------------------------
