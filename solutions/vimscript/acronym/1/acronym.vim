"
" Convert a phrase into an uppercased acronym formed from
" the initial letter of each word, ignoring leading underscores
"
" Examples:
"
"   :echo Abbreviate('First In, First Out')
"   FIFO
"
"   :echo Abbreviate('The Road _Not_ Taken')
"   TRNT
"
function! Abbreviate(phrase) abort
	let l:result = ''
	let l:phrase = substitute(a:phrase, '_', ' ', 'g')
	for l:section in split(l:phrase, ' ')
		for l:word in split(l:section, '-')
			let l:result .= toupper(l:word[0])
		endfor
	endfor

	return l:result
endfunction 
