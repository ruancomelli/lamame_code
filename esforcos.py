import numpy

# RELACAO DE TRANSMISSAO GLOBAL
rtg = 1/5.25 # = EP_f / PC_f

# MOTOR
#MT_p = 1/4 # [cv]
MT_p = 183.8747 # [W]
MT_v = 220 # [V]
MT_i = 2 # [A]
MT_f = 325/12 # [Hz]
MT_rpm = 1625 # [rpm]

# POLIA DO MOTOR
PM_d = 60E-3 # [m]
PM_f = MT_f

# POLIA DO CAMBIO
PC_d = 124E-3 # [m]
PC_f = PM_d / PC_d * PM_f

# TREVO
TR_fc = 27.3E-3 # [m]
TR_hf = 11E-3 # [m]
TR_lb = 20E-3 # [m]
TR_hc = 12.7E-3 # [m]
TR_df = 15E-3 # [m]

# EIXO PRINCIPAL
EP_d = 15E-3 # = TR_df [m]
EP_hT = TR_hc

# PINO
P_d = 8E-3 # [m]

# ENGRENAGEM
E_dp = 32.8E-3 # [m]
E_db = 30.40E-3 # [m]
E_di = 8E-3 # [m]
E_h = 25E-3 # [m]
E_he = 22E-3 # [m]

# CAIXA DE ENGRENAGEM
C_db = 84E-3 # [m]
C_dp = C_db / E_db * E_db

# EIXO INTERMEDIARIO
EI_d = C_dp - E_dp

# ESFORCOS E FREQUENCIAS

PC_tq = MT_p / (2 * numpy.pi * PC_f)

E_f = rtg * (C_dp / E_dp) * PC_f
E_tq = (PC_f / E_f) * (PC_tq / 4)
E_p = E_tq * 2 * numpy.pi * E_f

P_f = (E_dp / C_dp) * E_f
P_tq = (MT_p/4) / (2 * numpy.pi * P_f)
P_fa = P_tq / TR_fc
P_p = P_tq * 2 * numpy.pi * P_f

TR_fa = P_fa
TR_f = P_f
TR_tq = 4*P_tq

EP_tq = TR_tq
EP_f = TR_f


# MODOS DE FALHA
TR_t_arrancar = TR_fa / (TR_lb * TR_hf)
TR_t_cortar = TR_fa / (2 * TR_hf * (TR_lb-P_d)/2 )

P_t = P_fa / (numpy.pi * (P_d/2)**2)

EP_t = 2 * EP_tq / (numpy.pi * EP_hT * EP_d)
TR_t_desacoplar = 2 * TR_tq / (numpy.pi * TR_hc * TR_df)


# EXPORTAR PARA CSV
def summary(csvFile, matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != 3:
            raise ValueError("Error trying to export {} file, data size do not agree. Matrix line {} != 3".format(filename, len(matrix[i])))
    for i in range(len(matrix)):
        csvFile.write("{},{:g},{}\n".format(matrix[i][0], matrix[i][1], matrix[i][2]))
        # what is being exported, value, unit

filename = "esforcos_e_frequencias.csv"
csvFile = open(filename,"w")
matrix = [
    ["Potencia do motor", MT_p, "W"],
    ["Frequencia do motor", MT_f, "Hz"],
    ["Frequencia da polia do motor", PM_f, "Hz"],
    ["Diametro da polia do motor", PM_d, "m"],
    ["Diametro da polia do cambio", PC_d, "m"],
    ["Torque na polia do cambio", PC_tq, "N.m"],
    ["Diametro primitivo do eixo intermediario", EI_d, "m"],
    ["Frequencia da engrenagem", E_f, "Hz"],
    ["Torque na engrenagem", E_tq, "N.m"],
    ["Potencia da engrenagem", E_p, "W"],
    ["Frequencia do pino", P_f, "Hz"],
    ["Torque no pino", P_tq, "N.m"],
    ["Potencia do pino", P_p, "W"],
    ["Forca no pino", P_fa, "N"],
    ["Tensao de cisalhamento no pino", P_t, "Pa"],
    ["Frequencia do trevo", TR_f, "Hz"],
    ["Torque no trevo", TR_tq, "N.m"],
    ["Forca no furo do pino do trevo", TR_fa, "N"],
    ["tensao cisalhante de arrancar o trevo", TR_t_arrancar, "[Pa]"],
    ["tensao cisalhante de cortar o trevo", TR_t_cortar, "[Pa]"],
    ["tensao cisalhante de descacoplar o trevo do eixo principal", TR_t_desacoplar, "[Pa]"],
    ["Frequencia do eixo principal", EP_f, "Hz"],
    ["Torque no eixo principal", EP_tq, "N.m"],
    ["tensao cisalhante de descacoplar o eixo principal do trevo", EP_t, "[Pa]"],
    # ["", , ""],
]

summary(csvFile, matrix)
csvFile.close()
