"personal vim 
"last updated:
"*3-17-2014
"
"
set ic
set nu
set ts=3
set ai                     " enable auto-indent
set ignorecase             " ignore case 
set shiftwidth=3
set expandtab              " expantab for vim
set term=builtin_ansi      " required to get color on osx, prior to syntax on
filetype plugin on         " use the file type plugin
map \p i(<Esc>ea)<Esc>     " map parentheses
map \c i{<Esc>ea}<Esc>     " map curly braces
syntax on                  " enable syntax highlight
colorscheme desert
