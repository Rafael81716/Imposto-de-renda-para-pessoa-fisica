from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') 

#Usando o método abaixo é possivel referenciar outras paginas html, usando return

    
@app.route('/calcular', methods=['POST'])
def calcular():
    #Entradas do formlário
    RendaBruta = int(request.form.get('RendaBruta'))
    NumeroDependentes = int(request.form.get('dependentes'))
    DespesaEnsino = int(request.form.get('ensino'))
    DespesaPensao = int(request.form.get('pensaoAlimenticia'))
    DespesaMedica = int(request.form.get('medica'))
    Previdencias = int(request.form.get('INSS'))
    TipoImposto = request.form["tipoImposto"]

    v1 = 0
    #valores base para os if's
    valoresMensal = [1903.98, 2826.65, 3751.05, 4664.68]
    valoresAnual = [22847.76, 33919.8, 45012.60, 55976.16]
    
    #dependentes
    if NumeroDependentes >= 0 and TipoImposto == "Mensal":
        v1 = (189.59 * NumeroDependentes)
    if NumeroDependentes >= 0 and TipoImposto == "Anual":
        v1 = ( 2275.08 * NumeroDependentes) 

    somavalores = v1 +  DespesaEnsino + DespesaPensao + DespesaMedica + Previdencias 

    rendal = RendaBruta - somavalores
    
    if TipoImposto == "Anual":
        if rendal < valoresAnual[0]:
            valoraPagar = 0


        if rendal >= valoresAnual[0] and rendal < valoresAnual[1]:
            rendas = rendal - valoresAnual[0] 
            valoraPagar = (rendas/100) * 7.5
            valoraPagar = "{:.2f}".format(valoraPagar)
            
            
            
        if rendal >= valoresAnual[1] and rendal < valoresAnual[2]:
            rendas = rendal - valoresAnual[0] - (valoresAnual[1] - valoresAnual[0])
            valoraPagar = (rendas/100) * 15 + 834.40
            valoraPagar = "{:.2f}".format(valoraPagar)
            
            

        if rendal >= valoresAnual[2] and rendal < valoresAnual[3]:
            rendas = rendal - valoresAnual[0] - (valoresAnual[1] - valoresAnual[0]) - (valoresAnual[2] - valoresAnual[1])
            valoraPagar = (rendas/100) * 22.5 + 834.40 + 1663.92
            valoraPagar = "{:.2f}".format(valoraPagar)
            
            

        if rendal >= valoresAnual[3]:
            rendas = rendal - valoresAnual[0] - (valoresAnual[1] - valoresAnual[0]) - (valoresAnual[2] - valoresAnual[1]) - (valoresAnual[3] - valoresAnual[2])
            valoraPagar = (rendas/100) * 27.5 + 834.40 + 1663.92 + 2466.80
            valoraPagar = "{:.2f}".format(valoraPagar)
            
            

        
    if TipoImposto == "Mensal":
        if rendal < valoresMensal[0]:
            valoraPagar = 0

        if rendal > valoresMensal[0] and rendal < valoresMensal[1]:
            rendas = rendal - valoresMensal[0] 
            valoraPagar = (rendas/100) * 7.5
            valoraPagar = "{:.2f}".format(valoraPagar)
            
            
            
        if rendal > valoresMensal[1] and rendal < valoresMensal[2]:
            rendas = rendal - valoresMensal[0] - (valoresMensal[1] - valoresMensal[0])
            valoraPagar = (rendas/100) * 15 + 69.25
            valoraPagar = "{:.2f}".format(valoraPagar)
            
            

        if rendal > valoresMensal[2] and rendal < valoresMensal[3]:
            rendas = rendal - valoresMensal[0] - (valoresMensal[1] - valoresMensal[0]) - (valoresMensal[2] - valoresMensal[1])
            valoraPagar = (rendas/100) * 22.5 + 69.25 + 138.66
            valoraPagar = "{:.2f}".format(valoraPagar)
            
            

        if rendal > valoresMensal[3]:
            rendas = rendal - valoresMensal[0] - (valoresMensal[1] - valoresMensal[0]) - (valoresMensal[2] - valoresMensal[1]) - (valoresMensal[3] - valoresMensal[2])
            valoraPagar = (rendas/100) * 27.5 + 69.25 + 138.66 + 205.57
            valoraPagar = "{:.2f}".format(valoraPagar)
            
     
    return render_template ('calcular.html', rendaBruta = RendaBruta, dependentes = NumeroDependentes, 
    tipoImposto = TipoImposto, ensino = DespesaEnsino, pensao = DespesaPensao, medica = DespesaMedica, 
    INSS = Previdencias, rendaLiquida = rendal, Imposto = valoraPagar)
    
    