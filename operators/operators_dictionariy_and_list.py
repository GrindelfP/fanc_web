from operators.operators_class import addition, subtraction, multiplication, division, exponentiation, modulus, \
    radical_of_i_index, factorial, logarithm_based_on_i, ln, lg

operators_dictionary = {
    addition.symbol: addition,
    subtraction.symbol: subtraction,
    multiplication.symbol: multiplication,
    division.symbol: division,
    exponentiation.symbol: exponentiation,
    modulus.symbol: modulus,
    radical_of_i_index.symbol: radical_of_i_index,
    factorial.symbol: factorial,
    logarithm_based_on_i.symbol: logarithm_based_on_i,
    ln.symbol: ln,
    lg.symbol: lg
}


operators_symbol_list = [
    addition.symbol,
    subtraction.symbol,
    multiplication.symbol,
    division.symbol,
    exponentiation.symbol,
    modulus.symbol,
    radical_of_i_index.symbol,
    factorial.symbol,
    logarithm_based_on_i.symbol,
    ln.symbol,
    lg.symbol
]
