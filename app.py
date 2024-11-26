import streamlit as st

def gerar_dip(altura_sala, comprimento_sala, diametro_entrada, altura_dip):
    return f"""
# Gerar DIP
#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.13.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Usuario/Desktop/Openfoam')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)
sk = geompy.Sketcher2D()
sk.addPoint(0.0000000, 0.0000000)
sk.addSegmentAbsolute(0.0000000, {altura_sala})
sk.addSegmentAbsolute({comprimento_sala}, {altura_sala})
sk.addSegmentAbsolute({comprimento_sala}, 0.0000000)
sk.close()
Sketch_1 = sk.wire(geomObj_1) 
P1 = geompy.MakeVertex(0, ({altura_sala}/2), 0)
P2 = geompy.MakeVertexWithRef(P1, 0, -5, 0)
P3 = geompy.MakeVertexWithRef(P1, 0, -70, 0)
P4 = geompy.MakeVertexWithRef(P3, {comprimento_sala}, 0, 0)
P5 = geompy.MakeVertexWithRef(P2, {comprimento_sala}, 0, 0)
P6 = geompy.MakeVertexWithRef(P1, {comprimento_sala}, 0, 0)
L1 = geompy.MakeLineTwoPnt(P1, P6)
L2 = geompy.MakeLineTwoPnt(P2, P5)
L3 = geompy.MakeLineTwoPnt(P3, P4)
P7 = geompy.MakeVertex(({comprimento_sala}/2), 0, 0)
P8 = geompy.MakeVertexWithRef(P7, 0, {altura_sala}, 0)
L4 = geompy.MakeLineTwoPnt(P7, P8)
P9 = geompy.MakeVertexOnLinesIntersection(L1, L4)
P10 = geompy.MakeVertexOnLinesIntersection(L2, L4)
P11 = geompy.MakeVertexOnLinesIntersection(L3, L4)
P12 = geompy.MakeVertexWithRef(P11, 0, 35, 0)
E1 = geompy.MakeEllipse(P12, None, 35, 14, L4)
P13 = geompy.MakeVertexWithRef(P9, 33, 0, 0)
P14 = geompy.MakeVertexWithRef(P9, 35, 0, 0)
P15 = geompy.MakeVertexWithRef(P10, 33, 0, 0)
P16 = geompy.MakeVertexWithRef(P10, 35, 0, 0)
P17 = geompy.MakeVertexWithRef(P15, 140, 0, 0)
P18 = geompy.MakeVertexWithRef(P16, 140, 0, 0)
C1 = geompy.MakeCircle(P17, None, 140)
C2 = geompy.MakeCircle(P18, None, 140)
P19 = geompy.MakeVertexOnLinesIntersection(C1, L3)
P20 = geompy.MakeVertexOnLinesIntersection(C2, L3)
P19_vertex_3 = geompy.GetSubShape(P19, [3])
A1 = geompy.MakeArc(P13, P15, P19_vertex_3)
P20_vertex_3 = geompy.GetSubShape(P20, [3])
A2 = geompy.MakeArc(P14, P16, P20_vertex_3)
P21 = geompy.MakeVertexWithRef(P13, ({diametro_entrada} - 33), 0, 0)
P22 = geompy.MakeVertexWithRef(P14, ({diametro_entrada} - 33), 0, 0)
P23 = geompy.MakeVertexWithRef(P21, 150, 0, 0)
P24 = geompy.MakeVertexWithRef(P22, 150, 0, 0)
C3 = geompy.MakeCircle(P23, None, 150)
C4 = geompy.MakeCircle(P24, None, 150)
P25 = geompy.MakeVertexOnLinesIntersection(C3, L3)
P26 = geompy.MakeVertexOnLinesIntersection(C4, L3)
P27 = geompy.MakeVertexWithRef(P15, ({diametro_entrada} - 33), 0, 0)
P28 = geompy.MakeVertexWithRef(P16, ({diametro_entrada} - 33), 0, 0)
P25_vertex_3 = geompy.GetSubShape(P25, [3])
A3 = geompy.MakeArc(P21, P27, P25_vertex_3)
P26_vertex_3 = geompy.GetSubShape(P26, [3])
A4 = geompy.MakeArc(P22, P28, P26_vertex_3)
P29 = geompy.MakeVertexWithRef(P21, 0, {altura_dip}, 0)
P30 = geompy.MakeVertexWithRef(P22, 0, {altura_dip}, 0)
L5 = geompy.MakeLineTwoPnt(P13, P14)
L6 = geompy.MakeLineTwoPnt(P19_vertex_3, P20_vertex_3)
L7 = geompy.MakeLineTwoPnt(P25_vertex_3, P26_vertex_3)
L8 = geompy.MakeLineTwoPnt(P22, P30)
L9 = geompy.MakeLineTwoPnt(P30, P29)
L10 = geompy.MakeLineTwoPnt(P29, P21)
DIVISAO = geompy.MakeFaceWires([E1], 1)
F2 = geompy.MakeFaceWires([A1, A2, L5, L6], 1)
F3 = geompy.MakeFaceWires([A3, A4, L7, L8, L9, L10], 1)
PARTITION1 = geompy.MakePartitionNonSelfIntersectedShape([DIVISAO], [L4], [], [], geompy.ShapeType["FACE"], 0, [], 1, True)
[F1] = geompy.SubShapes(PARTITION1, [8])
REVOLUTION1_1 = geompy.MakeRevolution(F2, L4, 180*math.pi/180.0)
REVOLUTION1_2 = geompy.MakeRevolution(F3, L4, 180*math.pi/180.0)
REVOLUTION1_3 = geompy.MakeRevolution(F1, L4, 180*math.pi/180.0)
FUSE1 = geompy.MakeFuseList([REVOLUTION1_1, REVOLUTION1_2, REVOLUTION1_3], True, True)
geompy.addToStudy( Sketch_1, 'Sketch_1' )
geompy.addToStudy( P1, 'P1' )
geompy.addToStudy( P2, 'P2' )
geompy.addToStudy( P3, 'P3' )
geompy.addToStudy( P4, 'P4' )
geompy.addToStudy( P5, 'P5' )
geompy.addToStudy( P6, 'P6' )
geompy.addToStudy( L1, 'L1' )
geompy.addToStudy( L2, 'L2' )
geompy.addToStudy( L3, 'L3' )
geompy.addToStudy( P7, 'P7' )
geompy.addToStudy( P8, 'P8' )
geompy.addToStudy( L4, 'L4' )
geompy.addToStudy( P9, 'P9' )
geompy.addToStudy( P10, 'P10' )
geompy.addToStudy( P11, 'P11' )
geompy.addToStudy( P12, 'P12' )
geompy.addToStudy( E1, 'E1' )
geompy.addToStudy( P13, 'P13' )
geompy.addToStudy( P14, 'P14' )
geompy.addToStudy( P15, 'P15' )
geompy.addToStudy( P16, 'P16' )
geompy.addToStudy( P17, 'P17' )
geompy.addToStudy( P18, 'P18' )
geompy.addToStudy( C1, 'C1' )
geompy.addToStudy( C2, 'C2' )
geompy.addToStudy( P19, 'P19' )
geompy.addToStudy( P20, 'P20' )
geompy.addToStudyInFather( P19, P19_vertex_3, 'P19:vertex_3' )
geompy.addToStudy( A1, 'A1' )
geompy.addToStudyInFather( P20, P20_vertex_3, 'P20:vertex_3' )
geompy.addToStudy( A2, 'A2' )
geompy.addToStudy( P21, 'P21' )
geompy.addToStudy( P22, 'P22' )
geompy.addToStudy( P23, 'P23' )
geompy.addToStudy( P24, 'P24' )
geompy.addToStudy( C3, 'C3' )
geompy.addToStudy( C4, 'C4' )
geompy.addToStudy( P25, 'P25' )
geompy.addToStudy( P26, 'P26' )
geompy.addToStudy( P27, 'P27' )
geompy.addToStudy( P28, 'P28' )
geompy.addToStudyInFather( P25, P25_vertex_3, 'P25:vertex_3' )
geompy.addToStudy( A3, 'A3' )
geompy.addToStudyInFather( P26, P26_vertex_3, 'P26:vertex_3' )
geompy.addToStudy( A4, 'A4' )
geompy.addToStudy( P29, 'P29' )
geompy.addToStudy( P30, 'P30' )
geompy.addToStudy( L5, 'L5' )
geompy.addToStudy( L6, 'L6' )
geompy.addToStudy( L7, 'L7' )
geompy.addToStudy( L8, 'L8' )
geompy.addToStudy( L9, 'L9' )
geompy.addToStudy( L10, 'L10' )
geompy.addToStudy( DIVISAO, 'DIVISAO' )
geompy.addToStudy( F2, 'F2' )
geompy.addToStudy( F3, 'F3' )
geompy.addToStudy( PARTITION1, 'PARTITION1' )
geompy.addToStudyInFather( PARTITION1, F1, 'F1' )
geompy.addToStudy( REVOLUTION1_1, 'REVOLUTION1_1' )
geompy.addToStudy( REVOLUTION1_2, 'REVOLUTION1_2' )
geompy.addToStudy( REVOLUTION1_3, 'REVOLUTION1_3' )
geompy.addToStudy( FUSE1, 'FUSE1' )
"""

# Configuração da página do Streamlit
st.title("Gerador de Script DIP")

# Inputs do usuário
st.header("Parâmetros de Entrada")
altura_sala = st.number_input("Altura da Sala (mm)", value=3000)
comprimento_sala = st.number_input("Comprimento da Sala (mm)", value=5000)
diametro_entrada = st.number_input("Diâmetro de Entrada (mm)", value=100)
altura_dip = st.number_input("Altura DIP (mm)", value=200)

# Botão para gerar o script
if st.button("Gerar Script"):
    # Gera o script com os parâmetros fornecidos
    script = gerar_dip(altura_sala, comprimento_sala, diametro_entrada, altura_dip)
    
    # Exibe o conteúdo do script na página
    st.text_area("Script Gerado", script, height=400)
    
    # Cria o botão de download do arquivo gerado
    st.download_button(
        label="Baixar Script",
        data=script,
        file_name="script_dip.py",
        mime="text/plain"
    )

