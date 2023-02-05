from PySimpleGUI import PySimpleGUI as sg
import sqlite3
import random
import pandas as pd


#escolhendo tema da Interface
sg.theme('DarkBlue13')
#criando arquivo do Banco de Dados
con=sqlite3.connect("base_de_dados.db")
cur=con.cursor()


sql="""CREATE TABLE IF NOT EXISTS paciente(codigo TEXT NOT NULL PRIMARY KEY ,nome TEXT NOT NULL, dia TEXT NOT NULL, mes TEXT NOT NULL, ano TEXT NOT NULL, municipio TEXT NOT NULL) """
cur.execute(sql)
con.commit()

#Todas as funçoes sao criaçao da interface
def Janela_cadastro():
    layout=[
        [sg.Text('Nome'),sg.Input(key='nome')],
        [sg.Text("Dia"),sg.Input(key='dia')],
        [sg.Text("Mes"),sg.Combo(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],key="mes")],
        [sg.Text("Ano"),sg.Input(key='ano')],
        [sg.Text('Municipio')],
        [sg.Combo(["Paudalho","Carpina","Tracuanhem","Nazare"],key="municipio")],
        [sg.Button('Cadastrar')] ,
        [sg.Button('Voltar')]
]

    return sg.Window('Cadastro de Paciente',layout=layout,finalize=True)

def JanelaInicial():
    layout=[
        [sg.Button("Cadastro"),sg.Button("Cosulta"),sg.Button("Alterar")],
        [sg.Button("Gerar Excel Mes"),sg.Button("Gerar Excel Dia")]
        ]
    
    return sg.Window('Menu Inicial',layout=layout,finalize=True)

def JanelaConsulta():
    layout=[
       [sg.Text("Codigo da Paciente"),sg.Input(key="codigo")],
       [sg.Button("Consultar"),sg.Button("Voltar")],
       [sg.Output(size=(50,20))]
    ]
    return sg.Window('Consulta',layout=layout,finalize=True)


def JanelaAltera():

    layout=[
        [sg.Text("Insira o Codigo da Paciente"),sg.Input(key="codigo")],
        [sg.Button("Proseguir"),sg.Button("Voltar")],
        [sg.Output(size=(60,10))]

    ]
    return sg.Window('Alteracao',layout=layout,finalize=True)

def JanelaAltera2():
      layout=[
        [sg.Text('Nome'),sg.Input(key='nome')],
        [sg.Text("Dia"),sg.Input(key='dia')],
        [sg.Text("Mes"),sg.Combo(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],key="mes")],
        [sg.Text("Ano"),sg.Input(key='ano')],
        [sg.Text('Municipio')],
        [sg.Combo(["Paudalho","Carpina","Tracuanhem","Nazare"],key="municipio")],
        [sg.Button('Cadastrar')] ,
        [sg.Button('Voltar')]
      ]
      return sg.Window('Alteracao',layout=layout,finalize=True)

def JanelaExcel():
    layout=[
        [sg.Text("Ano"),sg.Input(key="ano")],
        [sg.Text("Mes"),
        sg.Combo(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],key="mes")],
        [sg.Text('Municipio')],
        [sg.Combo(["Paudalho","Carpina","Tracuanhem","Nazare"],key="municipio")],
        [sg.Button("Exportar"),sg.Button("Voltar")]
        
    ]
    return sg.Window('Excel',layout=layout,finalize=True)

def JanelaExcelDia():
    layout=[ 
        [sg.Text("Dia"),sg.Input(key="dia")],
        [sg.Text("Ano"),sg.Input(key="ano")],
        [sg.Text("Mes"),
        sg.Combo(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],key="mes")],
        [sg.Text('Municipio')],
        [sg.Combo(["Paudalho","Carpina","Tracuanhem","Nazare"],key="municipio")],
        [sg.Button("Exportar"),sg.Button("Voltar")]
        
    ]
    return sg.Window('Excel',layout=layout,finalize=True)

