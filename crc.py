def xor(a, b): 
    # initialize result 
    result = ['0' if a[i] == b[i] else '1' for i in range(1, len(b))] 

    return ''.join(result) 
   
   
# Performs Modulo-2 division 
def divBinaria(divident, divisor): 
    # Number of bits to be XORed at a time. 
    pos = len(divisor) 
    tmp = divident[0 : pos] 
   
    while pos < len(divident): 
        tmp = xor(divisor, tmp) if tmp[0] == '1' else xor('0'*pos, tmp)
        tmp += divident[pos]
        pos += 1

    tmp = xor(divisor, tmp) if tmp[0] == '1' else xor('0'*pos, tmp) 

    remainder = tmp 
    return remainder 
   

def encodeData(data, key): 
    lenght_data = len(key) 
    all_data = data + '0'*(lenght_data-1) 
    remainder = divBinaria(all_data, key) 
   
    codeword = data + remainder 
    return codeword     


mensaje = input("Indique el mensajea a enviar: ") 
data =(''.join(format(ord(x), 'b') for x in mensaje)) 
print (data) 

#polinimio escogido 0x8d95
#x (x+1)(x^8 +x^7 +x^3 +x^2 +1)
key = "111000111"
  
ans = encodeData(data,key)
print("Cod: " + ans) 
test = encodeData(ans, key)
print("Cor: " + test)
test = encodeData(ans + '1', key)
print("Bad: " + test)
