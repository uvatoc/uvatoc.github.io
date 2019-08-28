\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{uvatoc}[cs3102 LaTeX class]

\newcommand{\headlinecolor}{\normalcolor}
\LoadClass[11pt,fullpage]{article} % []{article}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\DeclareOption{submission}{\renewcommand{\headlinecolor}{\color{green}}}
\DeclareOption{assignment}{\renewcommand{\headlinecolor}{\color{slcolor}}}
\ProcessOptions\relax
