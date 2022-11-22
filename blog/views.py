from django.shortcuts import render
from .models import genNum
from django.http import HttpResponse
import math
from numpy import mean, var
import numpy as np

# Create your views here.
def datos_list(request):
    posts = genNum.objects.all()
    dic = {'valores': posts}
    sumas = []
    for post in posts:
        suma = 0
        suma = post.val1 + post.val3 + post.val4
        sumas.append(suma)
    dic["sumas"] = sumas
    return render(request, 'blog/registros.html', dic)


def inicio(request):
    return render(request, 'blog/inicio.html')


# ALGORITMO KNN
def algKNN_list(request):
    return render(request, 'blog/algoritmoKNN.html')

def buscar(request):
    if request.method == 'GET':
        return render(request, 'blog/algoritmoKNN.html', {})
    else:

        k = int(request.POST["k"])
        x1 = int(request.POST["x1"])
        x2 = int(request.POST["x2"])
        x3 = int(request.POST["x3"])
        db = genNum.objects.all()
        distancia = []
        for i in range(len(db)):
            val = math.sqrt(((x1-db[i].val1)**2)+((x2-db[i].val3)**2)+((x3-db[i].val4)**2))
            distancia.append((db[i].val2, val))
        #cont = { 'dist': distancia}
        dic = {}
        letter = []
        num = []
        for i in distancia:
            a, b = i
            num.append(b)
            letter.append(a)

        dic["letra"] = letter
        dic["number"] = num

        listK= distancia[:k]
        knn ={}
        letras=[]
        for i in listK:
            if i[0] in letras:
                knn[i[0]]+=1
            else:
                letras.append(i[0])
                knn[i[0]]=1
        #cont['knn']=knn
        return render(request, 'blog/algoritmoKNN.html', dic)



#BAYES
def alg_cbi(request):
    bd = list(genNum.objects.all())
    new_bd = genNum.objects.values('val2','val1','val3','val4').order_by('val2')
    letra=[]
    bd_final={}
    probabilidad=""
    cont=0
    for i in range(len(new_bd)):
        if bd[i].val2 in letra:
            cont+=1
        else:
            valor = genNum.objects.filter(val2=bd[i].val2)
            letra.append(bd[i].val2)
            suma_num1=[]
            suma_num3=[]
            suma_num4=[]
            for j in list(valor):
                suma_num1.append(j.val1)
                suma_num3.append(j.val3)
                suma_num4.append(j.val4)
            media_num1=mean(suma_num1)
            varianza_num1= 0.5
            media_num3=mean(suma_num3)
            varianza_num3=0.5
            media_num4=mean(suma_num4)
            varianza_num4=0.5
            bd_final[bd[i].val2]=(media_num1,varianza_num1,media_num3,varianza_num3,media_num4,varianza_num4)
    para_evidencia = {}
    if request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        z = int(request.POST['z'])
        p_letra = 1/len(bd_final)
        for l in range(len(bd_final)):
            para_evidencia[letra[l]]= pre_posteriori(bd_final[letra[l]][0], bd_final[letra[l]][2], bd_final[letra[l]][4], bd_final[letra[l]][1], bd_final[letra[l]][3], bd_final[letra[l]][5],x,y,z)

        evidcia = evidencia(para_evidencia,letra,p_letra)
        probabilidad = post_posteriori(para_evidencia,evidcia,letra)
        cont = {'letra': probabilidad}
    else:
        return render(request, 'blog/algCBI.html', {})
    return render(request,'blog/algCBI.html', cont)

def pre_posteriori(media1,media3,media4,var1,var2,var3,x,y,z):
    p_num1 = (1/math.sqrt(2*math.pi*var1))* math.e*(pow(x-media1,2)/(2*var1))
    p_num3 = (1/math.sqrt(2*math.pi*var2))* math.e*(pow(y-media3,2)/(2*var2))
    p_num4 = (1/math.sqrt(2*math.pi*var3))* math.e*(pow(z-media4,2)/(2*var3))

    return (p_num1,p_num3,p_num4)

def post_posteriori(para_evidencia, evidencia,letras):
    rel = {}
    valores_rel =[]
    letra=""
    for i in range(len(para_evidencia)):
        val = (para_evidencia[letras[i]][0]*para_evidencia[letras[i]][1]*para_evidencia[letras[i]][2]) / evidencia
        rel[letras[i]]= val
        valores_rel.append(val)
    maximo = max(valores_rel) 
    keys = list(rel.keys())  
    for j in range(len(rel)):
        if rel[letras[j]] == maximo:
            letra = keys[j]
    return letra
def evidencia(para_evidencia,letras,p_letra):
    rel=[]
    for i in range(len(para_evidencia)):
        rel.append(p_letra*para_evidencia[letras[i]][0]*para_evidencia[letras[i]][1]*para_evidencia[letras[i]][2])
    resultado = sum(rel)
    return resultado

def calcular_varianza(arr, is_sample=False):
    media = (sum(arr) / len(arr))
    diff = [(v - media) for v in arr]
    sqr_diff = [d**2 for d in diff]
    sum__sqr_diff = sum(sqr_diff)

    if is_sample == True:
        variance = sum__sqr_diff/(len(arr)-1)
    else:
        variance = sum__sqr_diff/(len(arr)-1)
    return variance



#REGRESION LOG

def regresionLog(request):
    return render(request, 'blog/algoritmoRL.html')

def interpretar(request):
    if request.GET["x1"].isdigit() and request.GET["x2"].isdigit():
        x = int(request.GET["x1"])
        y = int(request.GET["x2"])
        datos = genNum.objects.all()
        b = calcConstante(datos)
        resultado  = valorReferente(datos, x, y, b)
        print(f"RESULT {resultado}")
        return render(request, 'blog/ResultRL.html', {'consulta': resultado} )
    else:
        mensaje = "Te falto llenar o llenaste incorrectamente, recuerda que deben ser valores numericos"
    return HttpResponse(mensaje)

def valorReferente(datos, x1, x2, b):
    a1 = 0
    a2 = 0
    caracter = ''
    for i in datos:
        a1 = i.val1
        caracter = i.val2
        a2 = i.val3
        break
    salida = 1/(1 + np.exp(-(a1*x1 + a2*x2 + b)))
    if salida > 0.5:
        respuesta = f'El caracter obtenido es: {caracter}'
    else:
        respuesta = f'No hay caracter que haya podido encontrar: {caracter}'
    return respuesta

def calcConstante(datos):
    x = []
    y = []
    xCuadrada = 0
    xy = 0
    for i in datos:
        xCuadrada = xCuadrada + i.val1**2
        xy = xy + i.val1 * i .val3
        x.append(i.val1)
        y.append(i.val3)
    xSum = sum(x)
    ySum = sum(y)
    constante = (xCuadrada*ySum - xy*xSum)/(datos.count()*xCuadrada-xSum**2)
    return constante