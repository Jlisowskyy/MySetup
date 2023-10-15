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

# bash parameter completion for the dotnet CLI

function _dotnet_bash_complete()
{
  local cur="${COMP_WORDS[COMP_CWORD]}" IFS=$'\n' # On Windows you may need to use use IFS=$'\r\n'
  local candidates

  read -d '' -ra candidates < <(dotnet complete --position "${COMP_POINT}" "${COMP_LINE}" 2>/dev/null)

  read -d '' -ra COMPREPLY < <(compgen -W "${candidates[*]:-}" -- "$cur")
}

complete -f -F _dotnet_bash_complete dotnet
