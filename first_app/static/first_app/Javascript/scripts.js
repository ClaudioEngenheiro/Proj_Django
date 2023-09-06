function insert(num)
{
    var numero = document.getElementById('Resultado').innerHTML;
    document.getElementById('Resultado').innerHTML = numero + num;
}

function Clean()
{
    document.getElementById('Resultado').innerHTML = "";
}

function calculo()
{
    var Resultado = document.getElementById('Resultado').innerHTML;
    if (Resultado)
    {
        //document.getElementById('Resultado').innerHTML = eval(Resultado); 
        let p1 = document.getElementById('p1').value;
        let p2 = document.getElementById('p2').value;     
        let Resultado = parseFloat(p1) + parseFloat(p2);    
        document.getElementById('Resultado').value = Resultado;   
    }
    else
    {
        document.getElementById('Resultado').innerHTML = "Digite..."
    }
}


    function soma(pA,pB)
    {
        let p1 = document.getElementById('p1').value;
        let p2 = document.getElementById('p2').value;     
        let Resultado = parseFloat(p1) + parseFloat(p2);    
        document.getElementById('Resultado').value = Resultado;
    }  
    
    function sub(p1,p2)
    {
        return p1 - p2;
    }

    function mult(p1,p2)
    {
        return p1 * p2;
    }

    function div(p1,p2)
    {
        return p1 / p2;
    } 
