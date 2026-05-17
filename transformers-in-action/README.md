# Reading the book

First chapter is just a presentation of the state of art, and why encoder-decoder architecture is the base of the transformers too.

The second chapter goes into mathematical details about the article "Attention is all you need" (definitely is something I really need!).

Anyway, I stopped at definition of position encoding, and start asking support to some chatbot around, I mean google Gemini, I got some insight.

The two functions are used alternatively for the x and x+1 dimension, where x is divisible by 2 (but x+1 is not divisible by 2!). Ok, that was what look strange to me as definition, why that 2*i and 2*i + 1? It was just it.

Considering that each word has a position and is represented as a vector, the vector being of dimension `dim`, but let's say 512, each word position is encoded a vector of 256 values, and I could arrange those as column vector.

Then each vector could be placed one near the very previous, so defining a matrix of Dim X LoT, where LoT is Lenght of Text, and Dim is the dimension of the representation of a word.

Since Dim is the number of rows, each row is always the result of a single trigonometric function: the even are all

> sin( c / (10000 ^ ( (r/512) ) ) )

Where c is the column, r is the row index, and the other formula for odd rows:

> cos ( c / (10000 ^ ( (r-1) / 512) ) )

One may ask why am I doing this confusion here? That's simple: to solve my own confusion.

I just changed it so it is clear that the row number r is not multiplied by 2, it is taken the neareast even index before it.

It also give an interpretation more clear: the odd dimension follow a cyclic function that is 90 degree phase far. For example, the argument for 1st and 2nd rows are the same, but the function applied is sin() for the 1st, and cos() for the 2nd. This is for 3rd related to 4th, and so on. (I mean 1st = 0-index, 2nd = 1-index, ...)

What I asked is to visualize this geometrically, because I am really interested about that.

Something interactive, use:

https://html-preview.github.io/?url=https://github.com/danielecr/transformer-thought/blob/main/transformers-in-action/plot-dynamics-canva.html

Other code here:
* plot-the-pos.py
* plot-as-canvas.html
* plot-dynamics-canva.html

The geometrical interpretation is a kind of noise to be added to the dimension, and this noise spawn over each dimension is different ways and frequencies.

Based on the noise, the models "know" where the word is located in the text.

Disclaimer: ask the author, this is just my interpretation.