def Janela_Gerar_Etiqueta_Mes():
    layout= [
    [sg.Text("Ano"),sg.Input( key="ano")],
    [sg.Text("Mes"), sg.Combo(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"],key="mes")],
    [sg.Text('Municipio')],
    [sg.Combo(["Paudalho","Carpina","Tracuanhem","Nazare"],key="municipio")],
    [sg.Button("Gerar"),sg.Button("Voltar")]
    
    ]
    return sg.Window('Gerar Etiqueta Mes',layout=layout,finalize=True)







janelaInicio,janelaCadastro,janelaConsulta,janelaAltera,janelaAltera2,janelaExcel,janelaDia,janelaEtiquetaMes=JanelaInicial(),None,None,None,None,None,None,None
codigoAltera=None
while True:
    window,event,values=sg.read_all_windows()

    if window==janelaInicio and event== sg.WIN_CLOSED:
        break
    
    elif window==janelaInicio and event=='Cadastro':
        janelaCadastro=Janela_cadastro()
    
    elif window==janelaCadastro and event=='Voltar' :
        janelaCadastro.close()

    elif window==janelaCadastro and event=='Cadastrar':
        codigo=random.randint(1000,999999)
        nome=values['nome']
        dia=values['dia']
        mes=values['mes']
        ano=values['ano']
        municipio=values['municipio']
        print(codigo)

        if not nome or not dia or not mes or not ano or not municipio:
            sg.popup_error("Insira valor em todos os campos")
        
        else:
            inserir="""INSERT INTO paciente (codigo,nome,dia,mes,ano,municipio)
        
            VALUES('{}','{}','{}','{}','{}','{}')""".format(codigo,nome,dia,mes,ano,municipio)

            cur.execute(inserir)
            con.commit()
            sg.popup("Cadastrado com Sucesso")
    
    elif window==janelaInicio and event=="Cosulta":
        janelaConsulta=JanelaConsulta()
    
    elif window==janelaConsulta and event=="Voltar":
        janelaConsulta.close()
    
    elif window==janelaConsulta and event=="Consultar":
        codigo=values["codigo"]
        if not codigo:
            sg.popup("Insira o Codigo pra  consultar")
        else:
            print("codigo/nome/dia/mes/ano/municipio ")
        

            consulta="""SELECT codigo,nome,dia,mes,ano,municipio 
            FROM paciente
            WHERE codigo ='{}'
            """.format(codigo)
            cur.execute(consulta)
            print (cur.fetchall())
            print("___________________________________________")
    
    elif(window==janelaInicio and event=="Alterar"):
        janelaAltera=JanelaAltera()
    
    elif(window==janelaAltera and event=="Proseguir"):
        codigo=values['codigo']
        codigoAltera=codigo
        if not codigo:
            sg.popup("Insira o codigo da paciente")
        
        else:
            consulta="""SELECT codigo,nome,dia,mes,ano,municipio 
            FROM paciente
            WHERE codigo ='{}'
            """.format(codigo)
            cur.execute(consulta)
           
            print (cur.fetchall())
            print("___________________________________________")
            janelaAltera2=JanelaAltera2()

    elif window==janelaAltera2 and event=="Cadastrar":
        nome=values['nome']
        dia=values['dia']
        mes=values['mes']
        ano=values['ano']
        municipio=values['municipio']

        if not nome or not dia or not mes or not ano or not municipio:
            sg.popup_error("Falta inserir dados por favor complete :)")
        else:
            alteracao=""" UPDATE paciente SET nome='{}',dia='{}',mes='{}',ano='{}', municipio='{}' WHERE codigo='{}' """.format(nome,dia,mes,ano,municipio,codigoAltera)

            cur.execute(alteracao)
            con.commit()

            sg.popup("Modificado com Sucesso")
    
    
    elif window==janelaAltera2 and event=='Voltar':
        janelaAltera2.close()
    
    elif window==janelaAltera and event=="Voltar":
        janelaAltera.close()
    
    elif window==janelaInicio and event=="Gerar Excel Mes":
        janelaExcel=JanelaExcel()
    
    elif window==janelaExcel and event=="Exportar":

        ano=values['ano']
        mes=values['mes']
        municipio=values['municipio']

      

        if not ano and not mes:
            sg.popup_error("Por favor insira ano e mes")
        
        else:
            seleciona=""" SELECT * FROM paciente WHERE
            mes='{}'AND ano='{}' AND municipio='{}'""".format(mes,ano,municipio)
            cur.execute(seleciona)

            exporta=cur.fetchall()

            print(exporta)

            exporta=pd.DataFrame(exporta,columns=['codigo','nome','dia','mes','ano','municipio'])
            exporta.to_excel('tabelas'+'_'+municipio+'_'+mes +'_'+ano+'.xlsx')
            con.commit()
            sg.popup("Excel Gerado com sucesso")
    

    elif window==janelaExcel and event=="Voltar":
        janelaExcel.close()

    elif window==janelaInicio and event=="Gerar Excel Dia":
        janelaDia=JanelaExcelDia()
    
    elif window==janelaDia and event=="Exportar":
        dia=values['dia']
        mes=values['mes']
        ano=values['ano']
        municipio=values['municipio']

        if not dia or not mes or not ano:
            sg.popup_error("Insira valor em todos os Campos")
        
        else:
             seleciona=""" SELECT * FROM paciente WHERE 
             dia='{}'AND mes='{}'AND ano='{}' AND municipio='{}'""".format(dia,mes,ano,municipio)
             cur.execute(seleciona)
             exporta=cur.fetchall()
             print(exporta)
             exporta=pd.DataFrame(exporta,columns=['codigo','nome','dia','mes','ano','municipio'])
             exporta.to_excel('tabelas'+'_'+municipio+'_'+dia +'_'+mes +'_'+ano+'.xlsx')
             con.commit()
             sg.popup("Excel Gerado com sucesso")
    
    elif window==janelaDia and event=="Voltar":
        janelaDia.close()         
    
   
           
        

        
    
             



    

           



    






    
    

    
    
    



       
        



       





    

    
