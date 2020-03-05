import matplotlib.pyplot as plot
import numpy as np

from  matrixAndVectorLibrary import *

def finalMatrix( matrix ):
    row, column = len( matrix ), len( matrix[0] )
    for i in range( row ):
        nRow = []
        for j in range( column ):
            nRow.append( [( module( matrix[ i ][ j ] )**2 ),0])
            
        matrix[ i ]= nRow
    return matrix

def quantumProbabilisticSystem( matrix, vectIni, clicks ):
    if ( clicks  >= 0 ) and ( type( clicks ) is int ):
        length  = len( vectIni )
        copyMatrix = matrix[:]
        
        for x in range(clicks  ):
            matrix = multiplicaMat( matrix, copyMatrix)

        
        return finalMatrix( matrix )
    return -1

def multipleSlitQuantumExperiment( matrix , vectIni, clicks  ):
        return quantumProbabilisticSystem( matrix , vectIni, clicks  )

    

#Author : Iván Camilo Rincón Saavedra
