from interpreter import draw
from chessPictures import *

fila1 = square.join(square.negative()).horizontalRepeat(4)
fila2 = fila1.negative()

fila_piezas_negras = rock.join(knight)
fila_piezas_negras = fila_piezas_negras.join(bishop)
fila_piezas_negras = fila_piezas_negras.join(queen)
fila_piezas_negras = fila_piezas_negras.join(king)
fila_piezas_negras = fila_piezas_negras.join(bishop)
fila_piezas_negras = fila_piezas_negras.join(knight)
fila_piezas_negras = fila_piezas_negras.join(rock)

fila_piezas_negras = fila_piezas_negras.up(fila1)

fila_peones_negros = pawn.horizontalRepeat(8).up(fila2)

fila_peones_blancos = fila_peones_negros.negative()

fila_piezas_blancas = fila_piezas_negras.negative().up(fila2)

centro = fila1.under(fila2)
centro = centro.verticalRepeat(2)

resultado_g = fila_piezas_negras
resultado_g = resultado_g.under(fila_peones_negros)
resultado_g = resultado_g.under(centro)
resultado_g = resultado_g.under(fila_peones_blancos)
resultado_g = resultado_g.under(fila_piezas_blancas)
draw(resultado_g)