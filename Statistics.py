# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
import UploadRecord as up


def graph(ra, password):
        _, _, cod, cred, med, _, per, ano = up.GetRec(ra, password)

        # Aqui joga fora todos os dados relacionados ao ENADE, ja que esta nao e uma disciplina regular
        badcod = cod.index('ENADE-I')
        del cod[badcod]
        del cred[badcod]
        del med[badcod]
        del per[badcod]
        del ano[badcod]

        # Média por semestre
        med = np.array(med, dtype='float64')
        ano = np.array(ano, dtype='int32')
        cred = np.array(cred, dtype='int32')
        semestre = []
        for x in range(len(ano)):
            semestre.append(str(ano[x]) + '-0' + str(per[x]))

        semestre = np.array(semestre, dtype='datetime64[M]')

        media_sem = []
        for x in np.unique(semestre):
            media_sem.append(np.average(med[np.where(semestre == np.datetime64(x))], weights = cred[np.where(semestre == np.datetime64(x))]))

        media_sem = np.array(media_sem, dtype='float64')


def subj_graph(ra, password):
    subj, _, cod, _, med, _, _, _ = up.GetRec(ra, password)
    badcod = cod.index('ENADE-I')
    del subj[badcod]
    del cod[badcod]
    del med[badcod]

    med = np.array(med, dtype='float64')

    plt.bar(cod, med)
    plt.show()
    plt.close()
    return 


def GPA():
    return
