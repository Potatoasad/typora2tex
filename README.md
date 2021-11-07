# typora2tex
Quick terminal application that takes my typora notes and converts them into tex. 
The idea is something like this:

You should be able to convert it to a tex file (with the same name)
```bash
typora2tex mymarkdown.md
```

You should be able to give your own preamble if needed
```bash
typora2tex mymarkdown.md --preamble=mypreamble.tex
```

You should be able to give your own preamble if needed
```bash
typora2tex mymarkdown.md --preamble="some default known preamble"
```

### Features
I'll focus on a limited set of features important to me. It should be able to change:
- `#` to the appropriate `\section{header}`
- bullet points to `\begin{itemize} ... \end{itemize}`
- numbered points to `\begin{enumerate} ... \end{enumerate}`
- dragged and dropped figures into `\includegraphics{..../..}`
