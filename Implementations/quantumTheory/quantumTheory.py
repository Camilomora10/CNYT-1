from sys import stdin
from classicalToQuantum import *
import numpy as np
from numpy import linalg as Alg
## Tema: observables del libro, Quantum Computing for Computer Scientists


def Length( vect ):
    
    acu = 0
    for x in range( len( vect )):
        acu += (module(vect[x]))**2
    return math.sqrt(acu)
        
def normalizate( vect ):
    length = Length( vect)
    for x in range( len( vect ) ):
        vect[ x ] = [vect[x][0]/length,vect[x][1]/length]
    return vect


def bra( vect  ):
    return adjointVector( vect )
    

def transicion( vect1 ,vect2):
    ##(rvs hc)  el bra a vect1
    return internalProduct( vect1 , vect2)    

def probability( vector, position ):
    length = Length( vector)
    if ( 0<= position < len( vector) ):
        return float("{0:.4f}".format( module(vector[position])**2 / length**2 ));

def OmegaPsi( psi, omega ):
    return internalProduct( actionMatrixOnVector( omega, psi) , psi)[0]

def DeltaPsi( omega, expectedValue ):
    
    return subMat( omega ,multiEscalMat( expectedValue, identityMatrix( omega ) ) )

def matrixPsi( matrix, psi ):
    ## rvs pq al llmse 2 veces cmba
    actionMatrixOnVector(matrix, adjointVector(psi))
    vect = actionMatrixOnVector(matrix, adjointVector(psi))
    
    ##n dbra ser(psi) adjoint sino psi.
    
    return float( "{:.2f}".format(multVector( vect,adjointVector(psi)) [0] ) )

def variance( psi, omega):
    expectedValue = float("{:.2f}".format(OmegaPsi( psi, omega ))[:-1])
    deltaPsi = DeltaPsi( omega ,[expectedValue ,0.0])
    matrixOfVariance = multiplicaMat( deltaPsi, deltaPsi)
    return matrixPsi( matrixOfVariance,psi )


def describeAnObservable( psi, matrix ):
    if ( isHermitan( matrix )):
        mean = float("{:.2f}".format(OmegaPsi( psi, matrix ))[:-1])
        
        return [variance( psi, matrix),mean]
    return None


def EigenValues( omega ):
    # x Eigenvalor, v Eigenvector = Alg.eig(matrix), donde Alg es la libreria linalg 
    observable = np.array(omega)
    (eigenValues,eigenvector) = Alg.eig(observable)
    return [[eigenValues[x].real,eigenValues[x].imag ] for x in range( len( eigenValues ) )],eigenvector
            

    
    


#Author : Iván Camilo Rincón Saavedra
