let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/repos/endeavour/web-design
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 ~/repos/endeavour/web-design/testing.html
badd +14 ~/repos/endeavour/web-design/testing.css
badd +2 ~/repos/endeavour/web-design/navbar.css
badd +1 ~/repos/endeavour/web-design/navabr.html
badd +1 ~/repos/endeavour/web-design/testing.js
argglobal
%argdel
$argadd testing.html
$argadd testing.css
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit ~/repos/endeavour/web-design/testing.html
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 113 + 84) / 168)
exe 'vert 2resize ' . ((&columns * 54 + 84) / 168)
argglobal
balt ~/repos/endeavour/web-design/testing.js
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 18) / 37)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
lcd ~/repos/endeavour
wincmd w
argglobal
if bufexists(fnamemodify("~/repos/endeavour/web-design/testing.css", ":p")) | buffer ~/repos/endeavour/web-design/testing.css | else | edit ~/repos/endeavour/web-design/testing.css | endif
if &buftype ==# 'terminal'
  silent file ~/repos/endeavour/web-design/testing.css
endif
balt ~/repos/endeavour/web-design/testing.html
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 15 - ((5 * winheight(0) + 18) / 37)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 15
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 113 + 84) / 168)
exe 'vert 2resize ' . ((&columns * 54 + 84) / 168)
tabnext
edit ~/repos/endeavour/web-design/navbar.css
argglobal
if bufexists(fnamemodify("~/repos/endeavour/web-design/navbar.css", ":p")) | buffer ~/repos/endeavour/web-design/navbar.css | else | edit ~/repos/endeavour/web-design/navbar.css | endif
if &buftype ==# 'terminal'
  silent file ~/repos/endeavour/web-design/navbar.css
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 18 - ((10 * winheight(0) + 18) / 37)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 18
normal! 0
lcd ~/repos/endeavour
tabnext 1
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
