from modulos import Casa, Pessoa

casa_da_ana = Casa()
ana =Pessoa('Ana')

ana.set_local(casa_da_ana)
casa_da_ana.set_propietario(ana)

propietario = casa_da_ana.get_propietario()
propietario.se_apresentar()

ana.apresentar_local()