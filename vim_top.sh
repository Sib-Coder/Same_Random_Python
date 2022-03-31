sudo apt update
sudo apt install vim -y
sudo apt install xclip maim
command -v vim || sudo yum install -y vim || sudo apt install -y vim
command -v xsel || sudo yum install -y xsel || sudo apt install -y xsel
command -v flake8 || sudo yum install -y flake8 || sudo apt install -y flake8

echo "set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin() 
Plugin 'VundleVim/Vundle.vim'
Plugin 'https://github.com/ervandew/supertab'
Plugin 'https://github.com/ConradIrwin/vim-bracketed-paste'
Plugin 'flazz/vim-colorschemes'
Plugin 'scrooloose/nerdtree'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'nvie/vim-flake8'
\" All of your Plugins must be added before the following line
call vundle#end()            \" required
if \$COLORTERM == 'gnome-terminal'
          set t_Co=256
  endif
filetype plugin indent on
syntax on
colorscheme badwolf
set tabstop=4
set number
set autoindent
set shiftwidth=4
set textwidth=99
set expandtab
set smartindent
set encoding=utf-8
set mouse=a
set cursorline
vnoremap <silent> <C-C> \"+y
nnoremap <silent> <c-v> \"+p
inoremap <silent> <C-V> <C-R><C-P>+
set fileencodings=utf-8,cp1251,cp866,koi8-r
inoremap <silent> <C-j> <C-O>dd<Down><C-R><C-P>\"<Up>
\" inoremap <silent> <C-k> <C-O>dd<Up><C-R><C-P>\"<Up>
\" nnoremap <silent> <C-k> dd<Up>i<C-R><C-P>\"<Up><Esc>
nnoremap <silent> <C-j> dd<Down>i<C-R><C-P>\"<Esc><Up>
nnoremap <F3> :set hlsearch!<CR>
map <C-n> :NERDTreeToggle<CR>
nnoremap <C-H> :Hexmode<CR>
inoremap <C-H> <Esc>:Hexmode<CR>
vnoremap <C-H> :<C-U>Hexmode<CR>
command -bar Hexmode call ToggleHex()
function ToggleHex()
  let l:modified=&mod
  let l:oldreadonly=&readonly
  let &readonly=0
  let l:oldmodifiable=&modifiable
  let &modifiable=1
  if !exists(\"b:editHex\") || !b:editHex
    \" save old options
    let b:oldft=&ft
    let b:oldbin=&bin
    \" set new options
    setlocal binary \" make sure it overrides any textwidth, etc.
    silent :e \" this will reload the file without trickeries 
              \"(DOS line endings will be shown entirely )
    let &ft=\"xxd\"
    \" set status
    let b:editHex=1
    \" switch to hex editor
    %!xxd
  else
    \" restore old options
    let &ft=b:oldft
    if !b:oldbin
      setlocal nobinary
    endif
    \" set status
    let b:editHex=0
    \" return to normal editing
    %!xxd -r
  endif
  \" restore values for modified and read only state
  let &mod=l:modified
  let &readonly=l:oldreadonly
  let &modifiable=l:oldmodifiable
endfunction
augroup Binary
  au!
  au BufReadPre  *.bin let &bin=1
  au BufReadPost *.bin if &bin | %!xxd
  au BufReadPost *.bin set ft=xxd | endif
  au BufWritePre *.bin if &bin | %!xxd -r
  au BufWritePre *.bin endif
  au BufWritePost *.bin if &bin | %!xxd
  au BufWritePost *.bin set nomod | endif
augroup END" > ~/.vimrc
command -v git || sudo yum install -y git || sudo apt install -y git
command -v curl || sudo yum install -y curl || sudo apt install -y curl
mkdir -p ~/.vim/bundle/
git clone https://github.com/VundleVim/Vundle.vim ~/.vim/bundle/Vundle.vim
vim +PluginInstall +qall

echo "
transfer() {
    if [ \$# -eq 0 ]; then
        echo -e \"No arguments specified. Usage:\necho transfer /tmp/test.md\ncat /tmp/test.md | transfer test.md\";
        return 1;
    fi 
    tmpfile=\$( mktemp -t transferXXX );
    if tty -s; then
        basefile=\$(basename \"\$1\" | sed -e 's/[^a-zA-Z0-9._-]/-/g');
        curl --progress-bar --upload-file \"\$1\" \"http://data.tsu.ru:8090/\$basefile\" >> \$tmpfile;
    else 
        curl --progress-bar --upload-file \"-\" \"http://data.tsu.ru:8090/\$1\" >> \$tmpfile ;
    fi;
    cat \$tmpfile; command -v xsel && cat \$tmpfile | xsel -b;
    rm -f \$tmpfile;
}
" >> ~/.bashrc

echo "
takescreen() {
    maim -s | xclip -selection clipboard -t image/png && notify-send -t 300 "Screenshot copied to clipboard"
}
" >> ~/.bashrc

