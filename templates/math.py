from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import latex2mathml.converter
import random
latex_input = "arctan(x^2-1/2x) + arctan(1/x) = arctan((x^2-1/2x + 1/x)/(1 - x^2/2))"
mathml_output = latex2mathml.converter.convert(latex_input)
